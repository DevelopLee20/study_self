import numpy as np
import matplotlib.pyplot as plt

data = [[2,81],[4,93],[6,91],[8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

plt.figure(figsize = (8,5))
plt.scatter(x,y)
plt.show()

x_data = np.array(x)
y_data = np.array(y)

a = 0
b = 0

# 학습률
lr = 0.03

# 반복 횟수
epochs = 2001

for i in range(epochs):
    y_hat = a * x_data + b
    error = y_data - y_hat
    a_diff = -(2/len(x_data)) * sum(x_data * (error))
    b_diff = -(2/len(x_data)) * sum(error)
    a = a - lr * a_diff
    b = b - lr * b_diff
    if i % 100 == 0:
        print("epochs = %.f, 기울기 = %.04f, 절편 = %.04f" % (i,a,b))

y_pred = a * x_data + b
plt.scatter(x,y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()