# 구구단 출력

#2 x 1 = 2

for j in range(1,10):
    for i in range(2,10):
        print("{} x {} = {}".format(i,j,i*j),end="\t")
    print("")


## 은행가면 001 002 003 ... 010 011 012 ... 999

# for i in range(1,1000):
#     print("{:03d}".format(i))