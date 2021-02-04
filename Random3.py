import numpy as np
import matplotlib.pyplot as plt


coordinates = np.zeros((500, 2), dtype=float)
current_coord = np.array([0, 0], dtype=float)
for i in range(1, 500):
    axis = np.random.randint(0,2)
    movement = np.random.normal()
    if axis == 0:
        current_coord[0] += movement
    else:
        current_coord[1] += movement
    coordinates[i] = current_coord

plt.scatter(coordinates[..., 0], coordinates[..., 1], s=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
#plt.show()
plt.savefig('Random3.png', bbox_inches='tight')