running = True
dicts = {"Lion":"Sư tử", "Tiger":"Hổ", "Elephant":"Voi", "Giraffe":"Hươu cao cổ", "Monkey":"Khỉ", "Zebra":"Ngựa vằn", "Bear":"Gấu", "Wolf":"Sói", "Deer":"Hươu/Nai", "Fox":"Cáo", "Rabbit":"Thỏ", "Squirrel":"Sóc", "Dolphin":"Cá heo", "Whale":"Cá voi", "Shark":"Cá mập", "Eagle":"Đại bàng", "Owl":"Cú", "Snake":"Rắn", "Crocodile":"Cá sấu", "Kangaroo":"Chuột túi","Manager":"Quản lý", "Engineer":"Kỹ sư", "Analyst":"Nhà phân tích", "Developer":"Lập trình viên", "Designer":"Nhà thiết kế", "Consultant":"Cố vấn/Chuyên gia tư vấn", "Specialist":"Chuyên viên", "Accountant":"Kế toán viên", "Marketer":"Chuyên gia tiếp thị", "Journalist":"Nhà báo", "Architect":"Kiến trúc sư", "Technician":"Kỹ thuật viên", "Secretary":"Thư ký", "Receptionist":"Lễ tân", "Executive":"Quản lý cấp cao/Điều hành", "Operator":"Người vận hành", "Supervisor":"Giám sát viên", "Librarian":"Thủ thư", "Mechanic":"Thợ máy", "Cashier":"Nhân viên thu ngân","Quản lý":"Manager", "Kỹ sư":"Engineer", "Nhà phân tích":"Analyst", "Lập trình viên":"Developer", "Nhà thiết kế":"Designer", "Cố vấn/Chuyên gia tư vấn":"Consultant", "Chuyên viên":"Specialist", "Kế toán viên":"Accountant", "Chuyên gia tiếp thị":"Marketer", "Nhà báo":"Journalist", "Kiến trúc sư":"Architect", "Kỹ thuật viên":"Technician", "Thư ký":"Secretary", "Lễ tân":"Receptionist", "Quản lý cấp cao/Điều hành":"Executive", "Người vận hành":"Operator", "Giám sát viên":"Supervisor", "Thủ thư":"Librarian", "Thợ máy":"Mechanic", "Nhân viên thu ngân":"Cashier","Sư tử":"Lion", "Hổ":"Tiger", "Voi":"Elephant", "Hươu cao cổ":"Giraffe", "Khỉ":"Monkey", "Ngựa vằn":"Zebra", "Gấu":"Bear", "Sói":"Wolf", "Hươu/Nai":"Deer", "Cáo":"Fox", "Thỏ":"Rabbit", "Sóc":"Squirrel", "Cá heo":"Dolphin", "Cá voi":"Whale", "Cá mập":"Shark", "Đại bàng":"Eagle", "Cú":"Owl", "Rắn":"Snake", "Cá sấu":"Crocodile", "Chuột túi":"Kangaroo"}

while running:
    selection = int(input("\t---Từ điển Anh-Việt---\n1--Tra cứu từ điển\n2--Thêm từ điển\n3--Xoá từ trong từ điển\n4--Thoát chương trình\n5--Xem toàn bộ thư viện\n\nNhập lựa chọn của bạn: "))
    if selection==1:
        input_text = input("Nhập từ của bạn cần tra: ").capitalize()
        if input_text not in dicts:
            print("Từ này chưa có trong thư viện")
        else:
            print(dicts.get(input_text))
        continue_process = input("Bạn có muốn tiếp tục không? (y/n)\n\t").lower()
        if continue_process == "n":
            print("Đã thoát chương trình!! Hẹn gặp lại bạn sau")
            running = False
        else:
            print("Chương trình sẽ tiếp tục\n")
            continue    
    elif selection==2:
        input_text = input("Nhập từ bạn muốn thêm: ").capitalize()
        if input_text not in dicts:
            a = input(f"Nhập nghĩa của từ {input_text}: ").capitalize()
            dicts[input_text] = a
            dicts[a] = input_text
        else:
            print("Từ của bạn đã có trong từ điển")
        continue_process = input("Bạn có muốn tiếp tục không? (y/n)\n\t").lower()
        if continue_process == "n":
            print("Đã thoát chương trình!! Hẹn gặp lại bạn sau")
            running = False
        else:
            print("Chương trình sẽ tiếp tục\n")
            continue
    elif selection == 3:
        input_text = input("Nhập từ bạn muốn xoá: ").capitalize()
        if input_text not in dicts:
            print("Từ của bạn không có trong thư viện")
        else:
            print(f"Đã xoá từ {input_text} khỏi thư viện")
            del_vnese = input("Hãy nhập nghĩa tiếng việt của từ đó:\t")
            del dicts[input_text]
            del dicts[del_vnese]
        continue_process = input("Bạn có muốn tiếp tục không? (y/n)\n\t").lower()
        if continue_process == "n":
            print("Đã thoát chương trình!! Hẹn gặp lại bạn sau")
            running = False
        else:
            print("Chương trình sẽ tiếp tục\n")
    elif selection == 4:
        print("Hẹn gặp lại bạn vào lần sau sử dụng nhé!!")
        running = False
    elif selection == 5:
        for key,value in dicts.items():
            print(f"Các từ có trong thư viện và nghĩa của nó hiện tại là:\n {key}--{value}")