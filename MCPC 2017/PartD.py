bound = int(input())
aliceSequence = input().split()

def myFunction(bound, sequence):
    charSet = 'abcdefghijklmnopqrstuvwxyz'

    charPos = 0
    storage = []
    done = []

    # Going Backwards
    for i in range(len(sequence)-1,-1,-1):
        currentNum = int(sequence[i])
        if(currentNum < i + 1 or currentNum in done or charPos >= 27):
            return -1
        elif(currentNum == bound + 1):
            storage.append(charSet[charPos])
            charPos += 1
            done.append(bound - currentNum)
        else:
            storage.append(storage[bound - currentNum])
            done.append(bound - currentNum)
    output = ""
    for i in range(len(storage)-1 , -1, -1):
        output += storage[i]
    return output

print(myFunction(bound, aliceSequence))