def solution(n):
    dp = [set() for _ in range(n+1)]
    dp[1].add('()')
    for i in range(2, n+1):
        for item in dp[i-1]:
            dp[i].add('('+item+')')
            dp[i].add('()'+item)
            dp[i].add(item+'()')

    return len(dp[n])

print(solution(4))