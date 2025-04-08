# 카드 프로그램 - Card객체사용
shape = ["Spade","Heart","Diamond","Clover"]
num = [i+1 for i in range(13)]

c_list = [{}]

for i in range(4):
    for j in range(13):
        c_list = {shape[i]:num[j]}
        
print(c_list)

a_dict = {"no":1,"name":"홍길동"}
a_dict['name'] = "홍길동"

class Card:
    # shape
    # self.number
    #__str__
    shape = ["Spade","Heart","Diamond","Clover"]
    num = [i for i in range(13)]
    
    
    
    
class CardFunc:
    # 함수
    pass# 카드 셔플 함수

# cardMain.py
# 카드리스트객체 호출
# 카드객체 호출 52장
# 각각 5장을 나눠준 다음, 비교해서 큰 수가 승리하는 형태로 구현
