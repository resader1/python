# 숫자 맞추기 프로그램
import random

# 1-45 사이의 숫자 1개를 가져옴
lotto = random.randint(1,45)

input_list = [] # 입력한 숫자 저장 리스트
# ----
for i in range(10):
    input1 = int(input("{}번째 숫자를 입력하세요. : ".format(i+1)))
    input_list.append(input1) # 리스트에 숫자 추가

    if lotto==input1:
        print("당첨")
        break
    elif lotto>input1:
        print("틀렸습니다. {}보다 더 큰 수를 입력하세요".format(input1))
    else:
        print("틀렸습니다. {}보다 더 작은 수를 입력하세요.".format(input1))

    
# ----
    
print("랜덤 번호 : {}".format(lotto))
print("입력 번호 : {}".format(input_list))