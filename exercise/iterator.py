# 131
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 132
# fruit = ['apple', 'orange', 'watermelon']
# for i in fruit:
#     print('#####')

# 133
# 134
# for i in ['A', 'B', 'C']:
#     print('print', i)
# print('print', 'A')
# print('print', 'B')
# print('print', 'C')

# 135
# for i in ['a', 'b', 'c']:
#     b = i.upper()
#     print('변환', b)

# 136
# for i in [10, 20, 30]:
#     print(i)

# 137
# for i in [10, 20, 30]:
#     print(i)

# 138
# for i in [10, 20, 30]:
#     print(i)
#     print('-'*7)

# 139
# print('++++')
# for i in [10, 20, 30]:
#     print(i)

# 140
# for i in range(4):
#     print('-'*7)

# 141
# l = [100, 200, 300]
# for i in l:
#     print(i+10)

# 142
# l = ["김밥", "라면", "튀김"]
# for i in l:
#     print('today\'s menu', i)

# 143
# l = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in l:
#     print(len(i))

# 144
# l = ['dog', 'cat', 'parrot']
# for i in l:
#     print(i, len(i))

# 145
# l = ['dog', 'cat', 'parrot']
# for i in l:
#     print(i[0])

# 146
# l = [1, 2, 3]
# for i in l:
#     print('3 x', i)

# 147
# l = [1, 2, 3]
# for i in l:
#     print('3 x', i, '=', 3*i)

# 148
# l = ["가", "나", "다", "라"]
# for i in l[1:]:
#     print(i)

# 149
# l = ["가", "나", "다", "라"]
# for i in l[::2]:
#     print(i)

# 150
# l =  ["가", "나", "다", "라"]
# for i in l[::-1]:
#     print(i)

# 151
# l = [3, -20, -3, 44]
# for i in l:
#     if i < 0:
#         print(i)

# 152
# l = [3, 100, 23, 44]
# for i in l:
#     if i%3 == 0:
#         print(i)

# 153
# l = [13, 21, 12, 14, 30, 18]
# for i in l:
#     if i < 20 and i%3==0:
#         print(i)

# 154
# l = ["I", "study", "python", "language", "!"]
# for i in l:
#     if len(i) >= 3:
#         print(i)

# 155
# l = ["A", "b", "c", "D"]
# for i in l:
#     if i.isupper():
#         print(i)

# 156
# l = ["A", "b", "c", "D"]
# for i in l:
#     if i.islower():
#         print(i)

# 157
# l = ['dog', 'cat', 'parrot']
# for i in l:
#     print(i.capitalize())

# 158
# l = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in l:
#     i = i.split('.')[0]
#     print(i)

# 159
# l = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in l:
#     tail = i.split('.')[1]
#     if tail == 'h':
#         print(i)

# 160
# l = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in l:
#     tail = i.split('.')[1]
#     if tail == 'h' or tail == 'c':
#         print(i)

# 161
# for i in range(100):
#     print(i)

# 162
# for i in range(2002,2051, 4):
#     print(i)

# 163
# for i in range(0,31,3):
#     print(i)

# 164
# for i in range(99,-1, -1):
#     print(i)
# for i in range(100):
#     print(99-i)

# 165
# for i in range(10):
#     print(i/10)

# 166
# for i in range(1,10):
#     print('3x' + str(i), '=', 3*i)

# 167
# for i in range(1,10,2):
#     print('3x' + str(i), '=', 3*i)

# 168
# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)

# 169
# sum = 0
# for i in range(1,11,2):
#     sum += i
# print(sum)

# 170
# sum = 1
# for i in range(1, 11):
#     sum *= i
# print(sum)

# 171 range()에는 정수형만 들어올 수 있음
# pl = [32100, 32150, 32000, 32500]
# for i in range(len(pl)):
#     print(pl[i])

# 172
# l = [32100, 32150, 32000, 32500]
# for i in range(len(l)):
#     print(i, l[i])
# for i, data in enumerate(l):
#     print(i, data)

# 173
# for i in range(len(l)):
#     print(len(l)-1-i, l[i])

# 174
# for i in range(1, len(l)):
#     print(100+10*i, l[i])

# 175
# l = ["가", "나", "다", "라"]
# for i in range(len(l)-1):
#     print(l[i], l[i+1])

# 176
# l = ["가", "나", "다", "라", "마"]
# for i in range(len(l[:3])):
#     print(l[i], l[i+1], l[i+2])

# 177
# l = ["가", "나", "다", "라"]
# for i in range(len(l),1,-1):
#     print(l[i-1], l[i-2])
# for i in range(len(l)-1):
#     print(l[-1*(len(l)-3-i)],l[-1*(len(l)-2-i)])

# 178
# l = [100, 200, 400, 800]
# for i in range(len(l)-1):
#     print(l[i+1]-l[i])

# 179
# l = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(l)-2):
#     print((l[i]+l[i+1]+l[i+2])/3)

# 180
# low = [100, 200, 400, 800, 1000]
# high = [150, 300, 430, 880, 1000]
# v = []
# for i in range(len(low)):
#     v.append(high[i] - low[i])
# print(v)

# 181 two-dimensional list
apart = [[101,102], [201,202], [301, 302]]

# 182
stock =[['시가', 100,200,300], ['종가', 80,210,330]]

# 183
stock = {'시가':[100,200,300], '종가':[80,210,330]}

# 184
stock = {'10/10':[8,110,70,90], '10/11':[210, 230, 190,200]}

# 185
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j)

# 186
# 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(j)

# 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j)
#         print('-'*5)

# 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j, '호')
#     print('_'*5)

# 190
# for i in apart:
#     for j in i:
#         print(j, '호')
# print('-'*5)

# 191
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for i in data:
#     for j in i:
#         print(j*1.00014)

# 192
# for i in data:
#     for j in i:
#         print(j*1.00014)
#     print('-'*5)

# 193
# result = []
# for i in data:
#     for j in i:
#         result.append(j*1.00014)
# print(result)

# # 194
# for i in data:
#     l = []
#     for j in i:
#         l.append(j*1.00014)
#     result.append(l)
# print(result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     print(i[3])

# 196
# for i in ohlc[1:]:
#     if i[3] > 150:
#         print(i[3])

# 197
# for i in ohlc[1:]:
#     if i[3] >= i[0]:
#         print(i[3])

# 198
# v = []
# for i in ohlc[1:]:
#     v.append(i[1] - i[2])
# print(v)

# 199
# for i in ohlc[1:]:
#     if i[3]>i[0]:
#         print(i[1]-i[2])

# 200
sum = 0
for i in ohlc[1:]:
    sum += (i[3] - i[0])
print(sum)