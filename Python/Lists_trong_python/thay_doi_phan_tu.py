mylist = [10, 20, 30, 40, 50, 60,70,42,23,554,234,675,54,55,23,64,109]

for i in range(len(mylist)):
    if i % 2 ==0:
        print(mylist[i])

for i in range(len(mylist)):
    mylist[i] += (i+1)
print(f"{mylist}")


mylist1 = [10, 20, 30, 40, 50, 60,70,42,23,554,234,675,54,55,23,64,109]
mylist2 = [x+10 for x in mylist1 ] 
print(mylist2)

mylist3 = list(map(lambda x:x + 10,mylist1))
print(mylist3)