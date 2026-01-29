import os
from datetime import date

today = date.today()
folder_name = f"log_{today}"
if not os.path.exists(folder_name): #kiem tra thu muc co ton tai khong, neu khong thi tao ra thu muc
    os.mkdir(folder_name)
    print("Da tao them thu muc:",folder_name)
else:
    print(f"Thu muc {folder_name} da ton tai!!")