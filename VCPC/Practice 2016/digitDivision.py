def FindPartitions(string, divisor, total, startIndex):
    if startIndex <= 0:
        return total + 1
    currentTotal = 0
    for index in range(startIndex, 0, -1):
        if int(string[index - 1:startIndex]) % divisor == 0:
            currentTotal += FindPartitions(string, divisor, total, index - 1)
    return currentTotal + total

ln1 = input("Line 1: ").split()
ln2 = input("Line 2: ")
string = ln2
divisor = int(ln1[1])
print(FindPartitions(string, divisor, 0, int(ln1[0])))