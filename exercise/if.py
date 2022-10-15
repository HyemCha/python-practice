# 101
# 102
# print(3 == 5)

# 103
# print(3 < 5)

# 104
# x = 4
# print(1 < x < 5)

# 105
# print((3 == 3) and (4 != 3))

# 106
# print(3 => 4)

# 107
# if 4 < 3 :
#     print("Hello World")

# # 108
# if 4 < 3 :
#     print("Hello World.")
# else:
#     print("Hi, there.")

# 109
# if True:
#     print("1")
#     print("2")
# else:
#     print("3")
# print("4")

# 110
# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else:
#     print("4")
# print("5")

# 111
# str = input(">>")
# print(str*2)

# 112
# i = int(input("숫자를 입력하세요:"))
# print(i + 10)

# 113
# i = int(input(">>"))
# if i%2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 114
# i = int(input(">>"))
# i += 20
# if i > 255:
#     print(255)
# else:
#     print(i)

# 115
# i = int(input(">>"))
# i -= 20
# if i<0:
#     print(0)
# elif i>255:
#     print(255)
# else:
#     print(i)

# 116
# s = input('>>')
# if s[3:] == '00':
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')

# 117
# fruit = ["사과", "포도", "홍시"]
# s = input('>>')
# if s in fruit:
#     print('정답')
# else:
#     print('오답')

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# inv = input('>>')
# if inv in warn_investment_list:
#     print('투자 경고 종목')
# else:
#     print('투자 경고 종목 아님xxxxx')

# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# s = input('>>')
# if s in fruit:
#     print('정답')
# else:
#     print('x')

# 120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# s = input('>>')
# if s in fruit.values():
#     print('o')
# else:
#     print('x')

# 121
# s = input('>>')
# if s.islower():
#     print(s.upper())
# else:
#     print(s.lower())

# 122
# score = int(input('>>'))
# if 80<score<=100:
#     print('A')
# elif 60<score<=80:
#     print('B')
# elif 40<score<=60:
#     print('C')
# elif 20<score<=40:
#     print('D')
# else:
#     print('E')

# 123
# 환율 = {"달러": 1167,
#       "엔": 1.096,
#       "유로": 1268,
#       "위안": 171}
# nm= input('>>')
# n, m = nm.split()
# n=float(n)
# # if m == '달러':
# #     print(n*1167,'원')
# # elif m == '엔':
# #     print(n*1.096, '원')
# # elif m == '유로':
# #     print(n*1268, '원')
# # elif m == '위안':
# #     print(n*171, '원')
# # else:
# #     print('잘못입력하셨습니다.')
# print(n*환율[m], '원')

# 124
# n1 = int(input('>>'))
# n2 = int(input('>>'))
# n3 = int(input('>>'))
# print(max(n1,n2,n3))

# 125
# dic = {'001':'SKT', '016': 'KT', '019':'LGU', '010':'알수없음'}
# pn = input('>')
# print('당신은', dic[pn[:3]], '사용자입니다.')

# 126
# a = '강북구'
# b = '도봉구'
# c = '노원구'
# # li = [a,a,a,b,b,b,c,c,c,c]
# pn = input('>>')
# # print(li[int(pn[2])])
# pn = pn[:3]
# if pn in ['010', '011', '012']:
#     print(a)
# elif pn in ['014', '015', '016']:
#     print(b)
# else:
#     print(c)

# 127
# id = input('>>')
# id = int(id.split('-')[1][0])
# if id==2 or id==4:
#     print('xx')
# else:
#     print('xy')

# 128
# id = input('>>')
# id = int(id.split('-')[1][1:3])
# if 0<=id<=8:
#     print('서울')
# elif 9<=id<=12:
#     print('부산')
# else:
#     print('서울 아님')

# 129
# id = input('>>')
# id = id.replace('-', '').replace('', ' ').split()
# first = (int(id[0])*2 + int(id[1])*3 + int(id[2])*4 + int(id[3])*5 + int(id[4])*6 + int(id[5])*7 + \
#         int(id[6])*8 + int(id[7])*9 + int(id[8])*2 + int(id[9])*3 + int(id[10])*4 + int(id[11])*5)%11
# se = (11 - first)
# print(first)
# if se == int(id[12]):
#     print('qualified')
# else:
#     print('not qualified')

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
max_price = float(btc['max_price'])
op = float(btc['opening_price'])
vrange = float(btc['max_price']) - float(btc['min_price'])

if op+vrange > max_price:
    print('상승장')
else:
    print('하락장')