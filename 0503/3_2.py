dx = [-1, 1]
def newidx(dir, k, program, cnt): # dir == 0이면 위로 / dir == 1 이면 아래로
    flag = True
    while cnt>0:
        k = k + dx[dir]
        if k == len(program):
            flag = False
            break
        if program[k] == True:
            cnt -= 1

    # U, D
    if flag:
        return k

    # C를 위해 구현
    else:
        k -= 1
        while not program[k]:
            k -= 1
        return k

def solution(n, k, cmd):
    answer = ''
    program = [True]*n
    stack = []
    updown = 0

    for c in cmd:
        if c[0] == 'U':
            up, cnt = c.split()
            updown -= int(cnt)
        elif c[0] == 'D':
            down, cnt = c.split()
            updown += int(cnt)
        elif c[0] == 'C':
            if updown < 0: # 위로
                k = newidx(0, k, program, -updown)
            elif updown > 0: # 아래로
                k = newidx(1, k, program, updown)
            updown = 0
            program[k] = False
            stack.append(k)
            k = newidx(1, k, program, 1)
        elif c[0] == 'Z':
            now = stack.pop()
            program[now] = True
            if now < k: # 위쪽에 생기면
                k += 1

        print(c, k, updown, program)

    for p in program:
        if p:
            answer += 'O'
        else:
            answer += 'X'
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))