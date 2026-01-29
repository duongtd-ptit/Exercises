f = open("output.txt","w",encoding="utf-8")
f.write("Xin chao cac ban!\n") #neu chua co file --> tao file moi / co file r --> ghi de file
f.write("Day la dong thu 2\n")
f.close()


f = open("output.txt","a",encoding="utf-8")
f.write("Day la dong moi duoc them vao")
f.close()