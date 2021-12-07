import numpy as np

with open('input/day6') as f:
    lines = f.readlines()

fish = str.split(lines[0], ',')
fish = [int(i) for i in fish]

repDayslist = [0 for i in range(0, 7)]

for i in range(0, len(fish)):
    repDayslist[fish[i]] += 1

repDays = np.array(repDayslist)  # fish that will spawn next cycle
newrepDays = np.array([0 for i in range(0, 9)])
fishNum = len(fish)

for i in range(0, 256):
    newFish = repDays[i % 7] + newrepDays[i % 9]
    fishNum += newFish
    repDays[i % 7] += newrepDays[i % 9]
    newrepDays[i % 9] = 0
    newrepDays[i % 9] = newFish
    remove = 0
    for i in range(remove):
        fish.remove(-1)


print(fishNum)