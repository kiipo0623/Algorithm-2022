from copy import deepcopy
cube = {'U':['w']*9, 'D':['y']*9, 'F':['r']*9, 'B':['o']*9, 'L':['g']*9, 'R':['b']*9}
round = {'L':['U', 'F', 'D', 'B'],
         'R':['U', 'B', 'D', 'F'],
         'U':['F', 'L', 'B', 'R'],
         'D':['F', 'R', 'B', 'L'],
         'F':['U', 'R', 'D', 'L'],
         'B':['U', 'L', 'D', 'R']}

moveidx = {'L':[0, 3, 6],
           'R':[2 ,5, 8],
           'B':[0, 1, 2],
           'F':[6, 7, 8],
           'U':[0, 1, 2],
           'D':[6, 7, 8]}

def simulation(myun, dir):
    global nowcube
    nowround = round[myun]
    newround = ['X'] * 4
    for i in range(4):
        newround[(i + dir) % 4] = nowround[i]

    print("myun", myun)
    print("dir", dir)
    print("nowround", nowround)
    print("newround", newround)
    for idx in moveidx[myun]:
        #nowround 현재 newround 이동
        nowindex = ['x']*4
        for i in range(4):
            nowindex[i] = nowcube[nowround[i]][idx]
        for i in range(4):
            nowcube[newround[i]][idx] = nowindex[i]

        print("idx", idx)
        print("nowindex", nowindex)
    print(nowcube)

T = int(input())
for _ in range(T):
    N = int(input())
    nowcube = deepcopy(cube)
    print(nowcube)
    mvlist = list(input().split())
    for i in range(N):
        myun, dir = mvlist[i][0], mvlist[i][1]
        if dir == '+':
            dir = -1
        else:
            dir = 1
        simulation(myun, dir)
    print(nowcube['U'])
