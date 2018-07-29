import gym
import marlo
import numpy as np

env = gym.make('CatchTheMobSinglePlayer-v0')
env.init(
    allowContinuousMovement=["move", "turn"],
    continuous_discrete=False,
    videoResolution=[800, 600]
    )


done = False
for i in range(100):
    score = 0
    env.reset()
    while True:
        env.render(mode="rgb_array")
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        score += reward
        print(reward)
        if done:
            print(str(i) + 'th episode score is' + str(score))
            break

env.close()