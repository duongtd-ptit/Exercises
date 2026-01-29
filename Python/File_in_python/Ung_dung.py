students = ["An","Binh","Cuong","Dung"]
with open("Class.txt","w",encoding="utf-8") as f: #tao file
    for i in students:
        f.write(f"{i}\n") #co the: f.write(i+"\n")

with open("Class.txt","r",encoding="utf-8") as f:
    name = f.readlines()
    for n in name:
        print("Sinh vien:",n.strip())       