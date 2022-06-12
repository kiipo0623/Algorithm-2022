def check(num):
    num = str(num)
    L = len(num)
    for i in range(L-1):
        if num[i] > num[i+1]:
            continue
        else:
            return False
    return True

N = int(input())
counter = 0
number = 0
while True:
    if check(number):
        if counter == N:
            print(number)
            break

        counter += 1
    number += 1
    if number > 9876543210:
        break
print(-1)


