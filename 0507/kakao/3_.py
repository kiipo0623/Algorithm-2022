def checkout(row, col):
    if row<0 or col<0 or row>=151 or col>=151:
        return True
    return False

def solution(alp, cop, problems):
    time = [[0]*(151) for _ in range(151)]
    MAX_ALP, MAX_COP = 0, 0

    for p in problems:
        if p[0] > MAX_ALP:
            MAX_ALP = p[0]
        if p[1] > MAX_COP:
            MAX_COP = p[1]

    for i in range(151):
        for j in range(151):
            if checkout(alp+i,cop+j):
                continue
            time[alp+i][cop+j] = i+j
    print(time)

    for a in range(alp, 151):
        for c in range(cop, 151):
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if (a-alp_rwd >= alp_req and c - cop_rwd >= cop_req) and (a-alp_rwd>=alp and c-cop_rwd>=cop):
                    time[a][c] = min(time[a][c], time[a-alp_rwd][c-cop_rwd]+cost)
                    for dx, dy in [(0, 1), (1, 0)]:
                        if not checkout(a+dx, c+dy) and time[a+dx][c+dy] > time[a][c]+1:
                            time[a+dx][c+dy] = time[a][c]+1


    print(time)
    return time[MAX_ALP][MAX_COP]


print(solution(
    10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
))
print(solution(
    0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
))