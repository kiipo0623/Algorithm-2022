def solution(a, b, g, s, w, t):
    start, end = 0, int(1e9*1e5*2*2)
    answer = end

    while start <= end:
        mid = (start + end)//2
        all_gold, all_silver, all_total = 0, 0, 0
        for i in range(len(g)):
            now_gold, now_silver, now_total, now_time = g[i], s[i], w[i], t[i]
            if mid//now_time%2 == 1: #전체시간에서 나누어떨어지지 않으면 ? 출발만 할 수 있다
                count = (mid//now_time//2)+1
            else:
                count = (mid//now_time//2)

            all_gold += now_gold if (now_gold < now_total*count) else now_total*count
            all_silver += now_silver if (now_silver < now_total * count) else now_total*count
            all_total += now_gold + now_silver if (now_gold + now_time < now_total * count) else now_total*count

        if all_gold >= a and all_silver >= b and all_total >= a+b:
            answer = min(answer, mid)
            end = mid-1
        else:
            start = mid+1
        return answer