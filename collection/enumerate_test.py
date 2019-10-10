# 학생의 순서와 점수을 출력 해보자
score = [88, 95, 70, 100, 99]
no = 1
for s in score:
    print(no, "번 학생의 성적 :", s)
    no += 1


for no in range(len(score)):
    print(no + 1, "번 학생의 성적 :", score[no])

# enumerate 를 사용해서 학생의 순서와 점수를 출력 해보자
for no, s in enumerate(score, 1):
    print(no, "번 학생의 성적 :", s)
