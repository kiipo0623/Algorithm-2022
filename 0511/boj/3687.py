can_make = [set() for _ in range(101)]
can_make[2].add('1')
can_make[5].add('2')
can_make[5].add('3')
can_make[4].add('4')
can_make[5].add('5')
can_make[6].add('6')
can_make[3].add('7')
can_make[7].add('8')
can_make[6].add('9')
can_make[6].add('0')
print(can_make)

for i in range(3, 20): # 5
    for j in range(2, i//2+1):
        for front in can_make[j]:
            for back in can_make[i-j]:
                tmp = front + back
                can_make[i].add(tmp)


#
TC = int(input())

for _ in range(TC):
    num = int(input())
