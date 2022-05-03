from collections import defaultdict
def bt(visited, candidate, sheep, wolf, info):
    # 더이상 방문할 곳 없으면 리턴, 최고값 갱신
    global graph, answer
    flag = False
    # 다른 곳 방문
    for c in candidate:
        if info[c] == 0:
            visited.append(c)
            candidate.remove(c)
            cnt = 0
            for item in graph[c]:
                candidate.append(item)
                cnt = cnt+1
            bt(visited, candidate, sheep+1, wolf, info)
            visited.pop()
            for _ in range(cnt):
                candidate.pop()
            candidate.append(c)

        else: # 늑대인 경우
            if wolf+1 < sheep: # 여력 있음
                visited.append(c)
                candidate.remove(c)
                cnt = 0
                for item in graph[c]:
                    candidate.append(item)
                    cnt = cnt+1
                bt(visited, candidate, sheep, wolf+1, info)
                visited.pop()
                for _ in range(cnt):
                    candidate.pop()
                candidate.append(c)

            else: # 잡아 먹음 : 종료
                print("max 갱신", sheep)
                print(visited)
                answer = max(answer, sheep)
                return




def solution(info, edges):
    global answer, graph
    answer = 0
    graph = defaultdict(list)
    for p, s in edges:
        graph[p].append(s)
    print(graph)
    bt([0], graph[0], 1, 0, info)
    return answer
#
print(solution(
[0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
))

# print(solution(
# [0,1,0,1,1,0,1,0,0,1,0],
# [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
# ))