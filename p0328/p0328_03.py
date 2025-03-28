# 반복문을 사용해서 1-10까지 출력
# for i in range(1,11):
#     print(i)
    
a = "도봉리 마을 박막례"
print(a[2])

a_list = [1,2,3,4,5]
print(a_list[2])
print("-"*80)
print(a_list[1:4]) # 시작 위치:끝나는 위치 - 슬라이싱
print("-"*80)
print(a_list[:3]) # :끝나는 위치 - 처음부터 끝나는 위치까지 출력
print("-"*80)
print(a_list[2:]) # 시작위치: - 시작위치부터 끝까지 출력
print("-"*80)
print(a_list[::2]) # 2칸씩 띄워서 출력
print(a_list[::3]) # 3칸씩 띄워서 출력
print(a_list[::-1]) # 역순으로 출력
print(a_list[:-1]) # -1위치 제외하고 출력(-1은 맨 뒤)

print(len(a_list)) # 리스트 내 표본 수 확인
print(len(a))
print(a_list[:len(a_list)-1])

# sum = 0
# for i in range(1,100+1):
#     sum = sum + i
    
# print("1-100까지 합계 : {}".format(sum))



# 합계가 100 넘는 위치의 숫자는 얼마일까요? 그 떄 값도 출력하시오

sum = 0
for i in range(1,100):
    sum = sum + i
    if sum>100:
        break
print("i:{}, sum : {}".format(i,sum))