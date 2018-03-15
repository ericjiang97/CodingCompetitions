# ascii.txt
# xxxxx ....x xxxxx xxxxx x...x xxxxx xxxxx xxxxx xxxxx xxxxx .....
# x...x ....x ....x ....x x...x x.... x.... ....x x...x x...x ..x..
# x...x ....x ....x ....x x...x x.... x.... ....x x...x x...x ..x..
# x...x ....x xxxxx xxxxx xxxxx xxxxx xxxxx ....x xxxxx xxxxx xxxxx
# x...x ....x x.... ....x ....x ....x x...x ....x x...x ....x ..x..
# x...x ....x x.... ....x ....x ....x x...x ....x x...x ....x ..x..
# xxxxx ....x xxxxx xxxxx ....x xxxxx xxxxx ....x xxxxx xxxxx .....


# input.txt
# ....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx
# ....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
# ....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
# ....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x
# ....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
# ....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
# ....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx

Ascii = open('ascii.txt')
asciiArray = []

def convertFile(file,array):
    temp = []
    for line in file:
        temp.append(line)
    file.close()
    for i in range(len(temp)):
        temp[i]=temp[i].strip('\n')
    length = len(temp[0]) // 6 + 1
    array = []
    for i in range(length):
        array.append([[],[],[],[],[],[],[]])
    tempCounter = 0
    for i in range(7):
        strCounter = 0
        for j in range(length):
            array[j][i] = temp[tempCounter][strCounter:strCounter + 5]
            strCounter += 6
        tempCounter += 1
    return array

asciitable = convertFile(Ascii,asciiArray)


file = open('input.txt')
temp = []

for line in file:
    temp.append(line)

file.close()

for i in range(len(temp)):
    temp[i]=temp[i].strip('\n')

length = len(temp[0]) // 6 + 1

array = []

for i in range(length):
    array.append([[],[],[],[],[],[],[]])

tempCounter = 0
for i in range(7):
    strCounter = 0

    for j in range(length):

        array[j][i] = temp[tempCounter][strCounter:strCounter + 5]
        strCounter += 6

    tempCounter += 1

a = ''
b = ''


addTo = 0
for i in range(length):
    current = []
    for j in range(7):
        current.append(array[i][j])

    if current == asciitable[0]:
        if addTo == 0:
            a = a + '0'

        else:
            b = b + '0'

    elif current == asciitable[1]:
        if addTo == 0:
            a = a + '1'

        else:
            b = b + '1'

    elif current == asciitable[2]:
        if addTo == 0:
            a = a + '2'

        else:
            b = b + '2'

    elif current == asciitable[3]:
        if addTo == 0:
            a = a + '3'

        else:
            b = b + '3'

    elif current == asciitable[4]:
        if addTo == 0:
            a = a + '4'

        else:
            b = b + '4'

    elif current == asciitable[5]:
        if addTo == 0:
            a = a + '5'

        else:
            b = b + '5'

    elif current == asciitable[6]:
        if addTo == 0:
            a = a + '6'

        else:
            b = b + '6'

    elif current == asciitable[7]:
        if addTo == 0:
            a = a + '7'

        else:
            b = b + '7'

    elif current == asciitable[8]:
        if addTo == 0:
            a = a + '8'

        else:
            b = b + '8'

    elif current == asciitable[9]:
        if addTo == 0:
            a = a + '9'

        else:
            b = b + '9'

    else:
        addTo = 1


print(str(int(a)+int(b)))









