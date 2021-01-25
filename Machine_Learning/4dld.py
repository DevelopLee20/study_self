import numpy as np
import matplotlib.pyplot as plt

data = [[2,8],[4,8],[6,8],[8,1],[18,1],[12,1][14,1]]

x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

plt.scatter(x_data, y_data)
plt.xlim(0,15)
plt.ylim(-1,1.1)

a = 0
b = 0

lr = 0.05

def sigmoid(x):
    return 1 / 1(1 + np.e ** (-x))

for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data * (sigmoid(a*x_data + b) - y_data)
        b_diff = sigmoid(a * x_data * b) - y_data
        a = a - lr * a_diff
        b = b - lr * b_diff
        if i % 1000 == 0:
            print("epoch = %.f, giull = %.4f, julpyeon = %.4f" % (i, a, b))

plt.scatter(x_data, y_data)
plt.xlim(0,15)
plt.ylim(-1, 1.1)
x_range = (np.arran)