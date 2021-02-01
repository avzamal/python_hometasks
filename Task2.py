import sys
import matplotlib.pyplot as plt


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


line_lengths = []
file_name = sys.argv[1]
file_lines = file_len(file_name)
with open(file_name) as file:
    for k in range(file_lines//2):
        file.readline()
        line = file.readline().strip()
        line_lengths.append(len(line))

plt.hist(line_lengths, bins=25)
plt.title('FASTA length distribution')
plt.ylabel('Number')
plt.xlabel('Length')
#plt.show()
plt.savefig('Task2.png')