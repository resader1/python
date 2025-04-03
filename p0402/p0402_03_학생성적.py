### 파일 - 저장해서 불러오기
### DB에서 불러오기 
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":99,"math":100,"total":299,"avg":100.0,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":100.0,"rank":1},
]

count = 4 # 학생 번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*15,end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요. : "))
    
    
    
    # 번호 선택
    
    if choice == 1:
        while True:
            print(" [ 학생 성적 입력 ]")
            no = count
            name = input(f"{no}번 학생 이름 입력/0 입력시 이전 화면 : ")
            if name == "0":
                break
            while True:
                kor = input("국어 점수 입력 : ")
                if kor.isdigit():
                    kor = int(kor)
                    if 0<=kor<=100:
                        break
                    else:
                        print("0-100의 값을 입력해야함.")
                        
            while True:
                eng = input("영어 점수 입력 : ")
                if eng.isdigit():
                    eng = int(eng)
                    if 0<=eng<=100:
                        break
                    else:
                        print("0-100의 값을 입력해야함.")
            while True:        
                math = input("수학 점수 입력 : ")
                if math.isdigit():
                    math = int(math)
                    if 0<=math<=100:
                        break
                    else:
                        print("0-100의 값을 입력해야함.")
                    
            total = kor+eng+math
            avg = total/3
            rank = 0
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            print(f"{name} 학생 성적이 등록됨")
            count += 1
            print()
    elif choice == 2:
        print(" [ 학생 성적 출력 ]")
        print("-"*80)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*80)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
            
    elif choice == 3:
        print("[ 학생 성적 수정]")
        name = input("수정할 학생 이름 입력(0:이전화면 이동) : ")
        temp = 0
        for s in students:
            if name in s['name']: # 수정할 학생 찾음.
                temp = 1          # temp 1로 변경.
                print(f"{name} 학생이 있습니다. 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print("1.국어 2.영어 3.수학")
                print("-"*30)
                choice = int(input("원하는 번호를 입력하세요. : "))
                # 수정할 과목 확인
                if choice == 1:
                    p_kor = s['kor']
                    print(f"현재 국어 점수 : {s['kor']}")
                    s['kor'] = int(input("변경 국어 점수 : "))
                    print(f"국어 점수 {p_kor}점에서 {s['kor']}점으로 변경됨")
                    #합계와 평균도 수정해야함
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total']/3
                    
                elif choice == 2:
                    p_eng = {s['eng']}
                    print(f"현재 영어 점수 : {s['eng']}")
                    s['eng'] = int(input("변경 영어 점수 : "))
                    print(f"영어 점수 {p_eng}점에서 {s['eng']}점으로 변경됨")
                    #합계와 평균도 수정해야함
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total']/3
                elif choice == 3:
                    p_math = {s['math']}
                    print(f"현재 수학 점수 : {s['math']}")
                    s['math'] = int(input("변경 수학 점수 : "))
                    print(f"수학 점수 {p_math}점에서 {s['math']}점으로 변경됨")
                    #합계와 평균도 수정해야함
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total']/3
                
            # 수정할 학생 못찾음
        if temp == 0:
            print("수정할 학생 찾지 못함.")
            
            
                

        
    elif choice == 0:
        print(" [ 프로그램 종료 ]")
        break