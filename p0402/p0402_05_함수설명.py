def cal(*a,b=10): # 가변매개변수, 키워드 매개 변수 함께 사용 - 매개변수 키워드
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,3,4,5))



# # 키워드 매개변수
# def cal(b,a=10): # 키워드 변수는 뒤쪽에 있어야 함.
#     return a+b


# print(cal(1))



# # print()함수는 매개변수가 가변매개변수임.
# print(1,2,3,4,5)
# print(1,2)



# # 가변매개변수 사용
# def cal (*num): # 전개연산자
#     result = 0
#     for n in num:
#         result += n
#     return result

# print("2개 합계 : ",cal(1,2))
# print('3개 합계 : ',cal(10,20,30))
# print("4개 합계 : ",cal(20,40,60,80))



# def cal(n1,n2):
#     return n1+n2

# def cal2(n1,n2,n3):
#     return n1+n2+n3


# n1 = 10
# n2 = 20
# n3 = 30
# result = cal(n1,n2)
# print(result)

# result2 = cal2(n1,n2,n3)
# print(result2)




# # global 변수 : 전역변수
# def func1():
#     global a # 전역 변수 호출 - 글로벌은 하나밖에 못 보낸데.
#     a = 20


# a = 10
# print("a : ", a)
# func1()
# print("a : ", a)



# s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}



# def cal(ss):
#     ss['kor'] = int(input("수정할 국어점수 입력"))
#     ss['total'] = ss['kor']+ss['eng']+ss['math']
#     ss['avg'] = ss['total']/3


# # 국어 점수 변경 함수 호출
# cal(s)
# print("수정된 국어 점수 : ",s['kor'])

# s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}




# #매개변수로 일반변수 전달 형태 - 리턴으로 값을 돌려줘서 입력을 시켜야 함.
# #국어 점수 변경 함수 선언
# def cal(kor):
#     kor = int(input("수정할 국어 점수 입력 : "))
#     return kor


# kor = 100
# eng = 100
# math = 100
# # 국어 점수 변경 함수 호출
# kor = cal(kor)
# print("수정된 국어 점수 : ", kor)


# def cal(a_list):
#     a_list[0] = 100
#     a_list[1] = 200


# a_list = [0,0] #리스트타입변수 : 주소값
# a_list[0] = 10
# a_list[1] = 20
# print("함수호출 전 a_list : ",a_list[0],a_list[1])

# cal(a_list)
# print("함수 호출 후 a_list : ",a_list[0],a_list[1])

# #그룹으로 된 변수는 주소값을 지정하므로 소실되지 않음



# # 함수 선언
# def cal(a,b):
#     a = 100 # 지역 변수 - 함수 내 일반변수는 함수를 벗어나면 사라짐. - bool,int,float,str
#     b = 200


# #-----------------------------
# # 함수밖

# a = 10 # 전역변수
# b = 20
# print("함수 호출 전 a,b : ",a,b)

# # 함수 호출
# cal(a,b)
# print("함수 호출 후 a,b : ",a,b)







# # 번호, 이름, 국어, 영어, 수학, 점수를 입력받아 합계, 평균을 출력
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":99,"math":100,"total":299,"avg":100.0,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":100.0,"rank":1},
# ]



# def stu_print():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")
    
    
    

# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice = int(input("원하는 번호 입력 : "))

# if choice == 2:
#     stu_print()
# def cal(x,y,z):
#     total = x+y+z
#     avg = total/3
#     return total,avg
    



# no = 1
# name = input("이름 입력")
# kor = int(input("국어성적"))
# eng = int(input("영어성적"))
# math = int(input("수학성적"))
# total,avg = cal(kor,eng,math)

# print("{},{},{},{},{},{},{:.2f}".format(no,name,kor,eng,math,total,avg))










# 직사각형 넓이와 둘레를 구하는 프로그램을 구현.
# 넓이 = 가로*세로
# 둘레 = (가로+세로)*2

# def n(x,y):
#     print(x*y,"cm2")
#     print((x+y)*2,"cm")
    

    
# q = int(input("가로 입력"))
# w = int(input("세로 입력"))
# n(q,w)



# 입력을 5개를 받아, 짝수만 모두 더한 값을 출력하시오.
# 안됨
# def cal(n_list):
#     sum = 0
#     for x in n_list:
#         if x%2==0: sum += x
#         return sum
        

# n_list = [0]*5
# for i in range(5):
#     n_list[i] = int(input("숫자입력"))
# result = cal(n_list)



# print("짝수의 합 : ",result)



# 함수를 사용해서 두 수를 입력받아
# 10~20을 입력받으면 10+11+12+13+14........+20 값을 출력

# def add(x,y):
#     sum = 0
#     if x>y:
#         x,y = y,x
#     for i in range(x,y+1):
#         sum = sum + i
#     print("합계 : ",sum)


# n1 = int(input("숫자를 입력하세요. : "))
# n2 = int(input("숫자를 입력하세요. : "))
# # 큰 수를 먼저 넣어도 가능하게

# add(n1,n2)
# add() 결과값을 출력하시오




# 함수사용
# 1. 중복 코드가 있을 때
# 2. 소스가 너무 복잡할 때

# 먼저 프로그램을 모두 구현 한 뒤 중복되고 있는지 확인 후 함수 저장



#num1, num2, num3 값을 입력받아, 합계, 평균을 구하시오











# def pp(x,y,z):
#     return x+y+z


# x = int(input('점수를 입력하세요 : '))
# y = int(input('점수를 입력하세요 : '))
# z = int(input('점수를 입력하세요 : '))
# total = pp(x,y,z)
# avg = total/3

# print(x,y,z,total,avg)