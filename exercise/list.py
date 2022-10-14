## 리스트 : 여러 개의 값을 저장하기 위한 자료형
# 051
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# 052
movie_rank.append('베트맨')
print(movie_rank)

# 053
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 054
#movie_rank.remove('럭키')
del movie_rank[3]
print(movie_rank)

# 055
## del movie_rank[2:4]
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 056
lang1 = ['c', 'c++', 'java']
lang2 = ['python', 'go', 'c#']
langs = lang1 + lang2
print(langs)

# 057
nums = [1,2,3,4,5,6,7]
print("max:", max(nums))
print("min:", min(nums))

# 058
nums = [1,2,3,4,5]
print(sum(nums))

# 059
cook = ['피자', '김밥', '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
nums = [1,2,3,4,5]
print(sum(nums)/len(nums))

# 061
price = ['201880728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 063
print(nums[1::2])

# 064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 067 문자열의 join 메서드를 사용하면 리스트를 문자열로 붙일 수 있습니다.
print("/".join(interest))

# 068
print("\n".join(interest))

# 069
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 070
data = [2,4,3,1,5,10,9]
#data.sort()
data = sorted(data)
print(data)