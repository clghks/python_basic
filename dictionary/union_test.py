# 집합에 추가, 삭제, 결합을 사용해보자
asia = {"korea", "china", "japan"}
asia.add("vietnam")
asia.add("china")       # 추가 안됨
asia.remove("japan")
print(asia)

asia.update({'singapore', 'hongkong', 'korea'})
print(asia)
print()
print()
print()


# 합집합, 교집합, 차집합, 배타적 차집합 사용해보자
twox = {2, 4, 6, 8, 10, 12}
threex = {3, 6, 9, 12, 15}

print("교집합", twox & threex)
print("합집합", twox | threex)
print("차집합", twox - threex)
print("차집합", threex - twox)
print("배타적 차집합", twox ^ threex)


print()
print()
print()

# 부분 집합을 사용해보자
mammal = {"코끼리", "고릴라", "사자", "고래", "사람", "원숭이", "개"}
primate = {"사람", "원숭이", "고릴라"}

if "사자" in mammal:
    print("사자는 포유류이다.")
else:
    print("사자는 포유류가 아니다.")

print(primate <= mammal)
print(primate < mammal)
print(primate <= primate)
print(primate < primate)