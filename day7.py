import numpy as np
from numpy import loadtxt

crab = loadtxt('input/day7', delimiter=',', dtype=int)
print(crab)

leastFuel = -1
leastPosition = -1
for position in range(0, np.max(crab)):
    fuel = 0
    for i in crab:
        fuel += abs(i - position)
    if fuel < leastFuel or position == 0:
        leastFuel = fuel
        leastPosition = position

print(leastFuel)
print(leastPosition)


# part 2
print('part 2')
leastFuel = -1
leastPosition = -1
for position in range(0, np.max(crab)):
    fuel = 0
    for i in range(0, len(crab)):
        fuel += sum([j for j in range(1, abs(crab[i] - position) + 1)])
    if fuel < leastFuel or position == 0:
        leastFuel = fuel
        leastPosition = position

print(leastFuel)
print(leastPosition)
