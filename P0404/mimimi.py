from stu_func import *

students = []

with open("P0404/stu.txt","r",encoding="utf8") as f:
    while True:               # 여러줄일때 반복문 적용
        line = f.readline()   # 1줄 읽어오기
        if not line: break    # 문자열 없을때 종료
        s = line.strip().split(",") # 1줄 문자열을 ,기준으로 분리
        students.append({
            "no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),
            "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])
        })
        
print(students)