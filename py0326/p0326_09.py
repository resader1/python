# 이름, 국어, 영어, 수학 입력받아 합계, 평균을 출력하시오.
# 이름 : 홍길동
# 합계 : 300
# 평균 : 100.0 소수점은 1자리까지 출력하시오.

# a = input("1. 이름을 입력하세요.")
# b = input("2. 국어 점수룰 입력하세요.")
# c = input("3. 영어 성적을 입력하세요.")
# d = input("4. 수학 성적을 입력하세요.")
# b = int(b)
# c = int(c)
# d = int(d)
# print("이름 :",a)
# print("합계 :",b+c+d)
# b = float(b)
# c = float(c)
# d = float(d)
# e = (b+c+d)/3
# print("평균 :%.1f" % e)

# a = input("이름")
# b = int(input("국어"))
# c = int(input("영어"))
# d = int(input("수학"))
# total = b+c+d
# avg = (b+c+d)/3
# print("이름 :", a)
# print("국어 :", b)
# print("영어 :", c)
# print("수학 :", d)
# print("합계 :", total)
# print("평균 : %.1f" % avg)


# 프린트 시 \n : 엔터키, \t : tab키
# print("안녕하세요.\n반갑습니다.\t저는 홍길동이라고 합니다.")

# format() 문자형태 지정
a = 10
b = 3
print("%d / %d = %.2f" % (a,b,a/b))
str_print = ("{} / {} = {:.2f}".format(a,b,a/b))
# f함수 = format()
str_print2 = f"{a} / {b} = {a/b:.2f}"
print(str_print)
print(str_print2)