def updateanswer(ryan, info): # 최고의 점수 업데이트
    global best_diff, best_ryan
    ryan_grade, apeach_grade = 0, 0

    for i in range(11):
        if ryan[i] > info[i]:
            ryan_grade += (10-i)
        elif ryan[i] < info[i]:
            apeach_grade += (10-i)
        else:
            if ryan[i] == info[i] == 0:
                continue
            else:
                apeach_grade += (10-i)
    if apeach_grade >= ryan_grade: # 어피치 승
        return
    else: # 라이언 승
        if best_diff < (ryan_grade - apeach_grade): # 최고의 차이점수
            best_diff = ryan_grade - apeach_grade
            best_ryan = ryan[:]
        elif best_diff == (ryan_grade - apeach_grade):
            for i in range(10, -1, -1): # 뒤에서부터 확인
                if best_ryan[i] > ryan[i]: # 원래 것이 나음
                    return
                elif best_ryan[i] == ryan[i]: #같으면 다음거 비교
                    continue
                else:
                    best_ryan = ryan[:]


def bt(idx, ryan, leftarrow, info):
    if leftarrow == 0:
        updateanswer(ryan, info)
        return

    elif idx == 11:
        tmp = ryan[:]
        tmp[-1] += leftarrow
        updateanswer(tmp, info)
        # ryan[-1] -= leftarrow # 여기서 이 값을 되돌려주지 않고 종료했기 때문에 에러가 났다 어차피 return하면 원래 위치로 돌아가는데 왜 ??
        return

    # 승리하는 경우
    use = info[idx]+1
    if use <= leftarrow:
        ryan[idx] = use
        bt(idx+1, ryan, leftarrow-use, info)
        ryan[idx] = 0

    # 패배하는 경우
    bt(idx+1, ryan, leftarrow, info)

def solution(n, info):
    global best_diff, best_ryan
    best_diff, best_ryan = 0, [0]*11
    bt(0, [0]*11, n, info)
    if best_diff == 0:
        return [-1]
    else:
        return best_ryan

print(solution(
    5, [2,1,1,1,0,0,0,0,0,0,0]
))

print(solution(
    1, [1,0,0,0,0,0,0,0,0,0,0]
))

print(solution(
    9, [0,0,1,2,0,1,1,1,1,1,1]
))

print(solution(
    10, [0,0,0,0,0,0,0,0,3,4,3]
))