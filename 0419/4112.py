import sys

pyramid = []
first_num = []

def setting():
    num = 1
    rowlen = 1
    while num <= 10000:
        temp = []
        for i in range(rowlen):
            if i == 0:
                first_num.append(num)
            temp.append(num)
            num += 1
        pyramid.append(temp)
        rowlen += 1

def b_search(target):
    start, end = 0, len(first_num)-1
    while start <= end:
        mid = (start + end)//2
        if target > first_num[mid]:
            start = mid + 1
        elif target < first_num[mid]:
            end = mid - 1
        else:
            return mid
    return end

def find_pos(num):
    row = b_search(num)
    col = num - first_num[row]
    return [row, col]

sys.stdin = open("input.txt", "r")
T = int(input())
setting()
for i in range(T):
    answer = 0
    a, b = map(int, input().split())
    arow, acol = find_pos(a)
    brow, bcol = find_pos(b)

    row = arow - brow
    col = acol - bcol

    if (row*col) >= 0: # 부호 같음
        row, col = abs(row), abs(col)
        answer = max(row, col)
    else: # 부호 다름
        answer = abs(row) + abs(col)
    print('#%d %d' % (i + 1, answer))

