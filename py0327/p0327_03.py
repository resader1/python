# a,b = 100,200
# c = 300; d = 400
# e = 500
# f = 600

# # #관계 연산자 - True,False
# # print(a==b)
# # print(a!=b)
# # print(a>b)
# # print(a<b)
# # print(a>=b)
# # print(a<=b)

# print((a>50) and (a>=50))

# a = int(input("숫자를 입력하세요."))

# if a < 100:
#     print("입력한 값은 100보다 작은 수 입니다.")
# else:
#     print("입력한 값은 100보다 큰 수 입니다.")
    
    
#양수, 음수인지 확인 - 0은 양수로 하겠습니다.
# a= int(input("숫자를 입력하세요. :"))

# if a >= 0:
#     print("입력한 수는 양수입니다.")
# else:
#     print("입력한 값은 음수입니다.")

# num ->짝수인지, 홀수인지 구현 num % 2 == 0

# num = int(input("숫자를 입력하세요. :"))
# if num%2==0:
#     print("입력한 수는 짝수입니다.")
# else:
#     print("입력한 수는 홀수입니다.")

a = int(input("숫자를 입력하세요. :"))
if a%3==0:
    print(a,"은(는) 3의 배수입니다.")
else:
    print(a,"은(는) 3의 배수가 아닙니다.")