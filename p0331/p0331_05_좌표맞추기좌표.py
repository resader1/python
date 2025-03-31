# 5*5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
import random
#1차원 리스트 생성
#1차원 리스트 랜덤으로 섞기
#2차원 리스트 생성
#2차원 리스트에 1차원 랜덤번호를 넣기

#1차원 리스트 생성 후 랜덤 섞기
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

# 2차원 리스트 생성 후 1차원 리스트 값(셔플된 값)을 넣기
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j] #0,1,2,3...24
        
# 2차원 출력
print("             [좌표 맞추기 프로그램]   ")
print("-"*45)
while True:
    print("*   |",end="\t")
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i}   |",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()
        
    # x = int(input("x 좌표. : "))
    # if x<0 or x>4:
    #     print("숫자 다시")
    #     continue
    # y = int(input("y 좌표. : "))
    # if y<0 or y>4:
    #     print("숫자 다시")
    #     continue
    # a_list[y][x] = "x"
    