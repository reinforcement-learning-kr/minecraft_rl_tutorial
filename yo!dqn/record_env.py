import numpy as np
from minecraft_env import env
from utils.utils import *
from darknet import Darknet
import cv2
import torch.nn as nn
import pickle as pkl
import pandas as pd

CUDA = torch.cuda.is_available()

env = env.MinecraftEnv()
env.init(
    allowContinuousMovement=["move", "turn"],
    continuous_discrete=False,
    videoResolution=[800, 600]
    )

num_classes = 80
confidence = 0.5
nms_thesh = 0.4
classes = load_classes('data/coco.names') 
print("Loading network.....")
model = Darknet("cfg/yolov3.cfg")
model.load_weights('save_model/yolov3.weights')
print("Network successfully loaded")

model.net_info["height"] = 416
inp_dim = int(model.net_info["height"])
assert inp_dim % 32 == 0 
assert inp_dim > 32

video = cv2.VideoWriter('record/mob-fun.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, (800, 600))

done = False
write = False
batch_size = 1

for i in range(1):
    score = 0
    count = 0
    env.reset()
    while True:
        count += 1
        env.render(mode="rgb_array")
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        num_states = info['number_of_observations_since_last_state']
        num_rewards = info['number_of_rewards_since_last_state']
        observation = info['observation']
        # print(num_states, num_rewards)

        score += reward
        obs = np.reshape(obs, (600, 800, 3))
        img, origin_img, dim = prep_image(obs, inp_dim)

        with torch.no_grad():
            prediction = model(img, CUDA)

        prediction = write_results(prediction, confidence, num_classes, 
                                   nms = True, nms_conf = nms_thesh)
            
        # print('prediction: ', prediction)

        if type(prediction) == int:
            continue

        output = prediction
        i += 1

        
        if CUDA:
            torch.cuda.synchronize()
    
        try:
            output
        except NameError:
            print("No detections were made")
            exit()
        
        dim = (800, 600)
        im_dim  = torch.FloatTensor(dim)
        scaling_factor = torch.min(inp_dim/im_dim)
        
        output[:, [1,3]] -= (inp_dim - scaling_factor*im_dim[0])/2
        output[:, [2,4]] -= (inp_dim - scaling_factor*im_dim[1])/2
        
        
        
        output[:, 1:5] /= scaling_factor
        output[:, [1,3]] = torch.clamp(output[:, [1,3]], 0.0, im_dim[0])
        output[:, [2,4]] = torch.clamp(output[:, [2,4]], 0.0, im_dim[1])

        colors = pkl.load(open("pallete", "rb"))

        def write(x, result):
            c1 = tuple(x[1:3].int())
            c2 = tuple(x[3:5].int())
            img = result
            cls = int(x[-1])
            label = "{0}".format(classes[cls])
            color = random.choice(colors)
            cv2.rectangle(img, c1, c2,color, 1)
            t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1 , 1)[0]
            c2 = c1[0] + t_size[0] + 3, c1[1] + t_size[1] + 4
            cv2.rectangle(img, c1, c2,color, -1)
            cv2.putText(img, label, (c1[0], c1[1] + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225,255,255], 1)
            return img
        
        list(map(lambda x: write(x, origin_img), output))
        # result = write(output, origin_img)
          
        det_name = 'det/det_' + str(count) + '.jpg'
        
        cv2.imwrite(det_name, origin_img)

        if done:
            cv2.destroyAllWindows()
            video.release()
            print(str(i) + 'th episode score is ' + str(score))
            break

env.close()