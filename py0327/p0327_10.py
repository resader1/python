# 1-100까지의 랜덤 숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.
# 도전 횟수 : n
# 도전 번호 : 
# 랜덤 번호 : x

import random

list = []

x = random.randint(1,100)
n = 0

for n in range(1,11):
    a = int(input("숫자를 입력하세요 : "))
    list.append(a)
    if a == x:
        print("정답. {}".format(x))
        break
    elif a>x:
        print("작은 수를 입력.{}".format(a))
    else:
        print("큰 수를 입력.{}".format(a))
    
print("횟수.{}".format(n))
print("사용 숫자.{}".format(list))
print("랜덤번호.{}".format(x))


