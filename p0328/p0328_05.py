# 구구단 출력
# for i in range(2,9+1):
#     print("[ {} 단]".format(i))
#     for j in range(1,9+1):
#         print("{} x {} = {}".format(i,j,i*j),end=" ")
#     print()
    
    
    
# 3,5,7,9 홀수 단만 출력하시오.




# 시작 단과 끝나는 단을 입력받아 출력하시오.
# 2,6 -> 2~6단 출력

a = int(input("숫자 입력 : "))
b = int(input("숫자 입력 : "))
t = 0
if a>b:
    t = a
    a = b
    b = t
for i in range(a,b+1):
    for j in range(1,10):
        print("{} x {} = {}".format(i,j,i*j))
    print()