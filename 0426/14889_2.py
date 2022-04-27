def getgrade2(team_people):
    grade = 0
    for i in team_people:
        for j in team_people:
            grade += board[i][j]
    return grade

def getother(combi_cand):
    diff_team = []
    for i in range(N):
        if i not in combi_cand:
            diff_team.append(i)
    return diff_team

def combination(lst, N):
    def generate(select, cnt):
        global did, min_value
        if cnt == N:
            # 우리팀 점수
            if tuple(select) not in did:
                start = getgrade2(select)
                # 상대팀
                diff = getother(select)
                ink = getgrade2(diff)
                did.add(tuple(select))
                did.add(tuple(diff))

                min_value = min(min_value, abs(start - ink))
            else:
                return

        start = lst.index(select[-1]) + 1 if select else 0
        for i in range(start, len(lst)):
            select.append(lst[i])
            generate(select, cnt + 1)
            select.pop()

    generate([], 0)

N = int(input())
board = []
min_value = int(1e9)
did = set()

lst = [i for i in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

team_candidate = combination(lst, N//2)
print(min_value)