from collections import defaultdict
def bt(cnt, sum_, fin, attend, team_check, sales):
    global visit, answer
    if cnt == fin:
        print(attend)
        answer = min(answer, sum_)

    for team in team_check:
        if not team_check[team]:
            for p in team_candidate[team]:
                if p in attend:
                    team_check[team] = True
                    bt(cnt+1, sum_, fin, attend, team_check, sales)
                    team_check[team] = False
                else:
                    attend.append(p)
                    team_check[team] = True
                    bt(cnt+1, sum_ + sales[p-1], fin, attend, team_check, sales)
                    attend.pop()
                    team_check[team] = False

def solution(sales, links):
    global team_candidate, visit, answer

    INF = int(1e9)
    N = len(sales)+1 # 1부터 시작했을 떄 사람수
    answer = INF

    team_tree = defaultdict(list) # 팀 관리
    person_tree = defaultdict(set) # 사람 관리
    team_min = [INF]*(N)
    team_double_cand = [[] for _ in range(N)]
    team_min_cand = [0] * N

    team_candidate = defaultdict(set) # 갈 사람 예비 후보

    # 후보자 간택까지 진행
    for a, b in links:
        team_tree[a].append(b)
        person_tree[a].add(a)
        person_tree[b].add(a)

        # 두 개 이상 포함(팀장)
        if a != 1:
            team_double_cand[a].append(a)
            if sales[a-1] <= team_min[a]:
                team_min[a] = sales[a-1]
                team_min_cand[a] = a
        else:
            if sales[a-1] < team_min[a]:
                team_min[a] = sales[a-1]
                team_min_cand[a] = a

        if sales[b-1] < team_min[a]:
            team_min[a] = sales[b-1]
            team_min_cand[a] = b

    team_list = team_tree.keys()

    for team in team_list:
        team_candidate[team] = set(team_double_cand[team])
        team_candidate[team].add(team_min_cand[team])

    # 한명씩 골라서 최솟값 갱신하면서 visit cache 관리
    check = dict()
    for t in team_list:
        check[t] = False
    print(team_candidate)
    bt(0, 0, len(team_list), [], check, sales)

    return answer

# print(solution(
# [14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
# ))
print(solution(
[5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]
))
