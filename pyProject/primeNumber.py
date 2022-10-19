# 소수 구하기 print Prime Number
l = []
for i in range(3,101):
    cnt = 0
    for j in range(2,i):
        if i%j==0:
            cnt += 1
    if cnt == 0:
        l.append(i)
print(l)