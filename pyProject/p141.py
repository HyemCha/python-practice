# 랜덤하게 1~20까지의 숫자를 20개 채운 후에, 뽑힌 숫자 목록을 추출하는 코드를 작성

import random

l = []
for i in range(20):
    l.append(int(random.random()*20+1))
print('생성된 리스트는', l)

for i in range(1,21):
    if i in l:
        print(i, '는 리스트에 있습니다')