def move(frm, to, mid, n, answer):
    if n == 1:
        # 시작지 -> 목적지를 answer에 listfh wjwkd
        answer.append([frm, to])
        return
    move(frm, mid, to, n-1, answer) # n-1개를 시작 기둥에서 보조기둥으로 옮김
    answer.append([frm, to]) #n번째를 시작 기둥에서 목표 기둥으로 옮김
    move(mid, to, frm, n-1, answer) #n-1개를 보조기둥에서 목표기둥으로 옮김

def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer

print(solution(3))