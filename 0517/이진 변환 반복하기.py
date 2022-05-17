counter = 0
def binary_change(s):
    global counter
    zero_cnt = s.count('0')
    counter += zero_cnt
    s = s.replace('0','')

    return bin(len(s))[2:]

def solution(s):
    global counter
    cnt = 0
    while s!='1':
        s = binary_change(s)[:]
        cnt += 1

    return [cnt, counter]

print(solution(
"110010101001"
))