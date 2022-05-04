def movek(k, graph, dir):
    while True:
        if dir == 0: # 위로
            k -= 1
        else: # 아래로
            k += 1
        if k<0 or k>=len(graph):
            if dir == 0:
                dir = 1
            else:
                dir = 0
            continue
        if not graph[k]:
            continue
        return k

def move(idx, graph, dir, cnt):
    for _ in range(cnt):
        if dir == 0: #위
            idx -= 1
            while graph[idx] != True:
                idx -= 1
        if dir == 1: # 아래
            idx += 1
            while graph[idx] != True:
                idx += 1
    return idx

def mv_remove(idx, graph):
    while True:
        idx += 1
        if len(graph) == idx:
            break
        if graph[idx] == True:
            return idx

    while True:
        idx -= 1
        if graph[idx] == True:
            return idx

def solution(n, k, cmd):
    answer = ''
    graph = [True]*n
    stack = []
    mv_tmp = 0

    for c in cmd:
        if c == 'C': # 삭제인 경우
            if mv_tmp < 0:
                k = move(k, graph, 0, -mv_tmp)
            elif mv_tmp > 0:
                k = move(k, graph, 1, mv_tmp)
            mv_tmp = 0 # 초기화
            graph[k] = False
            stack.append(k)
            k = mv_remove(k, graph)
        elif c == 'Z':
            now = stack.pop()
            graph[now] = True
        else:
            A, B = c.split()
            if A == 'U':
                mv_tmp -= int(B)
            else:
                mv_tmp += int(B)

    for g in graph:
        if g:
            answer += 'O'
        else:
            answer += 'X'
    return answer


print(solution(
    8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
))