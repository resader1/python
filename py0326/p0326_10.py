# 숫자 두 개를 입력받아, 사칙연산 결과값을 출력하시오.

# 국어, 영어, 수학 점수를 입력받아 평균을 출력하시오.
# 합계 : 240
# 평균 : 80.00

a = int(input("숫자를 입력하세요. :"))
b = int(input("숫자를 입력하세요. :"))
str_print = ("{} + {} = {}".format(a,b,a+b))
str_print2 = ("{} - {} = {}".format(a,b,a-b))
str_print3 = ("{} * {} = {}".format(a,b,a*b))
str_print4 = ("{} / {} = {:.2}".format(a,b,a/b))
print(str_print)
print(str_print2)
print(str_print3)
print(str_print4)

a = int(input("국어 점수를 입력하세요. :"))
b = int(input("영어 점수를 입력하세요. :"))
c = int(input("수학 점수를 입력하세요. :"))
# total = f"{a} + {b} + {c}"
# avg = ("{} + {} + {} = {:.2f}".format(a,b,c,(a+b+c)/3))
# print("합계 :", (total))
# print("평균 :", (avg))

total = a + b + c
print("합계 :",total)
t = int(total)
print("평균 : {:.2f}".format(t/3))