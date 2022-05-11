def checkout(row, col):
    if row<0 or col<0 or row>=151 or col>=151:
        return True
    return False
def solution(alp, cop, problems):
    grade = [[0]*151 for _ in range(151)]
    MAX_ALP, MAX_COP = 0, 0

    for i in range(151):
        for j in range(151):
            if checkout(alp+i,cop+j):
                continue
            grade[alp+i][cop+j] = i+j

    for p in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = p

        if alp_req>MAX_ALP:
            MAX_ALP = alp_req
        if cop_req>MAX_COP:
            MAX_COP = cop_req

        for i in range(151):
            for j in range(151):
                if checkout(i+alp_rwd, j+cop_rwd):
                    continue
                if i<alp_req or j<cop_req:
                    continue
                if grade[i+alp_rwd][j+cop_rwd] > grade[i][j]+cost:
                    grade[i + alp_rwd][j + cop_rwd] = grade[i][j]+cost

    print(MAX_ALP)
    print(MAX_COP)
    return grade[MAX_ALP-1][MAX_COP-1]

print(solution(
    10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
))
print(solution(
    0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
))