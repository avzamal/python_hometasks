import time
import random
import numpy as np
import matplotlib.pyplot as plt


def random_module():
    n = random.random()


def numpy_module(k):
    n = np.random.rand(k)


ns = np.arange(0, 200)
times_random = np.zeros(200)
times_numpy = np.zeros(200)
for i in range(1, 200):
    for z in range(100):
        start_time = time.process_time_ns()
        for k in range(i):
            random_module()
        time_rand = time.process_time_ns() - start_time
        times_random[i] += time_rand
        start_time_np = time.process_time_ns()
        numpy_module(i)
        time_np = time.process_time_ns() - start_time_np
        times_numpy[i] += time_np

plt.plot(ns, times_random/100, label='Random module')
plt.plot(ns, times_numpy/100, label='Numpy module')
plt.grid()
plt.xlabel('Numbers taken')
plt.ylabel('Computation time in ns')
plt.title('Comparison of random in random and numpy module')
plt.legend()
plt.show()
#plt.savefig('Random1.png')
