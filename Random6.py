import numpy as np
import matplotlib.pyplot as plt


coordinates = np.zeros((3000000, 2))
coord_1 = np.array([0, 0])
coord_2 = np.array([0.5, 0])
coord_3 = np.array([1, 0])
coord_4 = np.array([1, 0.5])
coord_5 = np.array([1, 1])
coord_6 = np.array([0.5, 1])
coord_7 = np.array([0, 1])
coord_8 = np.array([0, 0.5])
carpet_edges = [0, coord_1, coord_2, coord_3, coord_4, coord_5, coord_6, coord_7, coord_8]

current_coord = np.array([np.random.rand(), np.random.rand()])

for i in range(1, 3000000):
    direction = np.random.randint(1, 9)
    current_coord = (2 * carpet_edges[direction] + current_coord) / 3
    coordinates[i] = current_coord

plt.figure(figsize=(8, 6))
plt.scatter(coordinates[..., 0], coordinates[..., 1], s=0.001)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sierpiński carpet')
#plt.show()
plt.savefig('Random6.png', bbox_inches='tight', dpi=400)
