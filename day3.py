from numpy import loadtxt
input = loadtxt("input/day3", delimiter="\n", unpack=False, dtype='str')

# Part 1
def splitDigits(arr):
    occurances = []
    for i in range(0, len(arr[0])):
        occurances.append([])

    for i in range(0, len(arr)):
        for k in range(0, len(occurances)):
            occurances[k].append(arr[i][k])
    return occurances


def gamma(arr):
    output = ''
    for i in arr:
        if i.count(str(0)) < i.count(str(1)):
            output += '1'
        else:
            output += '0'
    return output


def invert(binaryList):
    new = []
    for i in range(0, len(binaryList)):
        if binaryList[i] == str(0):
            new.append(str(1))
        else:
            new.append(str(0))
    return ''.join(binaryList), ''.join(new)

gamma = gamma(splitDigits(input))
gamma, epsilon = invert(gamma)
print(int(gamma, 2) * int(epsilon, 2))

# Part 2
part2 = list(input)
oxygen = list(input)
co2 = list(input)

print(oxygen)

def gcd(arr, digit, gl):
    arrSplit = splitDigits(arr)
    for i in range(0, len(arr)):
        if gl == 'g':
            if arrSplit[digit].count(str(0)) > arrSplit[digit].count(str(1)):
                return str(0)
            else:
                return str(1)
        else:
            if arrSplit[digit].count(str(0)) <= arrSplit[digit].count(str(1)):
                return str(0)
            else:
                return str(1)


def remove(arr: list, starting, digit):
    delete = []
    for i in range(0, len(arr)):
        if arr[i][digit] != str(starting):
            delete.append(arr[i])
    for i in delete:
        arr.remove(i)


index = 0
while len(oxygen) > 1:
    remove(oxygen, gcd(oxygen, index, 'g'), index)
    print(oxygen)
    index += 1

index = 0
while len(co2) > 1:
    remove(co2, gcd(co2, index, 'l'), index)
    print(co2)
    index += 1

print(int(oxygen[0], 2) * int(co2[0], 2))


