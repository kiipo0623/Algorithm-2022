from collections import deque
def make_num(N, q): # 점검 완료
    global number_set
    for i in range(N):
        byun = N/4
        # 회전
        tmp = q.popleft()
        q.append(tmp)
        precious = list(q)
        for k in range(1,5):
            tmp = precious[int((k-1)*byun):int(k*byun)]
            number_set.add(''.join(tmp))

def sixteen_to_ten(s):
    numdict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    l = len(s)
    sum_ = 0
    for i in range(l):
        now = s[i]
        if s[i] in numdict:
            now = numdict[now]
        sum_ += int(now) * (16**(l-i-1))
    return sum_

# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    numbers = list(input())
    numbers = deque(numbers)
    number_set = set()
    make_num(N, numbers)

    str_number_list = list(number_set)
    int_number_list = []
    for n in str_number_list:
        int_number_list.append(sixteen_to_ten(n))
    int_number_list.sort(reverse=True)
    print('# {} {}'.format(t+1, int_number_list[K-1]))
