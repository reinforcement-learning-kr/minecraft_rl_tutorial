import matplotlib.pyplot as plt
import numpy as np

lines = open('log.txt').readlines()

scores = []
# print(len(lines))
for line in lines:
	score = line.split('  ')[5]
	score = score.split('\n')
	if len(score) > 1:
		scores.append(float(score[0]))

plt.plot(scores)
plt.show()