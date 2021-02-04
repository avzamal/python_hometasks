from random import shuffle
import numpy as np
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt


def is_sorted(data) -> bool:
    return all(data[k] <= data[k + 1] for k in range(len(data) - 1))


def bogosort(data) -> list:
    while not is_sorted(data):
        shuffle(data)
    return data


d = {'len': [],
     'time': []}
full_list_for_sorting = np.random.randint(0, 200, size=50)
for i in range(2, 13):
    for j in range(3):
        list_for_sorting = full_list_for_sorting[0: i].tolist()
        start_time = time.process_time_ns()
        bogosort(list_for_sorting)
        final_time = time.process_time_ns() - start_time
        d['len'].append(i)
        d['time'].append(final_time)

plotting_data = pd.DataFrame(d)
sns.relplot(x="len", y="time", kind="line", data=plotting_data)
plt.xlabel('List length')
plt.ylabel('Sorting time')
plt.title('Bogosort timing')
plt.savefig('Random2_2.png', bbox_inches='tight')