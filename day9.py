import numpy as np

arr = np.loadtxt('input/day9', delimiter='\n', dtype='str')
arr2 = np.ones((len(arr), len(arr[0])), dtype=int)

for i in range(len(arr)):
    char = arr[i]
    for digit in range(len(char)):
        arr2[i][digit] = int(char[digit])

print(arr2)
print(arr2.size)

lowPoints = []

width = len(arr2[0]) - 1
height = len(arr2) - 1

for x in range(len(arr2[0])):
    for y in range(len(arr2)):
        point = arr2[y, x]
        print(x, y)
        if x == 0 and y == 0:
            if arr2[y, x + 1] > point and arr2[y - 1, x] > point:
                lowPoints.append(point)
        elif x == 0 and y == height:
            if arr2[y, x + 1] > point and arr2[y - 1, x] > point:
                lowPoints.append(point)
        elif x == width and y == 0:
            if arr2[y, x - 1] > point and arr2[y + 1, x] > point:
                lowPoints.append(point)
        elif x == width and y == height:
            if arr2[y, x - 1] > point and arr2[y - 1, x] > point:
                lowPoints.append(point)
        elif x == 0:
            if arr2[y + 1, x] > point and arr2[y - 1, x] > point and arr2[y, x + 1] > point:
                lowPoints.append(point)
        elif y == 0:
            if arr2[y, x + 1] > point and arr2[y, x - 1] > point and arr2[y - 1, x] > point:
                lowPoints.append(point)
        elif x == width:
            if arr2[y + 1, x] > point and arr2[y - 1, x] > point and arr2[y, x - 1] > point:
                lowPoints.append(point)
        elif y == height:
            if arr2[y, x + 1] > point and arr2[y, x - 1] > point and arr2[y - 1, x] > point:
                lowPoints.append(point)
        else:
            if arr2[y, x + 1] > point and arr2[y, x - 1] > point and arr2[y - 1, x] > point and arr2[y + 1, x] > point:
                lowPoints.append(point)

print(lowPoints)
for i in range(len(lowPoints)):
    lowPoints[i] += 1
print(sum(lowPoints))
