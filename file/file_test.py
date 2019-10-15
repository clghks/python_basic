# 파일 쓰기
file = open("live.txt", "w")
file.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
file.close()

# 파일 읽기
try:
    file = open("live.txt", "r")
    text = file.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    file.close()

# 파일 라인 읽기
file = open("live.txt", "r")
line = 1
while True:
    row = file.readline()
    if not row:
        break
    print(str(line) + " : " + row, end='')
    line += 1
file.close()

# 입출력 위치
file = open("live.txt", "r")
file.seek(12, 0)
text = file.read()
file.close()
print(text)


# 파일 내용 추가 하기
file = open("live.txt", "a")
file.write("\n\n푸쉬킨 형님의 말씀이었습니다.")
file.close()