# 201
def print_coin():
    print('비트ㅗ인')

# 202
print_coin()

# 203
# for i in range(100):
#     print_coin()

# 204 "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    for i in range(100):
        print('비트코인')

# 205 아래의 에러가 발생하는 이유에 대해 설명하라. : 함수가 정의되기 전에 호출되어서
# hello()
# def hello():
#     print("Hi")

# 206
# def message() :
#     print("A")
#     print("B")
#
# message()
# print("C")
# message()

# 215
def print_with_smile(s):
    print(s+':D')

# 216
print_with_smile('안녕하세요')

# 217
def print_upper_price(current_price):
    print(current_price*1.3)

# 218
def print_sum(a,b):
    print(a + b)

# 219
def print_arithmetic_operation(a, b):
    print(a, '+', b, '=', a + b)
    print(a, '-', b, '=', a - b)
    print(a, '*', b, '=', a * b)
    print(a, '/', b, '=', a / b)

# 220
def print_max(a, b, c):
    print(max(a,b,c))

# 221
def print_reverse(s):
    print(s[::-1])

# 222
def print_score(l):
    print(sum(l)/len(l))

# 223
def print_even(l):
    for i in l:
        if i%2 == 0:
            print(i)

# 224
def print_keys(d):
    for i in d.keys():
        print(i)

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(d, s):
    print(d[s])

# 226
def print_5xn(s):
    for i in range(0,len(s),5):
        print(s[i:i+5])
print_5xn("아이엠어보이유알")

# 227
def print_mxn(s, n):
    for i in range(0, len(s), n):
        print(s[i:i+n])
print_mxn("아이엠어보이유알어걸", 3)

# 232
def make_url(s):
    url = ('www'+s+'.com')
    return url

# 233
def make_list(s):
    l = []
    for i in s:
        l.append(i)
    return l

# 234
def pickup_even(l):
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
    return even

# 235
def convert_int(s):
    return int(s.replace(',', ''))