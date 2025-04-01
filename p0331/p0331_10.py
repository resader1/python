#좌표...
# 5*5
import random
flist = [i+1 for i in range(25)]

random.shuffle(flist)

slist = [[0]*5 for i in range(5)]


for i in range(5):
    for j in range(5):
        slist[i][j] = flist[5*i+j]
        
        



while True:
    print("*  |",end="\t")
    print()
    for i in range(5):
        print(f"{i}  |",end="\t")
        for j in range(5):
            print(slist[i][j],end="\t")
        print()

    x = int(input("x값 : "))
    y = int(input("y값 : "))
    slist[y][x] = "x"