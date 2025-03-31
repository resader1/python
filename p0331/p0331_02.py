# # 삭제 del, pop, remove, clear
# a_list = [1,2,3,4,5,6,7,8,9]
# del a_list[2] # 특정 위치값 삭제
# print(a_list)

# a_list.pop() # 맨 뒤 삭제, 특정 위치 삭제
# print(a_list)

# a_list.remove(5) # 데이터값을 삭제
# print(a_list)

# a_list.clear() # 전체 삭제
# print(a_list)


# # append, insert, extend
# a_list = [1,2,3]
# a_list.append(4) # 맨 뒤에 특정 값을 추가
# print(a_list)

# a_list.insert(1,100) # 특정 위치에 값을 추가(기존 값 손해 없음)
# print(a_list)

# a_list.extend([100,200,300]) # 뒤에 다른 리스트를 추가
# print(a_list)



#리스트 내포 a_list = [i for i in range(1,11)]

# 리스트 - append 추가하는 방법
# a_list = []
# for i in range(1,11):
#     a_list.append(i)

# print(a_list)


# # index 번호를 넣으려면 enumerate를 사용
# a_list = [273,10,5,9,100,1000,50]
# for idex,value in enumerate(a_list):
#     print(f"{idex} : {value}")