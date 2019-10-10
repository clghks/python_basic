
# 일련의 문자를 따옴표(“, ‘)로 감싸 나열해 놓은 것이다.
print("Hello World!")
a = "Hello World!"
print(a)

print('Hello World!')
a = 'Hello World!'
print(a)


# 따옴표(“, ‘) 잘 못 사용한 예
# print("Hello World!')           # SyntaxError
# print('Hello World!")           # SyntaxError
#
# print("I Say "Help" to you")    # SyntaxError
# print('I Say 'Help' to you')    # SyntaxError
#
# print("Let's go")


# 따옴표를 같이 사용 하는 방법
print("I Say \"Help\" to you")
print('I Say \'Help\' to you')

print("Let's go")


# 확장열 사용 예제
print("first\nsecond")
print("old\nnew")

print("c:\temp\new.text")       # 예상 결과가 다름
print("c:\\temp\\new.text")
print(r"c:\temp\new.text")      # 확장열을 적용하지 않음

# 긴 문자열
s = """강나루 건너서 밀받 길을 구름에 달 가듯이 가는 나그네
길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀 
구름에 달 가듯이 가는 나그네"""
print(s)

# 긴 문자열 개행 방지
s = """강나루 건너서 밀받 길을 구름에 달 가듯이 가는 나그네 \
길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀 \
구름에 달 가듯이 가는 나그네"""
print(s)


# 문자열 합치기
s = "korea" "japan" "2002"
print(s)

s = (
    "korea"
    "japan"
    "2002"
)
print(s)
