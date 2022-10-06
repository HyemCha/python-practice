myStr = '파이썬은 재미 있어요. 파이썬만 매일매일 공부하고싶어요.~GUI'
strPosList = []
index = 0

while True:
    try:
        index = myStr.index('GUI', index)
        strPosList.append(index)
        print("index : ", index)
        index = index + 1
    except:
        break
print("파이썬 글자 위치 --> ", strPosList)
