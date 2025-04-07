class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no = no
        self.__name = name
        self.__kor = kor # __언더바2개 접근제한 : 캡슐화
        self.__eng = eng
    
    def getNo(self):
        return self.__no
    def getName(self):
        return self.__name
    
    def getKor(self):
        return self.__kor
    # setter
    def setKor(self,kor):
        if kor>=0 and kor<=100:
            self.__kor = kor
        else:
            raise NotImplementedError("유효한 값 아님")
    # getter
    def getEng(self):
        return self.__eng
    # setter
    def setEng(self,eng):
        if eng>=0 and eng<=100:
            self.__eng = eng
        else: raise NotImplementedError("유효한 값 아님")
        
        
    def __str__(self):
        return f"{self.no},{self.name},{self.__kor},{self.eng}" 
        
s = Stu(1,"홍길동",100,99)
s.__kor = 200
print(s.no,s.name,s.__kor) # 지역변수개념의 s.__kor의 값 출력
s.eng = 300
s.SetKor(500)
print(s)