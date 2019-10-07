# -*- coding: utf-8 -*-

# # 2.x 버전에서 사용 가능
print "Hello World!"
print("Hello World!")
print 'Hello World!'
print('Hello World!')

# # 3.x 버전에서는 오류
print 'Hello World!'    # SyntaxError
print('Hello World!')
print "Hello World!"    # SyntaxError
print("Hello World!")



# 2.x 버전에서 형변환
print(1/2)          # 1
print(type(1/2))    # <type 'int'>

# 3.x 버전에서 형변환
print(1/2)          # 0.5
print(type(1/2))    # <class 'float'>



# 2.x 버전에 인코딩
print(type("Hello World!"))     # <class 'str'>
print(type(u"Hello World!"))    # <class 'unicode'>
print("안녕하세요.")               # SyntaxError: Non-ASCII

# 3.x 버전에 인코딩
print(type("Hello World!"))     # <class 'str'>
print(type(u"Hello World!"))    # <class 'str'>
print("안녕하세요.")