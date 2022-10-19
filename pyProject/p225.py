nn = [100,200,300,400,500]
print(nn[2:-1])
print(nn[::-1])
# nn[1:4]=[444,555]
# print(nn)
# nn[1]=[444,555]
nn[2:]=[]
print(nn)

myData = [[n*m for n in range(1,3)]for m in range(2,4)]
print(myData)