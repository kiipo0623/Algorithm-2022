import math
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def bt(idx, number):
    if len(number) and not isPrime(int(number)):
        return
    if idx == N:
        res.append(number)
        return

    for i in range(10):
        bt(idx+1, number+str(i))

N = int(input())
res = []
bt(0, '')
res.sort()
for r in res:
    print(r)