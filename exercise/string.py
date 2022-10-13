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

# 032
print("Hi" * 3)