import random

lotto = [i for i in range(1,46)] # 로또 45자
t_lotto = []*6 # 랜덤 생성된 로또번호
my_lotto = []*6
c_lotto = []


random.shuffle(lotto)


for i in lotto: # 로또 6자리 뽑는 for 문
    t_lotto.append(i)
    if len(t_lotto) == 6:
        break
    

while True:
    print("[ 로또 맞추기 ]")
    print("1. 로또 번호 입력")
    print("2. 내 로또 번호 확인")
    print("3. 당첨 확인")
    print("4. 로또 번호 확인")
    print("0. 프로그램 종료")
    count = 0
    try:
        choice = int(input("메뉴 선택"))
    except : break

    
    if choice == 1:
        my_lotto.clear()
        print("[ 로또 번호 입력 ]")
        while True:
            i = int(input("로또 번호 선택"))
            if i<=0 or 45<i:
                print("유효하지 않은 번호 1~45 입력")
                continue
            elif 0<i<46:
                if i not in my_lotto:
                    my_lotto.append(i)
                else:
                    print(f"{i}번호는 중복됨")
                    continue
                
            if len(my_lotto) == 6:
                break
        
    elif choice == 2:
        print("내 로또 번호")
        print(my_lotto)
        
    elif choice == 3:
        for i in range(6):
            for j in range(6):
                if my_lotto[i] == t_lotto[j]:
                    c_lotto.append(my_lotto[i])
                    count += 1
        print(t_lotto)
        print(my_lotto)
        print("당첨 숫자",c_lotto)
        print("당첨 개수",len(c_lotto))
    
    elif choice == 4:
        print(t_lotto)
    
    elif choice == 0:
        break