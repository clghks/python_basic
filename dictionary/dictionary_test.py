# 사전 키를 사용해 값을 불러오는 예제
dic = {"boy": "소년", "school": "학교", "book": "책"}
print(dic["boy"])
# print(dic["student"])       # KeyError

print(dic.get("boy"))
print(dic.get("student"))
print(dic.get("student", "사전에 없는 단어입니다."))

# in, not in 사용하여 사전에 단어가 있는지 알아보자.
dic = {"boy": "소년", "school": "학교", "book": "책"}
if "student" in dic:
    print("사전에 있는 단어입니다.")
else:
    print("사전에 없는 단어입니다.")

if "boy" not in dic:
    print("사전에 없는 단어입니다.")
else:
    print("사전에 있는 단어입니다.")

# 사전에 값을 변경해보자.
dic = {"boy": "소년", "school": "학교", "book": "책"}
dic["boy"] = "남자애"
dic["girl"] = "여자애"
print(dic)
del dic['book']
print(dic)

# 키와 값을 가져와 보자
dic = {"boy": "소년", "school": "학교", "book": "책"}
print(dic.keys())
print(dic.values())
print(dic.items())


# 두개의 사전을 병합해보자.
dic = {"boy": "소년", "school": "학교", "book": "책"}
dic2 = {"student": "학생", "teacher": "선생님", "book": "서적"}
dic.update(dic2)
print(dic)


# 팝송 가사에 등장하는 알파벳 문자의 출현 횟수를 세어 보자.
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
new how shall we sing the lord's song in a strange land
"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c in alphabet:
        alphabet[c] += 1
    else:
        alphabet[c] = 1

print(alphabet)

# 알파벳 문자수를 정렬해서 값을 확인해보자.
key = list(alphabet.keys())
key.sort()
for c in key:
    print(c, "=>", alphabet[c])

