import sys
input = sys.stdin.readline

def bt_m(maxcnt, selected, nowcnt):
    if nowcnt == maxcnt:
        m_selected.append(selected[:])

    start = m.index(selected[-1])+1 if selected else 0
    for i in range(start, len(m)):
        selected.append(m[i])
        bt_m(maxcnt, selected, nowcnt+1)
        selected.pop()

def bt_j(maxcnt, selected, nowcnt):
    if nowcnt == maxcnt:
        j_selected.append(selected[:])

    start = j.index(selected[-1])+1 if selected else 0
    for i in range(start, len(j)):
        selected.append(j[i])
        bt_j(maxcnt, selected, nowcnt+1)
        selected.pop()

L, C = map(int, input().split())
alphabet = list(input().split())
j, m = [], []
answer = []

for a in alphabet:
    if a in ['a', 'e', 'i','o', 'u']:
        m.append(a)
    else:
        j.append(a)

j.sort()
m.sort()


# 1개부터 자음 개수가 2개 이하가 될 때까지 : len(m) vs L-2(
for i in range(1, min(len(m), L-2)+1):
    # 자음 선택함수, 모음 선택함수 따로 > 합치기
    m_selected, j_selected = [], []
    bt_m(i, [], 0)
    bt_j(L-i, [], 0)


    for m_sel in m_selected:
        for j_sel in j_selected:
            tmp = m_sel + j_sel
            tmp.sort()
            answer.append(''.join(tmp))

answer.sort()
for item in answer:
    print(item)