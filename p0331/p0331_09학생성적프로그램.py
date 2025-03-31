students = list()
count = 1

while True:
    print(" "*20,end="")
    print("[학생 성적 프로그램]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("5. 학생성적 정렬")
    print("6. 학생성적 검색")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요. : "))
    print()
    
    if choice == 1:
        students = list()
        count = 1
        while True:
            student = []
            no = count
            name = input("이름. :")
            kor = int(input("국어. :"))
            eng = int(input("영어. :"))
            math = int(input("수학. :"))
            total = kor+eng+math
            avg = total/3
            rank = 0
            student = [no,name,kor,eng,math,total,avg,rank]
            students.append(student)
            count += 1
    elif choice == 2:
            # 학생 성적 출력
        print("[  학생 성적 프로그램  ]")
        print("-"*70)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        for stu in students:
            for i,s in enumerate(stu):
                if i != 6:
                    print(s,end='\t')
                else:
                    print(f"{s:.2f}",end="\t")
            print()
    elif choice == 0:
        print("[프로그램 종료]")
        break
    print()
