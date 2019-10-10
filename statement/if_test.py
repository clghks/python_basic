# if 조건문
age = 10
if age < 19:
    print("애들은 가라")

# 비교 연산자
a = 3
if a == 3:
    print("3 이다.")

if a > 5:
    print("5 보다 크다.")

if a < 5:
    print("5 보다 작다.")


# 문자열 비교 연산
country = "korea"
if country == "korea":
    print("한국 입니다.")
if country == "Korea":
    print("대한민국 입니다.")

if "korea" > "japan":
    print("한국이 더 크다.")
if "korea" < "japan":
    print("일본이 더 크다.")


# 논리 연산자
# and, or 예제 실습
a = 3
b = 4
if a == 3 and b == 4:
    print("AND OK")
if a == 3 and b == 8:
    print("AND OK")
if a == 3 or b == 8:
    print("OR OK")

# 블록 구조
age = 16
if age < 19:
    print("애들은 가라")
    print("공부 열심히 해야지")

# 블록 구조가 다른 경우
age = 22
if age < 19:
    print("애들은 가라")
print("공부 열심히 해야지")


# else 문
age = 22
if age < 19:
    print("애들은 가라")
else:
    print("어서 옵쇼")

# else 문 블록 구조
age = 22
if age < 19:
    print("애들은 가라")
    print("공부 열심히 해야지")
else:
    print("어서 옵쇼")
    print("즐거운 시간 되세요")


# elif 문
age = 22
if age < 19:
    print("애들은 가라")
elif age < 25:
    print("대학생입니다.")
else:
    print("어서 옵쇼")


# elif 문 예제
money = 6500
if money >= 20000:
    print("탕수육을 먹는다.")
elif money >= 10000:
    print("쟁반 짜장을 먹는다.")
elif money >= 6000:
    print("짬뽕을 먹는다.")
elif money >= 4000:
    print("짜장면을 먹는다.")
else:
    print("단무지를 먹는다.")

# if문 중첩
men = True
age = 22
if men == True:
    if age > 19:
        print("성인 남자입니다. ")
    else:
        print("소년 입니다. ")

