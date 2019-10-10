# 60점 이하인 점수만 출력해보자.
def flunk(s):
    return s < 60

score = [45, 89, 72, 53, 94]
for s in filter(flunk, score):
    print(s)

# 람다를 사용하여 60점 이하인 점수만 출력해보자.
score = [45, 89, 72, 53, 94]
for s in filter(lambda x: x < 60, score):
    print(s)

# 점수를 절반으로 나누어 출력해보자.
def half(s):
    return s / 2

score = [45, 89, 72, 53, 94]
for s in map(half, score):
    print(s)

# 람다를 사용하여 점수를 절반으로 나누어 출력해보자.
score = [45, 89, 72, 53, 94]
for s in map(lambda x: x /2, score):
    print(s)