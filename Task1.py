import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 50, 10)
ys = np.array([2, 5, 6, 7, 9, 11, 14, 17, 22, 32])

plt.plot(xs, ys, color='red', marker='+')
plt.title('My line plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

#plt.show()
plt.savefig('Task1')