import random



# 랜덤 1-45번 까지의 숫자 6개 ran_list 저장
# 입력받은 숫자 6개를 my_list 저장 시키는 프로그램을 구현하세요.
# 랜덤번호 :
# 입력번호 :
# 당첨갯수 :
# 당첨번호 : 


my_list = []
ran_list = random.sample(range(1,46),6)
lotto_count = 0 # 당첨갯수
lotto_list = [] # 당첨번호
i = 0
while i<6:
    print("랜덤번호 : ",ran_list)
    a = int(input("숫자를 입력하세요 : "))
    if a>45:
        print("45 이하의 수를 입력하세요. 입력한 숫자 {}".format(a))
    elif a not in my_list:
        my_list.append(a)
        i += 1
        if a in my_list and a in ran_list:
            lotto_list.append(a)
            lotto_count += 1
    else:
        print("중복된 숫자 {}".format(a))
        
#당첨 비교(2중 for) ran_list, my_list

# for j in range(6):
#     for k in range(6):
#         if ran_list[j] == my_list[k]:
#             lotto_count = lotto_count + 1
#             lotto_list.append(my_list[k])
#             break
for j in range(6):
    for k in range(6):
        if ran_list[j] == my_list[k]:
            lotto_count = lotto_count + 1
            lotto_list.append(my_list[k])
            break
        

print("랜덤번호 : ",ran_list)
print("입력번호 : ",my_list)
print("당첨갯수 : {}".format(lotto_count))
print("당첨번호 : {}".format(lotto_list))


#반복을 해서, ran_list 10개를 입력시키는 프로그램을 구현하시오
# 단, 같은 숫자가 들어가지 않도록 하시오.
# ran_list = []
# i = 0
# n = 1
# while i<10:
#     a = random.randint(1,10)
#     if a not in ran_list:
#         ran_list.append(a)
#         i += 1
#     else:
#         print("{}번째 중복, 중복된 숫자 {}".format(n,a))
#         n += 1
        
# print(ran_list)