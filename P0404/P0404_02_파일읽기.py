# 파일입출력 : 파일 열기 - 파일읽기, 파일쓰기 - 파일 닫기
# 파일열기 - 3가지 모드 : r:읽기모드, w:쓰기모드, a:추가모드, b:이진모드-파일복사
# f = open("a.txt","r") # 읽기모드
# f = open("a.txt","w") # 쓰기모드
# f = open("a.txt","a") # 추가모드


# news.txt 파일 출력하시오.
f = open("P0404/news.txt",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()





# 파일 읽어오기 - 절대경로
# f = open("C:/workspace/python/a.txt","r",encoding="utf-8")
# f = open("P0404/b.txt","r",encoding="utf-8") #폴더 안에 있는 파일 읽어오기
# for list in f:
#     print(list.strip())
# f.close()


# while True: # 3줄
#     line = f.readline()
#     if not line: break
#     print(line.strip())
# f.close()








# 파일읽기 - readlines() : 모두 읽어오기
# f = open("a.txt","r",encoding="utf-8")
# lines = f.readlines() # 모두읽어오기
# for line in lines:
#     print(line.strip())
# f.close()


# 파일읽기 - r 1줄읽기 read()
# f = open("a.txt","r",encoding="utf-8")
# print(type(f))
# for line in f:
#     print(line.strip())
# f.close()


# print("완료되었습니다.")