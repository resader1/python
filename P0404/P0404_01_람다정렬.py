# def add(a,b):
#     return a+b

# print(add(10,20))
# def func(a,b,c):
#     return max(a,b,c)  ## max - 값들 중 가장 큰 수

# print(max(10,5,20,100))





students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":95,"eng":95,"math":95,"total":285,"avg":95,"rank":2},
    {"no":3,"name":"이순신","kor":90,"eng":90,"math":90,"total":270,"avg":90,"rank":3},
]

# sorted - 기존의 리스트는 유지, 새로운 리스트 생성
s_list = sorted(students,key=lambda x:x['name'])
print(s_list)
print("-"*60)
print(students)

# sort() 기존의 리스트의 값을 변경시킴.
# 합계 정렬방법
print(students)
students.sort(key=lambda x:x['total'])
print(students)
students.sort(key=lambda x:x['total'],reverse=True)
print(students)

# dict타입은 sort() 함수를 사용할 수 없음.
print(students)
students.sort(key=lambda x:x['name'])
print(students)
students.sort(key=lambda x:x['name'],reverse=True)



# # 리스트 sort() 정렬됨
# a_list = [20,50,10,40,90]
# a_list.sort()
# print(a_list)
# a_list.sort(reverse=True)
# print(a_list)


# 람다식 lambda -> 함수 축약형
# def 함수명(매개변수) : return 값




#람다식
# lambda a:a*20
# 매개변수 : 리턴값
# map() 함수 : 리스트에 함수를 적용해서 다시 리스트로 반환.

# filter() 함수 : 리스트에 함수를 적용해서 조건에 맞는 것만 다시 리스트로 반환

# filter함수 관련
# a_list = [1,2,3,4,5]
# aa_list = []
# for i in a_list:
#     if i%2 == 0:
#         aa_list.append(i)
# print(aa_list)

# # filter() 함수 사용
# def func(x):
#     if x%2 == 0:
#         return x

# b_list = list(filter(func,a_list))
# print(b_list)


# c_list = list(filter(lambda x:x%2==0,a_list))
# print(c_list)

# map 함수 관련
a_list = [1,2,3,4,5] # llist 모든 값에 제곱을 해서 리스트를 생성
aa_list = []

def func(x):
    return x**2

for i in a_list:
    aa_list.append(i**2)
# map(함수,리스트)

print(list(map(func,a_list)))

# 람다식 - map() 함수를 almbda로 사용하면 코드를 줄일 수 있음
print(list(map(lambda x:x**2,a_list)))