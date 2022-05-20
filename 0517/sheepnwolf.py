answer = 0
def bt(visited, sheep, wolf, info):
    global answer, tree
    answer = max(answer, sheep)

    for node in visited:
        for newnode in tree[node]:
            if newnode not in visited:
                if info[newnode] == 0:
                    visited.append(newnode)
                    bt(visited, sheep+1, wolf, info)
                    visited.pop()

                elif info[newnode] == 1:
                    if sheep > wolf+1:
                        visited.append(newnode)
                        bt(visited, sheep, wolf+1, info)
                        visited.pop()
                    else:
                        continue


def solution(info, edges):
    global answer, tree
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        parent, son = edge
        tree[parent].append(son)
    bt([0], 1, 0, info)

    return answer

print(solution(
[0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
))

print(solution(
[0,1,0,1,1,0,1,0,0,1,0],
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
))