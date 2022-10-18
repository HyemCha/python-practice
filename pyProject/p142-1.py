import random

a = random.randrange(1,7) + random.randrange(1,7)
b = random.randrange(1,7) + random.randrange(1,7)

if a > b:
    print('a win', a, b)
elif b > a:
    print('b win', a, b)
else:
    print('무승부', a, b)