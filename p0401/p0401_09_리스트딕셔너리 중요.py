


# # zip() -> 2개의 리스트를 합치는 것 -> list 타입, dict 타입으로 변경 가능
# n_list = ['홍길동','유관순','이순신','강감찬','김구']
# t_list = [100,99,89,79,100]
# # tuple_list = list(zip(n_list,t_list))

# print(list(zip(n_list,t_list))) # list 타입/튜플형태

# print(dict(zip(n_list,t_list))) # 딕셔너리 타입



# students = {"no":1,"name":"홍길동","kor":100}
# for key,v in students.items():
#     print(f"{key} : {v}")
    


# # 2개의 리스트를 출력할 수 있음
# n_list = ['홍길동','유관순','이순신','강감찬','김구']
# t_list = [100,99,89,79,100]
# for n,t in zip(n_list,t_list):
#     print(f"{n} : {t}")
    




# # 리스트 내포 : if 조건절을 넣을 수 있음.
# n_list = [i for i in range(1,51) if i%3==0]
# print(n_list)





# list = [1,2,3,4,5]
# # list2 = ['10,100','10,200','10,300','10,400','10,500']
# # format 천단위 표시
# list2 = ["{:,d}".format((i+100)*100) for i in list]

# print(list2)


#------------------------------
# # set -> 중복을 제거해서 키를 확인
# myset1 = {1,2,2,3,3,3,5,5,7}
# print(myset1)

# menu_list = ['삼각김밥','바나나','삼각김밥','사과','바나나','도시락','삼각김밥']

# print(set(menu_list)) # list타입을 set타입으로 변경해서 확인