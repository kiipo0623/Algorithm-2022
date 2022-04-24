import heapq
def do_col(graph):
    sero = list(map(list, zip(*graph)))
    sero = do(sero)
    return list(map(list, zip(*sero)))

def do(graph):
    after = []
    maxlen, maxlenidx = -1, -1
    for lineidx, line in enumerate(graph): # [1, 2, 3]
        new_item = []
        tmp = []  # 크기 순 정렬
        value_list = []  # 키 리스트
        for idx, value in enumerate(line):
            if value == 0:
                continue
            if value in value_list:
                continue
            else:
                heapq.heappush(tmp, [line.count(value), value])
                value_list.append(value)

        while tmp:
            now = heapq.heappop(tmp)
            new_item.append(now[1])
            new_item.append(now[0])

        if len(new_item) > 100:
            new_item = new_item[:100]

        if maxlen < len(new_item):
            maxlen, maxlenidx = len(new_item), idx
        after.append(new_item)

    for idx, a in enumerate(after):
        if len(a)<maxlen:
            a.extend([0]*(maxlen-len(a)))
        after[idx] = a

    return after


def simulate(row, col, k):
    global A
    R, C = len(A), len(A[0])
    if row<=R-1 and col<=C-1 and A[row][col] == k:
        return 0

    for time in range(1, 101):
        R, C = len(A), len(A[0])
        if R>=C:
            A = do(A)

        else:
            A = do_col(A)

        R, C = len(A), len(A[0])
        if row<=R-1 and col<=C-1 and A[row][col] == k:
            return time

    return -1




r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

temp = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(simulate(r-1, c-1, k))