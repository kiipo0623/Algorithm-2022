'''
(in) 문자열
(out) 문자열

괄호가 개수는 맞지만 짝이 맞지 않는 형태
균형잡힌 괄호열 : 괄호의 개수 동일
올바른 괄호열 : 짝이맞을 때

u(균형잡힌 괄호 문자열 최소 : 개수 되자마자 끊음) + v(빈 문자열 가능)
u(올바른) : v에 대해 수행 한 후 붙임 (재귀)
u(올바르지 않은) :
'''

def check(s):
    stack = []
    for ss in s:
        if ss == '(':
            stack.append(ss)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def rev(b):
    ans = ''
    for bb in b:
        if bb == '(':
            ans += ')'
        else:
            ans += '('
    return ans[1:-1]

def balance(s):
    if len(s) == 0:
        return ''
    cnt = 0
    u, v = '', ''
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1

        if cnt == 0:
            u = s[:i+1]
            v = s[i+1:]
            break
    # u, v 구함
    if check(u):
        return u + balance(v)
    else:
        return '(' + balance(v) + ')' + rev(u)


def solution(p):
    return balance(p)

print(solution(
")("
))