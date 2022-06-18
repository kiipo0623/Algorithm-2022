# DFS를 사용해서 갈라치기를 해결할 수 없다
graph = []
answer = 0
def bt(Ynum, Snum, count, row, col, road):
    global answer
    if Ynum >= 4:
        return
    if count == 7:
        print(road)
        answer += 1

    for dx, dy in [(1, 0), (0, 1)]:
        drow, dcol = row+dx, col+dy
        if 0<=drow<5 and 0<=dcol<5:
            if graph[drow][dcol] == 'Y':
                road.append((drow, dcol))
                bt(Ynum+1, Snum, count+1, drow, dcol, road)
                road.pop()
            elif graph[drow][dcol] == 'S':
                road.append((drow, dcol))
                bt(Ynum, Snum+1, count+1, drow, dcol, road)
                road.pop()

for _ in range(5):
    graph.append(list(input()))

bt(0, 0, 0, 0, 0, [])
print(answer)