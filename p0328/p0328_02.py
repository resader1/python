print("안녕.")
print("안녕.")
print("안녕.")
print("안녕.")

#반복문

#range(3) = 0,1,2
for i in range(3):
    print("안녕",i)
    
#range(1,4) = 1,2,3 : 4 앞까지 출력
for i in range(1,4):
    print("안녕하",i)
    
#range(1,11,2) = 1에서 10까지인데 2씩 증가함.
#range 첫번째 숫자는 시작번호, 두번째 숫자는 마지막 번호보다 1 큼, 세번째 숫자는 간격
for i in range(1,11,2):
    print("한녕",i)
    
    
# range() 자리에 list 타입도 가능
a_list = [1,2,3,4,5]
for i in a_list:
    print("안녕",i)