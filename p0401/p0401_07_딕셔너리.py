#딕셔너리 추가
dic = {}
dic['no'] = 1
dic['name'] = '홍길동'
dic['kor'] = 100
print(dic)

#-------------------
# 딕셔너리 삭제

del dic['no']
print(dic)

#--------------
# 3. 딕셔너리 수정
dic['name'] = '이순신'

#=============
#4. 딕셔너리 출력
print(dic)
# print(dic['total']) #없는 키값을 입력시 에러
print(dic.get('total')) # 이와같이 입력시 값이 없다면 None


print(dic.keys()) # 키값들을 리스트로 출력
print(dic.values()) # value 값들만 리스트로 출력
print(dic.items()) # 튜플 형태로 출력 ('name', '이순신') - 이와 같은 형태를 튜플 형태라고 함



#----------------------
# 전체 출력 - 키, 값 모두 출력
for i,value in enumerate(dic):
    print(f"{i} : {value}")

# 키를 돌려줌.
for key in dic:
    print(key)
    print(dic[key])
    
    
# 존재하는지 확인
if 'name' in dic:
    print("키값이 존재함")

if 'no' in dic:
    print(f"no : {dic['no']}")
else:
    print("no키가 존재하지않음")





# # 딕셔너리 생성
# dic1 = {1:"a",2:"b",3:"c"}
# print(dic1)

# students_list = [1,"홍길동",100]
# students = {"no":1,"name":"홍길동","kor":100}
# print(students)

# stu = {"학번":1000,"이름":"홍길동","학과":"컴퓨터학과"}
# print(stu)






# 리스트 자리수 출력
# number = [273,103,5,32,65,9,72,800,99]

# # 자리수 : 3 값 273
# # 자리수 : 3 값 103
# # 자리수 : 1 값 5

# for n in number:
#     value = n
#     length = len(str(n))
#     print(f"자리수 {length} : {value}")





# 100 이상의 숫자만 출력하시오.
# 그리고 그 합을 구하시오.
# sum = 0
# list = []
# for i in number:
#     if i>=100:
#         list.append(i)
#         sum = sum + i
#     else:
#         pass
# print("100이상의 값들", list)
# print("100 이상 값들의 합",sum)


