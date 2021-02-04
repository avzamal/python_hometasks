import numpy as np
import matplotlib.pyplot as plt


coordinates = np.zeros((100000, 2))
coord_A = np.array([0, 0])
coord_B = np.array([1, 0])
coord_C = np.array([0.5, 0.866])

first_coord = np.array([np.random.rand(), np.random.rand()])
try_again = True
while try_again:
    A1 = (coord_A[0] - first_coord[0]) * (coord_B[1] - coord_A[1]) - (coord_B[0] - coord_A[0]) * (coord_A[1] - first_coord[1])
    A2 = (coord_B[0] - first_coord[0]) * (coord_C[1] - coord_B[1]) - (coord_C[0] - coord_B[0]) * (coord_B[1] - first_coord[1])
    A3 = (coord_C[0] - first_coord[0]) * (coord_A[1] - coord_C[1]) - (coord_A[0] - coord_C[0]) * (coord_C[1] - first_coord[1])
    if A1 >= 0 and A2 >= 0 and A3 >= 0:
        current_coord = first_coord
        coordinates[0] = current_coord
        try_again = False
    else:
        first_coord = np.array([np.random.rand(), np.random.rand()])
for i in range(1, 100000):
    direction = np.random.randint(0, 3)
    if direction == 0:
        current_coord = current_coord / 2
    elif direction == 1:
        current_coord[0] = (1 + current_coord[0]) / 2
        current_coord[1] = current_coord[1] / 2
    elif direction == 2:
        current_coord = (coord_C + current_coord) / 2
    coordinates[i] = current_coord

plt.figure(figsize=(10, 8))
plt.scatter(coordinates[..., 0], coordinates[..., 1], s=0.01)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sierpiński triangle')
#plt.show()
plt.savefig('Random4.png', bbox_inches='tight', dpi=400)
