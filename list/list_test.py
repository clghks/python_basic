# 성적의 합계, 평균을 구하는 예제
score = [88, 95, 70, 100, 99]
sum = 0
for s in score:
    sum += s

print("총점 :", sum)
print("평균 :", sum / len(score))

# 리스트를 자르는 예제
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])        # 2~5까지
print(nums[:4])         # 처음부터 4까지
print(nums[6:])         # 6에서 끝까지
print(nums[1:7:2])      # 1~7까지 하나씩 건너뛰며

# 리스트 값을 변경하는 예제
score = [88, 95, 70, 100, 99]
print(score[2])
score[2] = 55
print(score[2])

# 이중리스트 사용 방법 예제
lol = [ [1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lol[0])
print(lol[2][1])

for sub in lol:
    for item in sub:
        print(item, end=' ')
    print()

# 이차원 리스트로 성적을 처리하는 예제
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]

total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subjects = len(student)
    print("총점 %d, 평균 %.2f" % (sum, sum / subjects))
    total += sum
    totalsub += subjects

print("전체평균 %.2f" % (total / totalsub))


# [수식 for 변수 in 리스트 if 조건]
# 1에서 10까지 순회하며 그 2배되는 값을 리스트로 만들어 보자
nums = []
for n in range(1, 11):
    nums.append(n * 2)

print(nums)

# 1에서 10까지 순회하며 그 2배되는 값을 리스트로 만들어 보자
# 리스트 컴프리헨션
nums = [n * 2 for n in range(1, 11)]
for i in nums:
    print(i, end=', ')

print()

# 리스트에 99과 5를 추가해보자
nums = [1, 2, 3, 4]
nums.append(5)
nums.insert(2, 99)
print(nums)

# 만점 받은 학생의 수와 번호를 알아 보자
score = [88, 95, 70, 100, 99, 80, 78, 50]
perfect = score.index(100)
print("만점 받은 학생은 ", perfect, "번입니다. ")
perfect_count = score.count(100)
print("만점자 수는 ", perfect_count, "명입니다.")

# 학생 수와 최고 점수, 최저 점수를 찾아보자.
score = [88, 95, 70, 100, 99, 80, 78, 50]
print("학생 수는 %d 명 입니다." % len(score))
print("최고 점수는 %d 점 입니다." % max(score))
print("최저 점수는 %d 점 입니다." % min(score))

# 사용자에게 입력 받은 요소를 검사해보자.
# ans = input("결제 하시겠습니까? ")
# if ans in ['yes', 'y', '예', 'ok']:
#     print("결제 완료 되었습니다.")
# else:
#     print("안녕히 가세요.")


ans = input("결제 하시겠습니까? ")
if ans not in ['no', 'n', '아니오']:
   print("결제 완료 되었습니다.")
else:
   print("안녕히 가세요.")

# 성적의 순서를 정렬 해보자.
score = [88, 95, 70, 100, 99, 80, 78, 50]
score.sort()
print(score)
score.reverse()
print(score)


# 원본을 유지하고 정렬을 해보자.
score = [88, 95, 70, 100, 99, 80, 78, 50]
score_sort = sorted(score)
print(score)
print(score_sort)


# 성적 리스트의 요소를 삭제해보자
score = [88, 95, 70, 100, 99, 80, 78, 50]
score.remove(100)
print(score)
del score[2]
print(score)
score[1:4] = []
print(score)
print(score.pop())
print(score)