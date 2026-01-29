#Binary Files (File nhị nhân) : là các file ảnh, âm thanh, video,...    
try:
    with open("image.jpg","rb") as f:
        data = f.read()
        print("Kich thuoc file:",data,"bytes")
except FileNotFoundError:
    print("File khong ton tai")