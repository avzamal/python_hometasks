import matplotlib.pyplot as plt


def file_len(fname):
    with open(fname) as f:
        length = 0
        for i in f:
            length += 1
    return length


line_lengths = []
file_name = '/Users/Zamalutdinov/Desktop/test.fasta'
file_lines = file_len(file_name)
full_line = []
with open(file_name) as file:
    for k in range(file_lines):
        line = file.readline().strip()
        if line[0] == '>':
            line_lengths.append(len(full_line))
            full_line = []
        else:
            full_line += line

plt.hist(line_lengths[1: len(line_lengths)], bins=25)
plt.title('FASTA length distribution')
plt.ylabel('Number')
plt.xlabel('Length')
#plt.show()
plt.savefig('Task2.png')
