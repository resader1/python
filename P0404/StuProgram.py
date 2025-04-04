import stu_func

# stu.txt파일에서 데이터 읽어와 students = [] 데이터 입력시킴.
### 파일 불러오기
students = []
with open("P0404/stu.txt","r",encoding="utf8") as f:
    while True: # 여러줄일때 반복문 적용
        line = f.readline() # 한줄 읽어오기
        if not line: break # 문자열 없을 때 종료
        s = line.strip().split(",") # 1줄 문자열을, 기준으로 분리
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })

f.close

for s in students:
    print(s)

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
    elif choice == 5: # 학생 성적 정렬
        students2 = [*students] #복사
        print("[학생 성적 정렬]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면 이동")
        print("-"*50)
        choice = int(input("원하는 번호를 입력하세요. : "))
        if choice == 1: # 이름 순차정렬
            students2.sort(key=lambda x:x['name'])
        elif choice == 2: # 이름 역순정렬
            students2.sort(key=lambda x:x['name'],reverse=True)
        elif choice == 3: # 합계 순차정렬
            students2.sort(key=lambda x:x['total'])
        elif choice == 4: # 합계 역순정렬
            students2.sort(key=lambda x:x['total'],reverse=True)
        elif choice == 5: # 번호 순차정렬
            students2.sort(key=lambda x:x['no'])
        elif choice == 6: # 번호 역순정렬
            students2.sort(key=lambda x:x['no'],reverse=True)
        elif choice == 0:
            continue
        stu_func.stu_output(title,students2)
            
            
    elif choice == 6: # 학생 성적 삭제
        print("[ 학생 성적 삭제 ]")
        name = input("삭제하고자 하는 학생이름을 입력하세요. : ")
        temp = 0
        for i,s in enumerate(students):
            if name == s['name']:
                print(f"{s['no']}.번{name}학생을 찾았습니다.")
                answer = input("학교성적을 삭제할까요?(삭제하시면 복구 불가)")
                if answer == "y":
                    del students[i]
                print(f"{name}학생의 성적이 삭제.")
                print()
                break
        if temp == 0:
            print("삭제하고자 하는 학생을 찾지 못함.")
    elif choice == 7:
        print("[ 학생성적저장]")
        with open("P0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                # 1,홍길동,100,100,100,300,100.0,1
                line = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다.")
        print()
            
            
            
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break