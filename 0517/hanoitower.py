dp = dict()
ans = []
MIN = float('inf')

# now 형태 : ('123', '4', '')
# dp 형태 : now를 넣은거

def bt(visited, now, fin):
    global ans, MIN
    if now == fin and len(ans) < MIN:
        ans = visited
        MIN = len(ans)

    for do in [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]:
        if now[do[0]] == '': # 이동 할게 없으면
            continue
        if now[do[0]][-1] > now[do[1]][-1]:
            continue
        item = now[do[0]][-1]
        now[do[0]] = now[do[0]][:-1]
        now[do[1]] += item
        


def solution(n):
    answer = [[]]
    return answer