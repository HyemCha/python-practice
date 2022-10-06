num1 = input('숫자1 --> ')
num2 = input("숫자2 --> ")

try:
    num1 = int(num1)
    num2 = int(num2)
except :
    print("except : 오류가 발생했습니다")
else :
    print(num1, '/', num2, '=', num1/num2)
finally:
    print('finally : 이부분은 무조건 나옴')
