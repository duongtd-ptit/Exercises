class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def amount(self):
        print(f"So du hien tai: {self.__balance}đ")
        amount = int(input("Nhap so tien muon rut: "))
        self.__balance -= amount
        print(f"So du con lai: {self.__balance}đ")

acc = BankAccount("Duong",100000)
acc.amount()