def solution(s):
    answer = ''
    change = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',
              'eight':'8', 'nine':'9'}
    while s:
        if s[0] in '0123456789':
            answer += s[0]
            s = s[1:]
        else:
            if s[:3] in change.keys():
                answer += change[s[:3]]
                s = s[3:]
            elif s[:4] in change.keys():
                answer += change[s[:4]]
                s = s[4:]
            elif s[:5] in change.keys():
                answer += change[s[:5]]
                s = s[5:]
    return int(answer)

print(solution(
"one4seveneight"
))