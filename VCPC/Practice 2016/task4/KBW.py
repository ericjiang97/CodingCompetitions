sizeCases = int(input('Enter size: '))

def findMaxStrength(string):
    stringArray = []
    for i in range(len(string)):
        stringArray.append(string[i])
    currentStrength = StrengthCheck(stringArray)

    i=0
    while i<len(stringArray):
        temparray = stringArray[:i]
        if(stringArray[i]=='0'):
            temparray.append('1')
        else:
            temparray.append('0')
        temparray+=stringArray[i+1:len(stringArray)]
        i+=1
        if(StrengthCheck(temparray)>currentStrength):
            currentStrength = StrengthCheck(temparray)
    return currentStrength

def StrengthCheck(array):
    total = 0
    current = array[0]
    i = 0
    counter = 0
    cur = array[i]
    for i in range(len(array)):
        if array[i] == cur:
            counter += 1
        else:
            cur = array[i]
            total += counter ** 2
            counter = 1
    total += counter ** 2
    return total


for i in range(1,sizeCases):
    stringCase = input("Enter case "+str(i)+": ")
    arrayCase = findMaxStrength(stringCase)
    print(arrayCase)


