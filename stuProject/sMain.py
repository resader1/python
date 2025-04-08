



















while True:
    print("[학생성적프로그램]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("0. 프로그램 종료")
    choice = 0
    try:
        choice = int(input("번호 선택 : "))
    except Exception as e: print(e)
    
    
    if choice == 1:
        print("학생성적입력")
        name = input("이름 입력")
        kor = int(input("국어 성적 입력"))
        eng = int(input("영어 성적 입력"))
        math = int(input("수학 성적 입력"))
        total = kor+eng+math
        avg = total/3

        