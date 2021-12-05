from numpy import loadtxt
list = loadtxt("input/day1", delimiter="\n", unpack=False, dtype=int)

# Part 1
count = 0

for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        count += 1

print(count)

# Part 2
temp = 0
countWindow = 0
for i in range(0, len(list) - 2):
    window = list[i] + list[i + 1] + list[i + 2]
    if window > temp:
        countWindow += 1
    temp = window

print(countWindow - 1)
