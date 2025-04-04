# 문서 읽어오기 - r
# 일반파일 읽어오기 - rb
f = open('P0404/a.jpg','rb') # 파일 읽기
ff = open("C:/down/b.jpg","wb") # 파일 쓰기

# 이진파일은 용량이 클 수 있으므로, 1byte 읽어오기
while True:
    fData = f.read(1)
    if not fData: break
    # len = ff.write(fData)
f.close()
print("파일 읽어오기 완료")

# 문서저장 - w,a
# 파일저장 - wb
# 폴더 존재 확인 : os.path.exists()
# 폴더 생성 : os.makedir(): 폴더 1개 생성  - C:/down1/aaa/a.jpg
# 폴더 생성 : os.makedirs(): 모든 폴더 생성 - C:/down1/aaa/a.jpg
import os
if not os.path.exists("C:/down1"):
    os.makedirs("C:/down1")
ff = open("c:/down1/b.jpg","wb")
len = ff.write(fData)
print(f"파일크기 : {len} 바이트")
ff.close()

print("파일 저장완료")