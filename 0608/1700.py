from collections import defaultdict, deque
N, K = map(int, input().split())
items = list(map(int, input().split()))
item_dict = defaultdict(deque)
plug = [0]*N
answer = 0

# 딕셔너리에 미리 넣어두고
for idx, item in enumerate(items):
    item_dict[item].append(idx)

for i in range(K):
    now = items[i] # 순서대로 하나씩 뽑아서

    if now in plug:
        item_dict[now].popleft()

    elif 0 in plug: # 플러그에 자리가 있으면
        plug[plug.index(0)] = now
        item_dict[now].popleft()

    else: # 플러그에 자리가 없으면
        answer += 1 # 하나 무조건 뽑아야 함
        maxx, maxidx = 0, 0 # 제일 먼거, 그 인덱스
        for idx, plugitem in enumerate(plug):
            if len(item_dict[plugitem]) == 0: # 없으면
                maxx, maxidx = int(1e9), idx
                break
            # 나를 빼야 하는 경우는 이미 앞에서 걸린다
            elif item_dict[plugitem][0] > maxx:
                maxx, maxidx = item_dict[plugitem][0], idx

        item_dict[now].popleft()
        plug[maxidx] = now # 플러그 꽂기

print(answer)