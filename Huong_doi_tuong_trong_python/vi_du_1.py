class Student:
    def __init__(self,name,age,maSV):
        self.name = name
        self.age = age
        self.maSV = maSV
    def say_hello(self):
        print(f"Xin chao, toi la {self.name}")
    def thong_tin_SV(self):
        print("Thong tin sinh vien")
        print(f"Ho va ten: {self.name}")
        print(f"Ma SINH VIEN: {self.maSV}")
        print(f"Tuoi: {self.age}")
        
sv1 = Student("Trần Đăng Dương",18,"B25DCCC065")
sv2 = Student("Đặng Đức Việt",18,"B25DCCC111")
sv2.say_hello()
sv1.thong_tin_SV()