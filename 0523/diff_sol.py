def solution(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_lst = [()] # 현재까지 고칠 수 있는 취약점
    count = 0
    dist.sort(reverse=True)

    # 고칠 수 있는 것들 리스트
    for can_move in dist:
        repairs = [] # 친구별 고칠 수 있는 취약점
        count += 1

        for i, wp in enumerate(weak):
            start = wp # 각 위크포인트부터 시작
            ends = weak[i:] + [n+w for w in weak[:i]]
            can = [end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))

        cand = set()
        for r in repairs: # 새친구의 수리가능 지점
            for x in repair_lst: # 기존 수리가능 지점
                new = r | set(x)
                if len(new) == W: # 모두 수리가능한 경우 친구수
                    return count
                cand.add(tuple(new))
        repair_lst = cand
    return -1

print(solution(
    12, [1,5,6,10],[1,2,3,4]
))