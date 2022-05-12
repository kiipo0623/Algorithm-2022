D = []
answer = 0
def bt(cnt, tired, visited):
    global answer
    global L
    # 종료 조건
    if all(visited):
        answer = len(visited)
        return

    flag = False
    for i in range(L):
        if not visited[i]: # 방문처리 안되어있으면
            if tired >= D[i][0]:
                flag = True
                visited[i] = True
                bt(cnt+1, tired-D[i][1], visited)
                visited[i] = False

    if not flag:
        answer = max(answer, cnt)
        return



def solution(k, dungeons):
    global D, L, answer
    D = [a[:] for a in dungeons]
    L = len(dungeons)
    bt(0, k, [False]*L)
    return answer

print(solution(
    80, [[80,20],[50,40],[30,10]]
))