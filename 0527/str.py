def solution(s):
    answer = s
    for i in range(1, len(s)//2+1):
        tmp = ''
        before = ''
        cnt = 0
        for idx in range(0, len(s), i):
            if before == s[idx:idx+i]: # 같으면
                cnt += 1
            else: # 다르면
                if cnt > 1:
                    tmp += str(cnt)+before
                else:
                    tmp += before
                before = s[idx:idx+i]
                cnt = 1

        # 마지막 경우 처리
        if cnt > 1:
            tmp += str(cnt)+before
        else:
            tmp += before
        print(tmp)
        if len(tmp) < len(answer):
            answer = tmp
    return len(answer)

print(solution(
"aabbaccc"
))
print(solution(
"ababcdcdababcdcd"
))
