print('%d / %d = %d' % (5,10,5/10))
print("%5s" % "CookBook56565")
print("%2.1f" % 123.45)
print(type(4))
hex_num = hex(0xbc614)
print((hex_num))

def check(n):
    if 'A' <= n <= 'f':
        print("16진수")
        return;
    n = int(n)
    if 0 <= n <= 1:
        print("2진수 또는 8진수 또는 10진수 또는 16진수")
    elif n<= 8:
        print("8진수 또는 10진수 또는 16진수")
    elif n <= 9:
        print("10진수 또는 16진수")
    else:
        print("잘못 입력")


n = input('>>')
check(n)

