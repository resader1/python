a = "쮸잉큐님. 안녕안녕안녕하세요.안녕"

# a.find() 와 for 문을 사용해서 안녕이 몇번 나오는지 개수를 출력하시오

i = 0
count=0
while True:
    num = a[i:].find("안녕")
    if num != -1:
        count += 1
        i += num+1
    else: break
    
print("개수 : ",count)
    
    
# if"안녕" in a:
#     print("안녕이라는 글자가 있습니다.")
    
# print(a.find("안녕"))
    
    
    
    
    
    
    
    
# print(a.count("안녕"))