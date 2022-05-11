from collections import deque
import sys
sys.setrecursionlimit(10**6)
front_trav, back_trav = [], []

def front_traversal(binarytree, root):
    if root == -1:
        return
    front_trav.append(root)
    front_traversal(binarytree, binarytree[root][0])
    front_traversal(binarytree, binarytree[root][1])

def back_traversal(binarytree, root):
    if root == -1:
        return
    back_traversal(binarytree, binarytree[root][0])
    back_traversal(binarytree, binarytree[root][1])
    back_trav.append(root)

def find_son(node, start, end):
    global nodepos, board
    for i in range(nodepos[node][0]-1, -1, -1):
        for j in range(start, end):
            if board[i][j] != 0:
                return board[i][j]
    return -1


def find_binarytree(ROOT,COLMAX, COLMIN):
    queue = deque()
    queue.append((ROOT, COLMIN, COLMAX+1)) #for문에 넣기 좋은 형태
    binarytree = dict()

    while queue:
        node, l_boundary, r_boundary = queue.popleft()

        left_son = find_son(node, l_boundary, nodepos[node][1])
        right_son = find_son(node, nodepos[node][1]+1, r_boundary)
        binarytree[node] = [left_son, right_son]
        if left_son > 0:
            queue.append((left_son, l_boundary, nodepos[node][1]))
        if right_son > 0:
            queue.append((right_son, nodepos[node][1]+1, r_boundary))

    print(binarytree)
    return binarytree


def solution(nodeinfo):
    global N, nodepos, board
    N = len(nodeinfo)
    answer = []

    board = [[0]*100001 for _ in range(1001)]
    COLMAX, COLMIN = -int(1e9), 100000
    ROWMAX, ROWMIN = 0, 1000
    nodepos = dict()


    for idx, node in enumerate(nodeinfo): # idx 1올리기
        col, row = node
        if col > COLMAX: COLMAX = col
        if col < COLMIN: COLMIN = col
        if row > ROWMAX: ROWMAX = row
        if row < ROWMIN: ROWMIN = row

        board[row][col] = idx+1
        nodepos[idx+1] = [row, col]

    for i in range(COLMIN, COLMAX+1):
        if board[ROWMAX][i] != 0:
            ROOT = board[ROWMAX][i]
            break

    # binary tree 구성 완료
    binarytree = find_binarytree(ROOT, COLMAX, COLMIN)

    # 순회
    front_traversal(binarytree, ROOT)
    back_traversal(binarytree, ROOT)

    answer.append(front_trav)
    answer.append(back_trav)

    return answer


print(solution(
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
))