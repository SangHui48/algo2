# https://school.programmers.co.kr/learn/courses/30/lessons/12918

# 참고: https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EB%AC%B8%EC%9E%90%EC%88%AB%EC%9E%90%EC%9D%B8%EC%A7%80-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0isalpha-isdigit-isalnum
def solution(s):
    answer = False
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    return answer