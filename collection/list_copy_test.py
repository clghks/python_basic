list1 = [1, 2, 3]
list2 = list1

list2[1] = 100
print(list1)
print(list2)

# copy 메서드를 사용해서 리스트의 값을 변경해보자.
list1 = [1, 2, 3]
list2 = list1.copy()

list2[1] = 100
print(list1)
print(list2)

# 리스트 안에 리스트가 있는 상태에서 copy 해보기
list1 = [1, 2, 3]
list2 = [list1, 4, 5]
list3 = list2.copy()

list3[0][1] = 99
print(list1)
print(list2)
print(list3)

# 리스트 안에 리스트가 있는 상태에서 deepcopy 해보기
import copy

list1 = [1, 2, 3]
list2 = [list1, 4, 5]
list3 = copy.deepcopy(list2)

list3[0][1] = 99
print(list1)
print(list2)
print(list3)

# is 연산자를 사용해 같은 객체인지 확인해보자.
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

print("list1 == list2 :", list1 is list2)
print("list1 == list3 :", list1 is list3)
print("list2 == list3 :", list2 is list3)