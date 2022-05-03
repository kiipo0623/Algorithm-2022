from math import sqrt, floor
def changetok(n, k):
    t = '0123456789ABCDEF'
    a, b = divmod(n, k)
    if a == 0:
        return t[b]
    return changetok(a, k) + t[b]

def isPrime(num):
    if num <= 1:
        return 0
    for i in range(2, floor(sqrt(num))+1):
        if num%i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    newnum = changetok(n, k)

    # start = 0
    # for i in range(1, len(newnum)+1):
    #     if i == len(newnum):
    #         answer += isPrime(int(newnum[start:i]))
    #         break
    #     elif newnum[i] == '0':
    #         answer += isPrime(int(newnum[start:i]))
    #         start = i+1
    #         i = start+1

    start, end = 0, 1
    while True:
        if end == len(newnum):
            answer += isPrime(int(newnum[start:end]))
            break
        elif newnum[end] == '0':
            answer += isPrime(int(newnum[start:end]))
            start = end+1
            end = start+1
        else:
            end += 1

    return answer

print(solution(110011, 10))