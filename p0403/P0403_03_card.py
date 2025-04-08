# 카드모양 SPADE-4,DIAMOND-3,HEART-2,CLOVER-1
# # 번호 A,2,3,4,5,6,7,8,9,10,J,Q,K

# 카드 1장 - 카드 모양, 번호
# 카드 모양 4개
# 번호 13개
# 카드 총 장수 : 52

# 리스트-딕셔너리
# cList = [
#     {"shape":"SPADE","no":1},
#     {"shape":"SPADE","no":2},
# ]

import random
cList = []
cShape = ["CLOVER","HEART","DIAMOND","SPADE"]
no = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]

# 카드 생성
for i in range(52):
    cList.append({"shape":i//13,"no":i%13+1})

# 카드 랜덤으로 섞기
random.shuffle(cList)

# myCard, yourCard

# 5장을 입력
myCard = []
yourCard = []

# 카드 5장씩 배분
for i in range(5):
    myCard.append(cList[i])
    
for i in range(5,10):
    yourCard.append(cList[i])
    
# 카드 출력
print("내 카드")
for i in myCard:
    print(f"{cShape[i['shape']]},{no[i['no']]}")
    

# 상대 카드 출력
print("상대 카드")
for i in yourCard:
    print(f"{cShape[i['shape']]},{no[i['no']]}")


# 승리한 카드 출력
winCard = []
# 패배 카드 출력
looseCard = []
# 무승부 카드 출력
drawCard = []



score = [0,0,0,0,0]
for i in range(5):
    if myCard[i]['no'] > yourCard[i]['no']:
        score[i] = 2
        winCard.append(myCard[i])
    elif myCard[i]['no'] < yourCard[i]['no']:
        score[i] = 1
        looseCard.append(myCard[i])
    else:
        score[i] = 0
        drawCard.append(myCard[i])
        
print("[카드 승부 확인]")
print(f"내 승리 : {score.count(2)}, 상대 승리 : {score.count(1)} 무승부 : {score.count(0)}")


print("[ 승리 카드 ]")
for i,c in enumerate(myCard):
    if score[i] == 2:
        print(f"[  {cShape[c['shape']]}, {no[c['no']]}  ]")
    

# score = {"myWin":0,"yourWin":0,"draw":0}
# for i in range(5):
#     if myCard[i]['no'] > yourCard[i]['no']:
#         score['myWin'] += 1
#         winCard.append(myCard[i])
#     elif myCard[i]['no'] < yourCard[i]['no']:
#         score['yourWin'] += 1
#         looseCard.append(myCard[i])
#     else:
#         score["draw"] += 1
#         drawCard.append(myCard[i])
        
# print("[카드 승부 확인]")
# print(f"내 승리 : {score['myWin']}, 상대 승리 : {score['yourWin']} 무승부 : {score['draw']}")
# 승리한 카드 출력
print("승리카드")
for i in winCard:
    print(f"{cShape[i['shape']]},{no[i['no']]}")
    
# 패배 카드 출력
print("패배카드")
for i in looseCard:
    print(f"{cShape[i['shape']]},{no[i['no']]}")
# 무승부 카드 출력
print("무승부카드")
for i in drawCard:
    print(f"{cShape[i['shape']]},{no[i['no']]}")

# 11-J 12-Q 13-K 1-A




# # 전체 카드 출력
# for c in cList:
#     print(c['shape'],c['no'])




# import math
# import random

# # 0.0000000000000000 <= x < 1
# print(random.random())

# # 1-45까지 숫자 중 1개를 랜덤으로 추출.
# print(random.randint(1,45))

# #리스트에서 1개 랜덤 추출.
# a_list = [1,2,3,4,5]
# print(random.choice(a_list)) # a_list에서 하나 추출.

# #리스트에서 개수만큼 랜덤 추출. - 중복없이
# print(random.sample(a_list,2))

# #리스트를 랜덤으로 섞기
# random.shuffle(a_list)
# print(a_list)


# a = 3.141592
# b = 3.51582

# # a에서 소수점 3자리에서 올림해서 2자리까지 표시해서 출력

# print(math.ceil(a*100)/100)

# # b에서 소수점 5자리에서 ceil올림해서 4자리까지 표시해서 출력

# print(math.ceil(b*10000)/10000)


# # math 안에 있는 함수를 출력
# print(dir(math))







# # 올림
# print(math.ceil(a)) # 4
# # 반올림
# print(round(a)) # 3
# print(round(b)) # 4
# print(round(b,3)) # 소수점 3+1 자리에서 반올림
# print(round(a,4))

# # 버림
# print(math.floor(a))  # 버림
