from collections import deque


def solution(s):
    answer = ''
    s = deque(list(s))
    flag = True

    while s:
        now = s.popleft()
        if flag:
            if now.isdigit():
                flag = False
                answer += now
            elif now.isupper():
                flag = False
                answer += now
            elif now.islower():
                flag = False
                answer += now.upper()
            else:
                answer += now
        else:
            if now == ' ':
                flag = True
                answer += now
            elif now.isupper():
                answer += now.lower()
            else:
                answer += now
    return answer

print(solution("3people unFollowed me"))