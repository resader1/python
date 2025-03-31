import random
# 1. 순차적 리스트 생성
sample_list = [i+1 for i in range(25)]
# 2. 리스트 셔플
random.shuffle(sample_list)
# 3. 2차원 초기화 리스트 생성
a_list = [[0]*5 for i in range(5)] # 5x5리스트 0으로 초기화
# 4. 2차원 리스트에 랜덤리스트의 값을 입력
for i in range(5):
    for j in range(5):
        a_list[i][j] = sample_list[5*i+j]
        
# 5x5 리스트 출력
for i in range(5):
    for j in range(5):
        print(a_list[i][j],end="\t")
    print()


sample_list = list() # 리스트 초기화
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(0) #[0,0,0,0,0]
    sample_list.append(temp)

print(sample_list)
    
    
    
# 5x5 리스트 초기화
# list = [[0]*5]*5 #얕은 복사
# list = [[0]*5 for i in range(5)]
# for i in range(5):
#     for j in range(5):
#         list[i][j] = 5*i+(j+1)
# print(list)




# # 1-25
# import random
# list = [i+1 for i in range(25)]
# print(list)
# random.shuffle(list)
# # 랜덤으로 섞여진 리스트 출력
# print(list)









# # 1 2 3 4 5 
# # 6 7 8 9 10
# # 11 12 13 14 15
# # 16 17 18 19 20
# # 21 22 23 24 25

# aa = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
# for i in range(5):
#     for j in range(5):
#         print(aa[i][j],end="\t")
#     print()
    


# 1,2,3
# 4,5,6
# 7,8,9

# aa = [[1,2,3],[4,5,6],[7,8,9]]
# print(aa)

# for i in range(3):
#     for j in range(3):
#         print(aa[i][j],end="\t")
#     print()


# # 1차원 리스트
# aa = [10,20,30]
# print(aa[0])
# # 2차원 리스트
# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# print(aa[0][0])


# 리스트 값 변경
# a_list = [1,2,3,4,5,6,7,8,9]
# a_list[5] = 10

# a_list[1:2] = [100,200]
# print(a_list)
# 역순출력
# a_list =  [1,2,3,4,5,6,7,8,9]
# print(a_list[::-1])

# for i in range(10):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# for i in range(10):
#     if i%2 == 0:continue
#     print(i)



#continue - 그 위치에서 중지후 다시 for문 실행
#1-10까지 진행을 하는데, 1,2,3 - continue : 제외 4,5,6,7,8,9,10
#break - 반복문 완전 중지
# 1-10까지 진행을 하는데 1,2,3 - break :반복문 끝
#pass - 실행할 구문이 없음. for 문을 계속 반복
# 1-10까지 진행을 하는데, 1,2,3-pass,4,5,6,7,8,9,10 10번 실행



# 입력한 숫자의 합이 50을 넘으면 프로그램을 종료하고 총합을 구하시오.
# 입력한 숫자 중 5의 배수는 제외시킬것

# list = []
# sum = 0
# while True:
#     if sum<50:
#         num = int(input("숫자를 입력하세요. : "))
#         if num%5==0:
#             print("5의 배수는 제외 :".format(num))
#             continue
#         sum = sum + num
#     else: break
# print(sum)




# 1 - 100 까지의 숫자의 합을 구할 때 합계가 200을 넘을때 숫자를 출력하시오.

# list = [i+1 for i in range(100)]
# sum = 0
# for i in list:
#     sum = sum + i
#     if sum>200:
#         print("{} 까지의 합 : ".format(i))
#         print(sum)
#         break

# print("i 이전의 값{}, 이전까지의 합{}".format(i-1,sum-i))

# # 반복문 - for, while




# a_list = [i+1 for i in range(100)] # 1~100 숫자 리스트

# # a_list에서 홀수의 합계를 구하시오
# sum = 0
# for i in a_list:
#     if i%2 == 1:
#         sum = sum + i
        
# print(sum)




# import random

# #random.random() 함수 : 0<=x<1 사이의 랜덤실수를 가져옴.
# print(random.random()) # 0.00000000 <= x < 1.00000000
# print(int(random.random()*10)+1) # 1, 10 까지 숫자 뽑음
# print(int(random.random()*10)+0) #0, 9 가지 숫자 뽑음

# print(random.randint(1,10))

# import random

# a_list = [i+1 for i in range(45)]
# print(a_list)

# random.shuffle(a_list)

# print(a_list)

# print(a_list[:6])

# ### -------------------------------------------
# # 로또 프로그램
# # 6개 랜덤 숫자와 입력숫자 6개를 출력하시오.

# import random

# lotto = [i+1 for i in range(45)]
# l_list = random.sample(range(1,46),6)
# m_list = []
# for i in range(1,7):
#     a = int(input("숫자를 입력하세요. : "))
#     m_list.append(a)

# print(l_list)
# print(m_list)
# ##------------------------------------------

# l_list = []
# m_list = []
# for i in range(6):
#     l_list.append(random.randint(1,45))

# for i in range(6):
#     a = int(input("숫자를 입력하세요. :"))
#     m_list.append(a)


# # 10번의 숫자를 입력받아, 합계를 구하시오.
# #for문, while 문
# sum = 0
# for i in range(1,11):
#     a = int(input("숫자를 입력하세요. : "))
#     sum = sum + a
# print(sum)
    
# sum = 0
# i = 0
# while i<10:
#     a = int(input("숫자를 입력하세요. : "))
#     sum = sum + a
#     i = i + 1
    
# print(sum)



# # while 문
# i = 0
# while i<10:
#     print(i)
#     i = i+1




# #for 문
# for i in range(10): # 10번 반복
#     print(i)