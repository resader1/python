# 1,3,5,7,9................99 1-100 사이의 홀수만 숫자를 더해서 값을 구하시오
sum = 0
for i in range(1,100+1,2):
    sum = sum + i

print("합계 : {}".format(sum))


# 1부터 100까지의 3의 배수만 더하기 해서 sum을 구하시오
# if i#3 == 0

sum = 0
sum_list = []
for i in range(1,100+1):
    if i%3 == 0:
        sum = sum + i
        print("i : {}, sum : {}".format(i,sum))
        sum_list = sum
        
print(sum)
print(sum_list)

print("-"*80)
#3의 배수 이면서 5의 배수
sum = 0
for i in range(1,100+1):
    if i%3 == 0 and i%5 == 0:
        sum = sum + i
        print("i : {}, sum : {}".format(i,sum))

print("-"*80)
#3의 배수 혹은 7의 배수
sum = 0
for i in range(1,100+1):
    if i%3 == 0 or i%7 == 0:
        sum = sum + i
        print("i : {}, sum : {}".format(i,sum))
print("3또는 7의 배수들의 합 : {}".format(sum))
# 1-100까지의 숫자의 합을 구하시오
sum = 0
for i in range(1,100+1):
    sum = sum + i
    
print("1-100까지의 합계 : {}".format(sum))


