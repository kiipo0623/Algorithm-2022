def checker(s, l):
    tmp = []
    ans = ''
    for i in range(0, len(s), l):
        tmp.append(s[i:i+l])

    before = tmp[0]
    cnt = 1
    for t in tmp[1:]:
        after = t
        if before == after:
            cnt += 1
        else:
            if cnt > 1:
                ans = ans + str(cnt) + before
            else:
                ans += before
            before = after
            cnt = 1

    if cnt>1:
        ans = ans + str(cnt) + after
    else:
        ans += after

    print(tmp)
    print(ans)

    return len(ans)


def solution(s):
    answer = int(1e9)
    for i in range(1, len(s)//2+1):
        answer = min(answer, checker(s, i))

    return answer

# print(solution("aabbaccc"))
print(solution(
"ab"
))