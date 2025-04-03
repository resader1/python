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
# 함수 사용
# - 1. 중복된 코드의 재사용
# - 2. 소스의 가독성 증대

# 학생점수 수정 함수 선언
def stu_sub():
    print(" [ 학생 성적 수정 ]")
    name = input("수정하려고 하는 학생 이름을 입력하세요. : ")
    temp = 0 # 찾지 못했을 경우 
    for s in students:
        if s['name'] == name:
            temp = 1
            print(f"{name}학생을 찾음. 수정할 과목 선택.")
            print(" [ 수정 과목 선택 ]")
            print("1.국어, 2.영어, 3.수학")
            print("-"*50)
            choice = int(input("원하는 번호를 입력. : "))
            sub_list = ['','kor','eng','math']
            if choice == 1:
                p_score = s[sub_list[choice]]
                print(f"현재 {title[choice+1]}점수 : {p_score}")
                s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수 입력. : "))
                print(f"변경 전 : {p_score} 변경 후 : {s[sub_list[choice]]}")
                s['total'] = s['kor'] + s['eng'] + s['math']
                s['avg'] = s['total']/3
            elif choice == 2:
                p_score = s[sub_list[choice]]
                print(f"현재 {title[choice+1]}점수 : {p_score}")
                s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수 입력. : "))
                print(f"변경 전 : {p_score} 변경 후 : {s[sub_list[choice]]}")
                s['total'] = s['kor'] + s['eng'] + s['math']
                s['avg'] = s['total']/3
            elif choice == 3:
                p_score = s[sub_list[choice]]
                print(f"현재 {title[choice+1]}점수 : {p_score}")
                s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수 입력. : "))
                print(f"변경 전 : {p_score} 변경 후 : {s[sub_list[choice]]}")
                s['total'] = s['kor'] + s['eng'] + s['math']
                s['avg'] = s['total']/3
                
    if temp == 0:
        print(f"{name} 학생 없음. 다시 입력")
        print()


while True:
    choice = stu_func.stu_print()
    
    if choice == 1:
        #학생성적입력부분
            count = stu_func.stu_input(count,students)
    
    elif choice == 2:
        stu_func.stu_output(title,students)
        
    elif choice == 3: # 학생성적수정부분
        stu_sub()
    elif choice == 4: # 등수처리
        stu_func.stu_rank(students)
    elif choice == 0:
        print("[프로그램 종료]")
        break