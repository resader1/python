# with 파일
# with open("P0404/a1.txt","w",encoding="utf-8") as f:
#     f.write("안녕")

# print("저장완료")






# 학생성적 -> 파일쓰기
# f = open("P0404/stu.txt","a",encoding="utf-8")
# no = 1
# while True:
#     name = input("이름을 입력하세요.(0.종료) : ")
    
#     if name == "0":break
#     kor = int(input("국어점수 입력 : "))
#     eng = int(input("영어점수 입력 : "))
#     total = kor+eng
#     lines = f"{no},{name},{kor},{eng},{total}\n"
#     f.write(lines)
#     no += 1


# f.close()
# print("학생성적이 저장되었습니다.")