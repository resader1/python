# 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨 번호 확인
# 출력

my_lotto = [0]*6
win_lotto = []
lotto = [i+1 for i in range(45)]
lotto2 = [i+1 for i in range(45)]


def lotto_mix():
    global lotto,lotto2
    random.shuffle(lotto)
    lotto2 = [i+1 for i in range(45)]



lotto_mix()
while True:
    print()
    print("[  로또 프로그램  ]")
    print("-"*30)
    print('1. 로또 프로그램 재실행')
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨 확인")
    print("4. 로또 리스트 모두 확인")
    print("5. 내가 입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요. : "))
    
    if choice == 1:
        lotto_mix()
    if choice == 2:
        count = 0
        while True:
            print("[ 로또 번호 입력 ]")
            print("-"*50)
            for i in range(45):
                if i%7 != 0:
                    print(lotto2[i],end="\t")
                    
                else:
                    print()
                    print(lotto2[i],end="\t")
            print()
            choice = int(input("숫자 입력(0 입력시 이전화면) : "))
            if choice == 0: break
            elif 0>choice or choice>45:
                print("1~45 숫자를 입력.")
                continue
            temp = 0
            for i in lotto2:
                if i == choice:
                    lotto2[choice-1] = "X"
                    my_lotto[count] = choice
                    count += 1
                    temp = 1
            if temp == 0:
                print(f"{choice}는 이미 입력한 번호")
                
            if count == 6:
                print("입력한 번호",my_lotto)
                break
            
    if choice == 3:
        print("[ 로또번호 당첨 확인 ]")
        for i in lotto[:6]:
            for j in my_lotto:
                if i == j:
                    win_lotto.append(i)
                    
        print("로또 당첨 번호", lotto[:6])
        print("내 로또 번호",my_lotto)
        print("당첨된 숫자",win_lotto)
        print("당첨 개수",len(win_lotto))
    if choice == 4:
        print("[ 로또 리스트 모두 확인]")
        print(lotto)
    if choice == 5:
        print(my_lotto)
    if choice == 0:
        print("프로그램 종료")
        break
                
            
