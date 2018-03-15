def permBarrier(length, array):
    for i in range(length):
        permString = ''
        for j in range(length - i):
            permString = permString + '1'

        permString = permString.ljust(length, '0')
        array.append(permString)

array = []
permBarrier(4, array)
print(array)

arrayperms = []

for i in range(len(array)):
    arrayperms.append(set("".join(string) for string in permutations(array[i])))