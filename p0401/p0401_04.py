students = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99,67,2],
    [3,'이순신',100,100,99,299,99,67,2]
]

count = 4 #학생 번호를 생성
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
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요.(0.이전화면 이동) : ")
        # 이전화면 이동 로직 구현
        kor = int(input("국어 점수를 입력하세요. : "))
        eng = int(input("영어 점수를 입력하세요. : "))
        math = int(input("수학 점수를 입력하세요. : "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        students.append([no,name,kor,eng,math,total,avg,rank])
        count = count + 1
        print(f"{no}번 {name} 학생 성적이 등록되었습니다.")
        print()
    
    elif choice == 2:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
                print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))
    
    
    elif choice == 3:
        print("[ 학생성적 수정]")
        name = input("수정하려는 학생 이름을 입력하세요. : ")
        temp = 0 # 찾지 못했을 경우 사용하기 위해 쓰는 변수
        for i,s in enumerate(students):
            if name in s: #있을 경우
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                print()
                print("[ 수정하려는 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                print("-"*20)
                choice = int(input("원하는 번호를 입력하세요. : "))
                if choice == 1:
                    print("[ 국어 성적 수정 ]")
                    print(f"현재 국어점수 : {s[2]}")
                    s[2] = int(input("변경 국어 점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name}학생 성적이 수정되었습니다.")
                elif choice == 2:
                    print("[영어 성적 수정]")
                    print(f"현재 영어점수 : {s[3]}")
                    s[3] = int(input("변경 영어 점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name}학생 성적이 수정되었습니다.")
                else:
                    print("[수학 성적 수정.]")
                    print(f"현재 수학점수 : {s[4]}")
                    s[4] = int(input("변경 수학 점수 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name}학생 성적이 수정되었습니다.")
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력하세요.")
        
    
    
    
    elif choice == 4:
        print("[ 학생 성적 삭제 ]")
        name = input("삭제할 학생 이름을 입력하세요. : ")
        for i,s in enumerate(students):
            temp = 0
            if name in s: #있을 경우
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                choice = int(input(f"{name}학생 성적을 삭제할까요?(0.취소, 1.삭제)"))
                if choice == 1:
                    print(f"{name} 학생 성적을 삭제했습니다.")
                    del students[i]
                else:
                    print(f"{name} 학생 성적 삭제를 취소했습니다.")
                break # 반복문을 중지시켜줌.
            
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 실행하세요.")
        print()
        
    elif choice == 6:
        pass
    elif choice == 0:
        print('프로그램을 중료합니다.')
        break
    
    
    
#del index()
#pop 마지막 순번 삭제
#remove 해당 데이터를 가지고 삭제
#