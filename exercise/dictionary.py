# 081
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

# 082
a,a,*valid_score = scores
print(a,valid_score)

# 083
_, *valid_score, _ = scores
print(valid_score)

# 084
temp = {}
print(temp)

# 085
dic = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(dic)

# 086
# 틀림 dic += {'죠스바':1200, '월드콘':1500}
dic['죠스바'] = 1200
dic['월드콘'] = 1500
print(dic)

# 087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(ice['메로나'])

# 088
ice['메로나'] = 1300
print(ice)

# 089
del ice['메로나']
print(ice)

# 090

# 091
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

# 092
print(inventory['메로나'][0])

# 093
print(inventory['메로나'][1])

# 094
inventory['월드콘'] = [500,7]
print(inventory)

# 095
k = list(inventory.keys())
print((inventory.keys()))

# 096
v = list(inventory.values())
print(v)

# 097
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

# 098
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)