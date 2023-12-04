import matplotlib.pyplot as plt

x1 = [2, 15, 20, 5, 30, 26, 60]
y1 = [1, 5, 10, 18, 20, 25, 26]

x2 = [3, 20, 6, 15, 9, 30, 50, 62]
y2 = [2, 6, 11, 20, 22, 26, 25, 30]

plt.scatter(x1, y1, c='blue', label='Group 1')
plt.scatter(x2, y2, c='red', label='Group 2')

plt.title('Scatter plot of given x and y positions')
plt.xlabel('x values')
plt.ylabel('y values')

plt.legend()

plt.show()
