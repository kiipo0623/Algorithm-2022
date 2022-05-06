def solution(gems):
    minlen, minidx = int(1e9), [-1, -1]
    kind = set(gems)
    K = len(kind)
    start, end = 0, K

    # 하나씩 체크해서 시간 단축해야 하는건지 ?
    while True:
        if minlen == K: #이미 최선을 구했는 경우
            break

        if end == len(gems)+1: # 끝까지 탐색한 경우
            break

        if len(set(gems[start:end])) != K: # 범위 내
            end += 1

        else: # 성공한 경우
            while True:
                if start == end:
                    end = start+K
                    break

                if len(set(gems[start+1:end])) == K: # 더 갈수 있으면
                    start += 1

                else: # 이게 최선
                    if end-start < minlen:
                        minlen = end-start
                        minidx = [start, end-1]
                    start += 1
                    break

    minidx[0], minidx[1] = minidx[0]+1, minidx[1]+1
    # 마지막에 1씩 뺴주기
    return minidx

print(solution(
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
))
print(solution(
["AA", "AB", "AC", "AA", "AC"]
))