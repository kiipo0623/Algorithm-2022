from collections import deque
def checker(p):
    stack = []
    queue = deque(p)

    while queue:
        now = queue.popleft()
        if now == '(':
            stack.append(now)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack):
        return False
    return True

def change(p):
    if len(p) == 0:
        return ''

    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    print("u", u)
    print("v", v)

    if checker(u):
        return u + change(v)
    else:
        tmp = ''
        tmp += '('
        tmp += change(v)
        tmp += ')'
        tmp += reverseitem(u[1:-1])
        return tmp

def reverseitem(s):
    a = ''
    for i in range(len(s)):
        if s[i] == '(':
            a += ')'
        else:
            a += '('
    return a

def solution(p):
    if checker(p):
        return p
    else:
        return change(p)

print(solution("))((()"))
