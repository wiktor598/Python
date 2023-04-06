mylist = ["4","2","3","1"]

ans = input("Print in asc or desc ? ")

if ans == "asc":
 mylist.sort()
 print (mylist)
 
elif ans == "desc":
 mylist.sort(reverse=True)
 print(mylist)




