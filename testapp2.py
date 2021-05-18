mydict = { }

mydict[(1,2,3)] = 4
mydict[(2,3,4)] = 5

print(mydict)
for i in range(1,3):
    print(mydict[(i,2,3)])
