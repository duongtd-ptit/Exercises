with open("data.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())
#with open khong can den f.close() de dong file, chay het code file tu dong dong

with open("note.txt","w",encoding="utf-8") as f:
    f.write("Hom nay muon an gi??\n")
    f.write("Em an gi cung duoc!\n")