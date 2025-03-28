# 파이썬 타입
# bool타입
# int타입 정수
# float타입 실수
# str타입 문자열 "" 안에 입력

# bool타입 - True, False

# if True:
#     print("참입니다.")
    
# if False:
#     print("거짓입니다.")



# list 타입
# list_a = [1,2,3,4]
# list_b = [소,쥐,닭,돼지]
# list_c = [간,폐,콩팥]

# print(list_a[0]+list_a[1])

# x = input("데이터를 입력하세요. : ")
# print("입력 데이터 : ", x)

## 두 수를 입력받아 합계, 평균을 출력하시오

# a = int(input("숫자를 입력하세요. : "))
# b = int(input("숫자를 입력하세요. : "))
# print(a+b)

# 조건문

# a = int(input("점수를 입력하세요. : "))
# if a>=70:
#     print("합격")
# elif a>=60:
#     print("재시험")
# else:
#     print("불합격")

a= int(input("점수를 입력하세요. : "))
#90점 이상 A,B,C,D,F 출력하시오

if a>=90:
    print("A")
elif a>=80: print("B")
elif a>=70: print("C")
elif a>=60: print("D")
else: print("F")