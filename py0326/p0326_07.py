# a = 100
# b = 50

# b = 100, a = 50 값을 교체

# 두 변수의 값을 교체하려면, 추가적인 변수 c를 하나 두고 값을 보관해서 교체
# c = a
# a = b
# b = c

# print(b)


# a = 100
# b = 50

# a,b = b,a # 파이썬 a,b의 변수값 교체방법

# print(a)

# 입력 : input
# 출력 : print


# 변수() 있으면 함수 - 어떠한 기능 구현을 말함.
# print()

# 입력 - 무조건, 문자열(str)타입
# 타입 변경 - 정수로 변경 - int(), 실수로 변경 - float(), 문자열로 변경 - str()
a = input("1. 숫자를 입력하세요.")
b = input("2. 숫자를 입력하세요.")
a = float(a)
b = float(b)
print(a)
print(b)
print(a,b)
print(type(a)) # str - 문자열
print(type(b))
print(a+b)