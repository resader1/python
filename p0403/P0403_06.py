import stu_func
# import stu_fonc as stu    # 별칭 사용 방법    ------- 이제부터 stu_func 를 stu라고만 지칭 가능
# from stu_func import *    ### 모든 함수 다 가져옴
# from stu_func import stu_print,stu_input,stu_output


students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":95,"eng":95,"math":95,"total":285,"avg":95,"rank":2},
    {"no":3,"name":"이순신","kor":90,"eng":90,"math":90,"total":270,"avg":90,"rank":3},
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print("[ 학생 성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("0. 프로그램 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요. : "))

    if choice == 1:
        print("[ 학생 성적 입력]")
        
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 0:
        print("프로그램 종료")
        break