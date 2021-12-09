import numpy as np

input = np.loadtxt('input/day8input', dtype='str', delimiter='\n')
print(input)

test = 'asdfasd | adsf'

test = test[test.index('|') + 2:]

for i in range(len(input)):
    input[i] = input[i][input[i].index('|') + 2:]

segments = [i.split(' ') for i in input]
list = []
for i in segments:
    for j in i:
        list.append(j)
print(list)

lengths = [2, 4, 3, 7]
count = 0
for i in list:
    for length in lengths:
        if len(i) == length:
            count += 1

print(count)