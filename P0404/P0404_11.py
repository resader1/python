import stu_func

students = []

with open("P0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data = f.readline() #
        if not data: break # ''공백이면 반복문 종료
        s = data.strip().split(",") # strip() - 공백제거, split(",") - , 기준으로 분리
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7]),
        })
        

count = max(students,key=lambda x:x['no'])['no']+1
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print("[ 학생 성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("7. 학생성적저장")
    print("0. 프로그램 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요. : "))

    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input("이름을 입력하세요. : ")
        kor = int(input("국어 점수 입력 : "))
        eng = int(input("영어 점수 입력 : "))
        math = int(input("수학 점수 입력 : "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        students.append({
            "no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank
        })
        
        print(f"{no}번 {name}학생 저장.")
        print()

    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")
            
        
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        print("[ 학생성적 저장 ]")
        with open("P0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(data)
                
        print("파일 저장 완료")
    elif choice == 0:
        print("프로그램 종료")
        break






