# 학생 성적 프로그램
# 이름, 국어, 영어, 수학 입력받아서 합계, 평균을 출력하는 프로그램을 구현


a = input("이름을 입력하세요. :")
b = int(input("국어 점수를 입력하세요. :"))
c = int(input("국어 점수를 입력하세요. :"))
d = int(input("국어 점수를 입력하세요. :"))
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
total = int(b+c+d)
avg = total / 3
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(a,b,c,d,total,avg))