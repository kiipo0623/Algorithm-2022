def solution(n, t, m, p):
    answer = ''
    everything = ''
    i = 0
    while len(everything) <= t*m:
        everything += change(i, n)
        i += 1
    print(everything)

    for i in range(p-1, t*m, m):
        answer += everything[i]

    return answer

def change(num, n):
    tmp = '0123456789ABCDEF'
    q, v = divmod(num, n)
    if q > 0:
        return change(q, n) + tmp[v]
    return tmp[v]

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
