#1차원 리스트
import random

list = [i for i in range(1,26)]
random.shuffle(list)
# random.random(), random.randint(), random.sample(), random.shuffle()

# 2차원 리스트


mlist = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        mlist[i][j] = list[5*i+j]

#화면출력

while True:
    print(" "*5,end="")
    print("        [좌표맞추기 프로그램]")
    print("-"*50)
    print("*   |",end="\t")
    for i in range(5):
        print(i,end="\t")
    print()
    print("-"*50)
    for i in range(5):
        print(i,"  |",end="\t")
        for j in range(5):
            print(mlist[i][j],end="\t")
        print()
        
    print("-"*50)
    # 좌표입력
    # x = int(input("x좌표를 입력하세요. : "))
    # y = int(input("y좌표를 입력하세요. : "))

    # mlist[y][x] = "x"
    
    # 숫자입력
    num = int(input("숫자(1-25) : "))
    for i in range(5):
        for j in range(5):
            if mlist[i][j] == num:
                mlist[i][j] = "x"
            elif 1>num or num>25:
                print("1-25라고")