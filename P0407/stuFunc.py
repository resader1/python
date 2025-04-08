from stuModule import Student,Students

# Students 객체선언
students = Students()
title = ['번호','이름','국어','영어','수학','합계','평균','등수']


# ----------------------------------------------------------
# 상단 메뉴
def tmenu_print():
    print(" "*20)
    print("[ 학생성적처리 프로그램 ]")
    print(" "*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    choice = 0
    try:
        choice = int(input("원하는 번호를 입력하세요. : "))
    except Exception as e:
        print(e)
    return choice


#--------------------------------------------------------------
# 학생성적입력 함수 선언
def stu_input():
    print("[ 학생성적입력 ]")
    name = input(f"{Student.count}번째 학생 이름 입력. : ")
    score = [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"{title[i+2]} 점수를 입력하세요"))
    students.add(Student(name,*score))
    print(f"{name} 학생이 등록됨.")
    print()



#-------------------------------------------------------------
# 학생성적출력 함수 선언
def stu_output():
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students: # 참조변수명. 리스트변수.
        print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}")


# ---------------------------------------------------------------
# 학생성적수정
def stu_modify():
    print("[ 학생성적수정 ]")
    search = input("수정하고자 하는 학생 입력 : ")
    temp = 0 # 찾지 못했을 때 사용 변수
    for s in students.students:
        if search == s.name:
            temp = 1
            print(f"{search} 학생을 찾음. 성적 수정.")
            print("[ 수정과목 선택 ]")
            print("1. 국어, 2. 영어, 3. 수학")
            print("-"*40)
            try:
                choice = int(input("원하는 번호 입력 : "))
            except Exception as e: print(e)
            if choice == 1:
                s.kor = sub_modify(s.kor,choice)
            elif choice == 2:
                s.eng = sub_modify(s.eng,choice)
            elif choice == 3:
                s.math = sub_modify(s.math,choice)
            s.stu_total()
            s.stu_avg()
            print()
    if temp == 0:
        print(f"{search} 찾을 수 없음.")
        



# ------------------------------------------------------------
# 과목점수수정
def sub_modify(subject,choice):   # subject = s.kor,s.eng,s.math
    print(f"[ {title[choice+1]}과목 수정 ]")
    print(f"현재 {title[choice+1]} 점수 : {subject}")
    subject = int(input(f"수정할 {title[choice+1]}점수 입력 : "))
    print(f"{subject} 점으로 {title[choice+1]} 점수가 변경됨")
    return subject


