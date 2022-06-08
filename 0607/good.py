# 1, 2, 3으로만 이루어진 N짜리 수열 중 가장 작은 수를 나타내는 수열 빈칸없
# 인접한 두 개의 부분수열이 동일하면 나쁜 수열
# 없으면 좋은 수열
def bt(s):
    L = len(s)
    if L == N:
        answer.append(s)
        return

    for i in range(1, 4):
        tmp_s = s+str(i)
        L = len(tmp_s)
        for j in range(1, (L+1)//2+1):
            


N = int(input())
answer = []
# 계속 추가하면서 그앞에 확인해서 ?
bt('1')
bt('2')
bt('3')
print(min(answer))
