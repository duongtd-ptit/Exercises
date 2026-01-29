class Student:
    def __init__(self,name,age,MSV):
        self.name = name
        self.age = age
        self.MSV = MSV
    def sayhello(self):
        print(f"Xin chào sinh viên: {self.name} (MSV :{self.MSV} -- Tuổi {self.age})")
sv1 = Student("Trần Đăng Dương",18,"B25DCCC065")
print(sv1.name)
print(sv1.age)
sv1.sayhello()