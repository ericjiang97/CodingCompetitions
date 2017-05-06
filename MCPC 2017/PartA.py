scores = input().split()
darcyScore = int(scores[0])
rajkoScore = int(scores[1])

sDeter = (darcyScore + rajkoScore) % 10
if(sDeter >=0 and sDeter < 4):
    print("Darcy")
else:
    print("Rajko")