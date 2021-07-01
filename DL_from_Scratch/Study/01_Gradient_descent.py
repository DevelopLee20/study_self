import matplotlib.pyplot as plt

w = 1.0
b = 1.0
x = [2,4,6,8]
y = [81,93,91,97]

for i in range(100):
  for x_i, y_i in zip(x,y):
    y_hat = x_i * w + b
    err = y_i - y_hat
    w_rate = x_i
    w = w + w_rate * err
    b = b + 1 * err
    print(err)

print("w: ",w)
print("b: ",b)
plt.scatter(x,y)
plt.plot([0.0,10],[80,100])
plt.show()