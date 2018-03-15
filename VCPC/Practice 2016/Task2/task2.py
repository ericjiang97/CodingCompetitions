from itertools import permutations
def permBarrier(length, array):
    for i in range(length):
        permString = ''
        for j in range(length - i):
            permString = permString + '1'

        permString = permString.ljust(length, '0')
        array.append(permString)


ln1 = input("Line 1: ")
ln2 = input("Line 2: ")


temp = ln1.split()
length = int(temp[0])
divisor = int(temp[1])
numstring = ln2

permArray = []
permBarrier(length - 1, permArray)

permArray2 = []

for i in range(len(permArray)):
    permArray2.append(set("".join(string) for string in permutations(permArray[i])))

stringArray = []
counter = 0
for i in range(len(permArray2)):
    while len(permArray2[i]) > 0:
        stringArray.append(permArray2[i].pop())

numberArray = []

for i in range(len(stringArray)):
    tempArray = []
    num = numstring[0]
    for j in range(length - 1):
        cur = stringArray[i][j]

        if cur == '0':
            num = num + numstring[j + 1]

        else:
            tempArray.append(num)
            num = numstring[j + 1]

    tempArray.append(num)
    numberArray.append(tempArray)
    
counter = 0

for i in range(len(numberArray)):
    flag = 0
    for j in range(len(numberArray[i])):
        if int(numberArray[i][j]) % divisor != 0:
            flag = 1

    if flag == 0:
        counter += 1

if int(numstring) % divisor == 0:
    counter += 1
    
print(counter)
