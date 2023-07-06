# https://school.programmers.co.kr/learn/courses/30/lessons/181949

str = input()
for s in str:
    if s.isupper():
        print(s.lower(), end = '')
    else:
        print(s.upper(), end = '')