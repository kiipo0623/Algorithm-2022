def combination(select, maxnum, num):
    global sol
    if len(select) == maxnum:
        sol.append(select)
        print(select)
        return

    start = select[-1]+1 if select else num
    for i in range(start, NUM):
        select.append(i)
        combination(select, maxnum, num+1)
        select.pop()

NUM = 6
sol = []
combination([], 3, 0)
print(len(sol))
# 중복 처리가 안된다 permutation의 결과가 나온다
