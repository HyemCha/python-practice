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