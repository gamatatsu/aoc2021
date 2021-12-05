from numpy import loadtxt

list = loadtxt("input/day2", delimiter="\n", unpack=False, dtype="str")

# Part 1
horizontal = 0
depth = 0
for instruction in list:
    direction, num = instruction.split(sep=" ")
    num = int(num)
    if direction == "forward":
        horizontal += num
    if direction == "up":
        depth -= num
    elif direction == "down":
        depth += num

print(horizontal * depth)

# Part 2
horizontal = 0
depth = 0
aim = 0
for instruction in list:
    direction, num = instruction.split(sep=" ")
    num = int(num)
    if direction == "forward":
        horizontal += num
        depth += num * aim
    if direction == "up":
        aim -= num
    elif direction == "down":
        aim += num

print(horizontal * depth)

