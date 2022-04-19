# 두 팀으로 나눔 idx : 몇번째 까지 확인했는지 depth : 몇개 T인지
def split_team(check, idx, depth, fin):
    global team
    if depth == fin:
        temp = []
        for idx, sol in enumerate(check):
            if sol:
                temp.append(idx)
        team.append(temp)
        return
    if idx == len(check):
        return

    check[idx] = True
    split_team(check, idx+1, depth+1, fin)
    check[idx] = False
    split_team(check, idx+1, depth, fin)

def make_team(team):
    ret = []
    for t in team:
        another_t= []
        for i in range(N):
            if i not in t:
                another_t.append(i)
        ret.append((tuple(t), tuple(another_t)))
    print(list(set(ret)))

def check_sum(p1, p2):
    sum_ = 0
    sum_ += persons[p1][p2]
    sum_ += persons[p2][p1]
    return sum_

# nC2 구하는 함수
# teamperson : 선택된 사람들 idx , combi : 전체 조합
def Ateam_combi(teamperson, idx, candiperson):
    global Ateam
    if len(teamperson) == 2:
        Ateam.append(teamperson[:])
    if idx == len(candiperson):
        return

    teamperson.append(candiperson[idx])
    Ateam_combi(teamperson, idx+1, candiperson)
    teamperson.remove(candiperson[idx])
    Ateam_combi(teamperson, idx+1, candiperson)

def Bteam_combi(teamperson, idx, candiperson):
    global Bteam
    if len(teamperson) == 2:
        Bteam.append(teamperson[:])
    if idx == len(candiperson):
        return

    teamperson.append(candiperson[idx])
    Bteam_combi(teamperson, idx+1, candiperson)
    teamperson.remove(candiperson[idx])
    Bteam_combi(teamperson, idx+1, candiperson)


N = int(input())
persons = []
for _ in range(N):
    persons.append(list(map(int, input().split())))

ck = [False] * N
team = []
split_team(ck, 0, 0, int(N/2))
new_team = make_team(team)
print(new_team)


# answer = int(1e9)
#
# for teamA in team:
#     teamB = []
#     for i in range(N):
#         if i not in teamA:
#             teamB.append(i)
#
#     Ateam = []
#     Bteam = []
#
#     Ateam_combi([], 0, teamA)
#     Bteam_combi([], 0, teamB)
#
#     asum, bsum = 0, 0
#     for a in Ateam:
#         asum += check_sum(a[0], a[1])
#     for b in Bteam:
#         bsum += check_sum(b[0],b[1])
#
#     answer = min(answer, abs(asum-bsum))
# print(answer)