rowSize = 5
colSize = 7

def convertFile(sizeOfRows, sizeOfCols, file,array):
    temp = []
    for line in file:
        temp.append(line)
    file.close()

    for i in range(len(temp)):
        temp[i]=temp[i].strip('\n')

    length = len(temp[0]) // (sizeOfRows+1) + 1

    array = []

    for i in range(length):
        array.append([[],[],[],[],[],[],[]])

    tempCounter = 0
    for i in range(sizeOfCols):
        strCounter = 0

        for j in range(length):

            array[j][i] = temp[tempCounter][strCounter:strCounter + sizeOfRows]
            strCounter += sizeOfRows+1

        tempCounter += 1
    return array