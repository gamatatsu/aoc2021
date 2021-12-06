
with open('input/day6') as f:
    lines = f.readlines()

fish = str.split(lines[0], ',')
fish = [int(i) for i in fish]
print(fish)


def day(arr):
    for i in range(len(arr)):
        arr[i] -= 1
        if (arr[i] == -1):
            arr[i] = 6
            arr.append(8)

populations = [len(fish)]
for i in range(80):
    day(fish)
    populations.append(len(fish))


print(populations)