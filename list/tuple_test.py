# 튜플로 정의한 점수의 평균과 총점을 구해보자.
score = (88, 95, 70, 100, 99)
sum = 0
for s in score:
    sum += s

print("총점 :", sum)
print("평균 :", sum / len(score))

# () 괄호 없이 튜플 정의해보기
score = 88, 95, 70, 100, 99
sum = 0
for s in score:
    sum += s

print("총점 :", sum)
print("평균 :", sum / len(score))

# 요소가 하나인 튜플
tuple_value = 2,
value = 2
print(tuple_value)      # (2,)
print(value)            # 1


# 튜플로 가능한 일
tuple_value = 1, 2, 3, 4, 5
print(tuple_value[3])
print(tuple_value[1:4])
print(tuple_value[:4])
print(tuple_value)
print(tuple_value + (6, 7))
print(tuple_value * 2)
print(tuple_value)
tuple_value[1] = 100    # TypeError
del tuple_value[1]      # TypeError


# 튜플 언패킹
member = ("이순신", "김유신", "강감찬")
lee, kim, kang = member
print(lee)
print(kim)
print(kang)

# 리스트를 튜플로 튜플을 리스트로 변경하는 예제
score = [88, 95, 70, 100, 99]
tu = tuple(score)
print(tu)

li = list(tu)
li[0] = 100
print(li)
