# # 1. 두 숫자를 입력받아, 합과 곱을 출력하시오.
# # a,b라는 변수에 입력받아, a,b를 출력하고 a,b의 값을 교체해서 출력하시오.

# a = input("1. 숫자를 입력하세요.")
# b = input("2. 숫자를 입력하세요.")
# a = float(a)
# b = float(b)
# print(a+b)
# print(a*b)

# # a,b = b,a
# # print(a)
# # print(b)

# c = a
# a = b
# b = c

# print("두 수 출력 :",a,b)

# a = 100
# st = "안녕"
# print("변수값 : ",a)
# print("변수값 : "+a) # 에러 = 다른 타입은 +연산자를 사용 할 수 없음.
# print("변수값 :",st)
# print("변수값 :"+st)

a = 10
b = 5
print(a,"+",b,"=",a+b)

c = 100
d = 7
# print(c,"*",d,"=",c*d)
print("%d * %d = %d" % (c,d,c*d))
print("%d / %d = %07.3f" % (c,d,c/d))