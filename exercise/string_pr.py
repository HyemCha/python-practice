# 021 인덱싱(indexing) : 파이썬 문자열에서 한 글자를 가져오는 것
letters = 'python'
print(letters[0], letters[2])

print("=" * 10)
# 022 슬라이싱(slicing) : 문자열에서 여러 글자를 가져오는 것 [시작 인덱스:끝 인덱스:오프셋]
# 오프셋:동일 오브젝트 안에서 오브젝트 처음 주어진 요소나 지점까지의 변위차를 나타내는 정수형형# 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미,
# 시작 인덱스를 생략하면 0으로 간주, 끝 인덱스 생략하면 문자열의 끝을 의미
license_plate = "24가 2210"
print(license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4], sep="")
print(string[::2])

# 024
string = "PYTHON"
print(string[::-1])

# 025
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 026
print(phone_number.replace("-", ""))

# 027
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# 028
lang = 'python'
#lang[0] = 'P'
print(lang)

# 029
string = 'abcdef2a354a32a'
print(string.replace('a', 'A'))

# 030 문자열은 변경할 수 없는 자료형이므로 replace 메서드를 사용하면 원본은 그대로 둔 채로 변경된 새로운 문자열 객체를 리턴해줌
string = 'abcd'
string.replace('b', 'B')
print(string)

# 031
a = "3"
b = "4"
print(a+b)

# 032 문자열의 곱셈은 문자열의 반복을 의미한다.
print("Hi" * 3)

# 033
print('-' * 80)

# 034
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 3)

# 035
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print('이름 : %s 나이 : %d' % (name1, age1))
print('이름 : %s 나이 : %d' % (name2, age2))

# 036
print('이름 : {} 나이 : {}' .format(name1, age1))
print('이름 : {} 나이 : {}' .format(name2, age2))

# 037
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 038
상장주식주 = "5,9494,782,550"
상장주식주 = int(상장주식주.replace(",",""))
print(상장주식주, type(상장주식주))

# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040
data = "   삼성전자    "
print(data.strip())

# 041
ticker = "btc_krw"
ticker1 = (ticker.upper())

# 042
ticker2 = ticker1.lower()
print(ticker2)

# 043
a = "hello"
a = a.capitalize()
print(a)

# 044
file_name = "보고서.xlsx"
print(file_name.endswith('.xlsx'))

# 045
print(file_name.endswith(("xlsx","xls")))

# 046
file_name = "2020_" + file_name
print(file_name.startswith("2020"))

# 047
a = "hello world"
s = a.split()
print(s[0])

# 048
t=ticker.split('_')
print(t)

# 049
data = "2020_05_01"
data = data.split('_')
year = data[0]
month = data[1]
day = data[2]
print(year, month, day)

# 050 rstrip() : data가 오른쪽 공백이 제거된 반환된 새로운 문자열 객체와 바인딩 기존의 문자열은 메모리에서 자동으로 삭제됨
data = " 039490     "
print(data.rstrip()+'1')