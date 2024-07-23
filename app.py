import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

ages = np.random.randint(low=15, high=75, size=40)

print(ages)

labels = []

for age in ages:
    if age < 30:
        labels.append(0)
    else:
        labels.append(1)


for i in range(0,3):
    result = np.random.randint(0, len(labels) - 1)
    if labels[result] == 0:
        labels[result] = 1
    else:
        labels[result] = 0

plt.scatter(ages, labels, color='blue')
plt.show()