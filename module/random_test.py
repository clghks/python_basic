# import random
#
# for i in range(5):
#     print(random.random())
#
# for i in range(5):
#     print(random.randint(1, 10))

import random

a = random.randint(1, 9)
b = random.randint(1, 9)
question = "%d + %d = ?" % (a, b)
c = int(input(question))

if c == a + b:
    print("정답입니다.")
else:
    print("틀렸습닏.")
