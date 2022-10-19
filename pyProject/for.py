

sum = 0
for i in range(3333,10000):
    if i%1234==0:
        sum += i
        print(i)
    if sum > 100000:
        print(sum)
        break
print(sum)