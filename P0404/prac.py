

students = []

with open("P0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data = f.readline()
        if not data: break
        s = data.strip().split(",")
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7]),
        })
            
            



with open("P0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data = f.readline()
        if not data: break
        s =  data.strip().split(",")
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":int(s[6]),"rank":int(s[7])
        })
     
     
count = 4
     
     
        
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


if choice == 1:
    print("[학생성적프로그램]")
    no = count
    name = input("이름 입력")
    kor = int(input("국어점수 입력"))
    eng = int(input("영어점수 입력"))
    math = int(input("수학점수 입력"))
    total = kor+eng+math
    avg = total/3
    rank = 0
    students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
    count += 1
    
    
elif choice == 2:
    pass