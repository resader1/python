# 입력한 숫자를 5번 반복해서 리스트에 추가하는 프로그램 구현
num_list = []
# 입력한 숫자
# for a in range(5):
    
#     num = int(input("숫자를 입력하세요. : "))
#     if num not in num_list:
#         num_list.append(num)

# print(num_list)


i = 0
while i<5:
    num = int(input("{}번째 숫자를 입력하세요. : ".format(i+1)))
    if num not in num_list:
        num_list.append(num)
        i += 1
    else:
        print("중복된 숫자")
    
print(num_list)


# input_list - [1,5,10,9,8,20]

# a = 5
# if a in input_list:
#     print("{}가 존재합니다.".format(a))
# else:
#     print("{}가 존재하지 않습니다".format(a))






# i = 0
# while i<10:
#     print(i)
#     i += 1 # 1씩 증가
# print("-"*50)
# #---위와 아래는 같음---
# print("-"*50)
# for j in range(10):
#     print(j)
    
    
# 반복문 while - 조건이 맞으면 무한 반복 가능
# 반복문 for - 횟수 만큼 반복