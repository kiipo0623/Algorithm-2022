from collections import defaultdict
def bt(cnt, fin, attend, team_check, sales):
    global visit, answer
    if cnt == fin:
        attend = tuple(sorted(list(set(attend))))
        print(attend)
        if attend in visit: #이미 방문
            return
        else: # 점수 확인
            sum_ = 0
            for a in attend:
                sum_ += sales[a-1]
            answer = min(answer, sum_)
            visit.add(attend)
            return

    for team in team_check:
        if not team_check[team]:
            for p in team_candidate[team]:
                attend.append(p)
                team_check[team] = True
                bt(cnt+1, fin, attend, team_check, sales)
                attend.pop()
                team_check[team] = False

def solution(sales, links):
    global team_candidate, visit, answer

    INF = int(1e9)
    N = len(sales)+1 # 1부터 시작했을 떄 사람수

    answer = INF

    team_tree = defaultdict(set) # 팀 관리
    person_tree = defaultdict(set) # 사람 관리
    team_min = [INF]*(N)
    team_double_cand = [[] for _ in range(N)]
    team_min_cand = [0] * N

    team_candidate = defaultdict(set) # 갈 사람 예비 후보

    for a, b in links:
        team_tree[a].add(b)
        team_tree[a].add(a)
        person_tree[a].add(a)
        person_tree[b].add(a)

    # 후보자 간택 : 시간초과 시 수정
    for i in range(1, N):
        # 두개 이상 포함되는 애
        if len(person_tree[i]) > 1:
            for team in person_tree[i]:
                team_double_cand[team].append(i)
                if sales[i-1] <= team_min[team]:
                    team_min[team] = sales[i-1]
                    team_min_cand[team] = i
        # 최솟값인 애 : 등호 제외
        else:
            team = list(person_tree[i])[0]
            if sales[i-1] < team_min[team]:
                team_min[team] = sales[i-1]
                team_min_cand[team] = i

    print(team_tree)
    print(person_tree)
    print(team_min)
    print(team_double_cand)
    print(team_min_cand)

    team_candidate = defaultdict(set)  # 갈 사람 예비 후보

    team_list = team_tree.keys()
    for team in team_list:
        team_candidate[team] = set(team_double_cand[team])
        team_candidate[team].add(team_min_cand[team])

    print(team_candidate)

    # 한명씩 골라서 최솟값 갱신하면서 visit cache 관리
    visit = set()
    check = dict()
    for t in team_list:
        check[t] = False
    bt(0, len(team_list), [], check, sales)

    return answer

# print(solution(
# [14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
# ))
print(solution(
[5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]
))
print(solution(
[10, 10, 1, 1],[[3,2], [4,3], [1,4]]
))