students = list()
count = 1
while True:
    student = []
    no = count
    name = input("이름. :")
    kor = int(input("국어. :"))
    eng = int(input("영어. :"))
    math = int(input("수학. :"))
    total = kor+eng+math
    avg = total/3
    rank = 0
    student = [no,name,kor,eng,math,total,avg,rank]
    students.append(student)
    count += 1

    # 학생 성적 출력
    print("[  학생 성적 프로그램  ]")
    print("-"*70)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
    for stu in students:
        for i,s in enumerate(stu):
            if i != 6:
                print(s,end='\t')
            else:
                print(f"{s:.2f}",end="\t")
        print()
# students = [[1,'홍길동',100,100,100,300,100.0,0],[1,'홍길동',100,100,100,300,100.0,0],[1,'홍길동',100,100,100,300,100.0,0]]

# print("[  학생 성적 프로그램  ]")
# print("-"*70)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
# for stu in students:
#     for s in stu:
#         print(s,end='\t')
#     print()