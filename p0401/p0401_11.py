students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":99,"math":100,"total":299,"avg":100.0,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":100.0,"rank":1},
]

count = 4 # 학생 번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print("[학생성적프로그램]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("0. 프로그램종료")
    choice = input("번호 입력")
    if choice == 1:
            print("학생성적입력")
            no = count
            name = input("이름 입력/0입력시 프로그램 종료")
            if name == 0:
                break
            kor = int(input("국어성적입력"))
            eng = int(input("국어성적입력"))
            math = int(input("국어성적입력"))
            total = kor+eng+math
            avg = total/3
            rank = 0
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            
    elif choice == 2:
        pass
    elif choice == 0:
        print("프로그램 종료")
        break