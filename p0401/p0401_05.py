students = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99,67,2],
    [3,'이순신',100,100,99,299,99,67,2]
]

count = 4     #학생 번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
while True:
    print(" "*20,end="")
    print("[학생 성적 프로그램]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("5. 학생성적 정렬")
    print("6. 학생성적 검색")
    print("7. 등수처리")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요 : "))
    
    
    if choice == 1:
        print("[학생 성적 입력]")
        no = count
        name = input("학생 이름을 입력하세요. : ")
        kor = int(input("국어 점수를 입력하세요. : "))
        eng = int(input("영어 점수를 입력하세요. : "))
        math = int(input("수학 점수를 입력하세요. : "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        students.append([no,name,kor,eng,math,total,avg,rank])
        count += 1
        print(f"{no}번 {name}학생 성적이 입력되었습니다.")
        print()
        
        
        
    elif choice == 2:
        print("[학생 성적 출력]")
        print("-"*80)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
        
        
    elif choice == 3:
        print("[학생 성적 수정]")
        name = input("수정할 학생 : ")
        temp = 0
        for i,s in enumerate(students):
            if name in s:
                temp = 1
                print(f"{name} 있음.")
                print("[점수 수정할 과목 선택]")
                print("1.국어,2.영어,3.수학")
                choice = int(input("숫자 선택"))
                if choice == 1:
                    print("국어 성적 변경")
                    num = int(input("수정입력할 점수"))
                    students[i]
                    
                
        
    elif choice == 4:
        print("[학생 성적 삭제]")
        name = input("성적을 삭제할 학생 이름 입력 : ")
        for i,s in enumerate(students):
            temp = 0
            if name in s:
                temp = 1
                choice = int(input(f"{name} 학생을 찾았습니다. 취소:0 삭제:1"))
                if choice == 1:
                    print("삭제 완")
                    del students[i]
                else:
                    print("취소")
                    break
        if temp == 0:
            print("해당 학생 없음")
    elif choice == 0:
        pass