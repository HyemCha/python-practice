for i in range(5,-1,-1):
    print("%d"%i)

dan = 15
for i in range(9,0,-1):
    print("%d x %d = %3d" %(dan, i, dan*i))

sum = 0
for i in range(3333,10000):
    if i%1234==0:
        sum += i
    if sum > 100000:
        # sum-=i
        break
print(sum)