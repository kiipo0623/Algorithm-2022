def solution(a, b, g, s, w, t):
    answer = float('inf')
    start = 0
    end = 10 ** 9 * 10 ** 5 * 4 - 10 ** 5

    while start <= end:
        mid = (start + end) // 2
        gM, gm, sM, sm = 0, 0, 0, 0

        for i in range(len(t)):
            c = (mid - t[i]) // (2 * t[i]) + 1
            # g[i]-c*w[i] 시간 내내 운반해도 다 운반 못할때
            gM += g[i] if g[i] - c * w[i] <= 0 else c * w[i]
            # 다 운반 못하면 남은값 다하면 0
            # s[i]를 min에 집어넣는 이유 : g에서 아무것도 안옮긴 경우 커버
            sm += min(s[i], abs(g[i] - c * w[i])) if g[i] - c * w[i] <= 0 else 0
            sM += s[i] if s[i] - c * w[i] <= 0 else c * w[i]
            gm += min(g[i], abs(s[i] - c * w[i])) if s[i] - c * w[i] <= 0 else 0

        if gM >= a and sM >= b and gM + sm >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer

print(solution(10, 10, [100], [100], [7], [10]))  # 50