N = int(input())
count = -1
answer = -1

def solution(limit, sub):
    global count, answer

    # 해당하는 길이에서 끝까지 탐색한 경우
    if len(sub) == limit:
        count += 1
        if count == N:
            answer = int(sub)
            print(answer)
            exit()
        return

    # 다음 탐색해야 되는 경우 : 맨 앞자리부터 생성
    else:
        if sub == '':
            for i in range(limit-1, 10):
                sub += str(i)
                solution(limit, sub)
                sub = ''
        else:
            # 앞자리보다 더 작은 수만
            for i in range(int(sub[-1])):
                # 범위 안에 수를 계속 줄일 수 없는 경우
                if limit - len(sub) - 1 > i:
                    continue
                sub += str(i)
                solution(limit, sub)
                sub = sub[:-1]

for k in range(1, 11):
    solution(k, '')
print(-1)