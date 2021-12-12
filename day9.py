import numpy as np

arr = np.loadtxt('input/day9', delimiter='\n', dtype='str')
arr2 = np.ones((len(arr), len(arr[0])), dtype=int)

for i in range(len(arr)):
    char = arr[i]
    for digit in range(len(char)):
        arr2[i][digit] = int(char[digit])

print(arr2)

lowPoints = []

for x in range(len(arr2[0])):
    for y in range(len(arr2)):
