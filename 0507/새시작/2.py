def count(i, j, queue):
    ans = int(1e9)
    start, end = 0, len(queue)//2-1
    if i-start >= 0 and j-end >= 0:
        ans = min(ans, (i-start)+(j-end))
    return ans
    # 역방향 이동

def solution(queue1, queue2):
    global L
    answer = int(1e9)
    queue = queue1+queue2
    SOL = sum(queue)//2

    L = len(queue)
    start = 0
    end = start
    SUM = queue[0]
    while end<L-1 and start<=end:
        # 값 확인해보고 start/end 조절
        if SUM>SOL:
            SUM -= queue[start]
            start += 1
        elif SUM<SOL:
            end += 1
            SUM += queue[end]
        else:
            answer = min(answer, count(start, end, queue))
            end += 1
            SUM += queue[end]

    if answer == int(1e9):
        return -1
    else:
        return answer

print(solution(
 [1,2,1,2], [1, 10, 1, 2]
))