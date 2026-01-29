#Ghi đè những giữ logic của lớp cha
class Student:
    def __init__ (self,name,MSV):
        self.name = name
        self.MSV = MSV
        print(f"Khởi tạo sinh viên: {self.name} -- Mã sinh viên: {self.MSV}")
class CV(Student):    
    def __init__ (self,name,MSV,CV):
        super().__init__(name,MSV)
        self.CV = CV
        print(f"Khởi tạo chức vụ {self.CV} cho {self.name}")
        
sv1 = CV("Trần Đăng Dương", "B25DCCC065","Lớp trưởng")