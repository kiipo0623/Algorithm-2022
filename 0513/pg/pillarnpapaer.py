def solution(n, build_frame):
    answer = []
    gidung = [[0]*(n+1) for _ in range(n+1)]
    bo = [[0]* (n+1) for _ in range(n+1)]

    def check_one(row, col, architect):
        if architect == gidung:
            if row == 0:
                return True
            elif bo[row][col] or bo[row][col-1]:
                return True
            elif gidung[row-1][col]:
                return True

        elif architect == bo:
            if gidung[row-1][col] or gidung[row-1][col+1]:
                return True
            elif bo[row][col+1] and bo[row][col-1]:
                return True
        return False

    def check_all(architect): # 모든 좌표에 대해 검사
        for i in range(n+1):
            for j in range(n+1):
                if architect[i][j]:
                    if not check_one(i, j, architect):
                        return False
        return True

    def build(x, y, a, b):
        if a == 0:  # 기둥
            if b == 0:  # 삭제
                gidung[y][x] = 0
            elif b == 1:  # 설치
                gidung[y][x] = 1

        elif a == 1:  # 보
            if b == 0:  # 삭제
                bo[y][x] = 0
            elif b == 1:  # 설치
                bo[y][x] = 1

    for todo in build_frame:
        x, y, a, b = todo
        build(x, y, a, b)
        if not check_all(gidung): # False 뜨면
            if b==0: build(x, y, a, 1)
            elif b==1: build(x, y, a, 0)
            continue
        if not check_all(bo):
            if b==0: build(x, y, a, 1)
            elif b==1: build(x, y, a, 0)

    def find_frame(architect):
        if architect == gidung:
            for i in range(n+1):
                for j in range(n+1):
                    if architect[i][j] == 1:
                        answer.append([j, i, 0])

        elif architect == bo:
            for i in range(n+1):
                for j in range(n+1):
                    if architect[i][j] == 1:
                        answer.append([j, i, 1])
    find_frame(bo)
    find_frame(gidung)
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer

print(solution(
    5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
))

