def combination(lst, N):
    candidate = []

    def generate(select, cnt):
        if cnt == N:
            candidate.append(select[:])
            return

        start = lst.index(select[-1]) + 1 if select else 0
        for i in range(start, len(lst)):
            select.append(lst[i])
            generate(select, cnt + 1)
            select.pop()

    generate([], 0)
    return candidate

def getgrade(team_people):
    grade = 0
    two_people = combination(team_people, 2)
    for a, b in two_people:
        grade += board[a][b]
        grade += board[b][a]
    return grade

def getgrade2(team_people):
    grade = 0
    for i in team_people:
        for j in team_people:
            grade += board[i][j]
    return grade

N = int(input())
board = []
min_value = int(1e9)

lst = [i for i in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

team_candidate = combination(lst, N//2)
did_check = []

for combi_cand in team_candidate:
    if combi_cand in did_check:
        continue

    diff_team = []
    for i in range(N):
        if i not in combi_cand:
            diff_team.append(i)
    did_check.append(diff_team)

    start = getgrade2(combi_cand)
    ink = getgrade2(diff_team)
    min_value = min(min_value, abs(start-ink))

print(min_value)