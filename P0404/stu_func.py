# 화면 출력 함수 선언
def stu_print():
    print("[ 학생 성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print("5. 학생성적 정렬")
    print("6. 학생성적 삭제")
    print("7. 학생성적 저장")
    print("0. 프로그램 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요. : "))
    return choice
    
# 1. 학생성적입력 함수 선언
def stu_input(count,students):
    while True:
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요. : / 0 입력시 이전화면")
        if name == '0': break
        kor = int(input("국어 점수를 입력하세요. : "))
        eng = int(input("영어 점수를 입력하세요. : "))
        math = int(input("수학 점수를 입력하세요. : "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
        print(f"{no}번 {name}학생이 등록되었습니다.")
        print()
        count += 1
        return count
        
        
# 2. 학생 성적 출력 함수 선언
def stu_output(title,students):
    # 학생성적출력부분
    print("[ 학생 성적 출력]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print() 
    
    
# 3. 등수 출력
def stu_rank(students):
    print("[등수처리]")
    for s in students:
        num = 1
        for ss in students:
            if s['total']<ss['total']:
                num += 1
        s['rank'] = num # 등수입력
    print("[등수처리 완료]")
    print()