
class Student:
    count = 1
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        Student.count += 1 # 객체선언시마다 1 증가
    
    def __str__(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math}"


class Students:
    def __init__(self):
        self.students = []
        
    def add(self,s):
        self.students.append(s)
        
    def __str__(self): # 리턴이 무조건 문자열을 해줘야 함
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""
            
            
         
ss = Students()
s = Student("홍길동",100,100,99)
s2 = Student("유관순",90,90,91)
s3 = Student("이순신",80,80,89)
ss.add(s)
ss.add(s2)
ss.add(s3)

print(ss)

# class Student:
#     #생성자 함수
#     # 인스턴스 변수 - 객체선언시 각각 변수들이 존재 : 공용으로 사용 안됨.
#     # no = 1
#     # name = "" # 인스턴스 변수
#     count = 1 # 클래스 변수 - 모든 객체가 공용으로 사용하는 변수
    
#     def __init__(self,name,kor,eng,math):
#         self.no = Student.count
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math
#         self.total = kor+eng+math
#         self.avg = self.total/3
#         self.rank = 0
#         Student.count += 1 # 객체선언시마다 1 증가
        

# # 매개변수가 있는 생성자를 활용해서 데이터 입력
# s = Student("홍길동",100,100,99)
# print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,Student.count)
# s2 = Student("유관순",99,99,98)
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math,s2.total,s2.avg,Student.count)

# s3 = Student("이순신",90,90,91)
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math,s3.total,s3.avg,Student.count)






# # 기본생성자를 이용해 객체선언 후 데이터 입력
# class Student:
#     no = 1
#     name = ""
    
    
    
# s = Student() # 기본생성자
# s.name = "홍길동"
# print(s.no, s.name)

# s2 = Student()
# s2.no = 2
# s2.name = "이순신"
# print(s2.no,s2.name)