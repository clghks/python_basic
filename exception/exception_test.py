# try:
#     실행할 명령
# except 예외 as 변수:
#     오류 처리문
# else:
#     예외가 발생하지 않을 때의 처리

# 89점 예외를 처리 해보자
str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생했습니다.")
print("작업 완료")


# 예외의 종류에 따라 적절한 처리를 해보자
str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자의 범위를 벗어났습니다.")
print("작업완료")

# 1 ~ n 합계를 구하는 함수에서 0보다 큰 인수를 받아야 한다.
def calcsum(n):
    if n < 0:
        raise ValueError
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

try:
    print("~10 =", calcsum(10))
    print("~5 =", calcsum(-5))
except ValueError:
    print("입력값이 잘못되었습니다.")


# 네트워크 사용 후 자원을 종료 해보자
try:
    print("네트워크 접속")
    a = 2 / 0
    print("네트워크 통신 수행")
finally:
    print("접속 해제")
print("작업 완료")