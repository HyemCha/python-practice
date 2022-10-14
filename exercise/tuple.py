# 071
my_variable = ()

# 072
my_variable = ('닥터 스트레인지', "스플릿", "럭키")
print(my_variable)

# 073
num = (1,)
print(num)

# 074
t = (1,2,3)
# t[0] = 'a'

# 075
t = 1,2,3,4
print(t)

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c') # 기존의 튜플은 자동으로 삭제됨
print(t)

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest))

# 078
interest = tuple(interest)
print(type(interest))

# 079
temp = ('apple', 'banana', 'cake')
a,b,c = temp
print(a,b,c)

# 080
tu = tuple(range(2,100,2))
print(tu)
print(tuple(range(2,100)))