string = 'hello'
stringArray = []

for i in range(len(string)):
    stringArray.append(string[i])

def genreatePerms(possible, array,listofsolutions):
    if(len(possible)==len(array)):
        listofsolutions.append(possible.copy())
    else:
        for i in range(len(array)):
            possible.a


