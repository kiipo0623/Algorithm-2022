# 큐브는 U / 이동은 up

def cube_move(myun, dir):
    if myun == 'left':
        move = ['B', 'U', 'F', 'D']
        if dir == '+':
            pass
        elif dir == '-':
            move.reverse()
        beforetmp = [cube[move[3]][0], cube[move[3]][3], cube[move[3]][6]]
        for i in range(4):
            nowtmp = [cube[move[i]][0], cube[move[i]][3], cube[move[i]][6]]
            cube[move[i]][0], cube[move[i]][3], cube[move[i]][6] = beforetmp[0], beforetmp[1], beforetmp[2]
            nowtmp, beforetmp = beforetmp, nowtmp

    if myun == 'right':
        move = ['B', 'D', 'F', 'U']
        if dir == '+':
            pass
        elif dir == '-':
            move.reverse()
        beforetmp = [cube[move[3]][2], cube[move[3]][5], cube[move[3]][8]]
        for i in range(4):
            nowtmp = [cube[move[i]][2], cube[move[i]][5], cube[move[i]][8]] # 지금거 저장해두고
            cube[move[i]][2], cube[move[i]][5], cube[move[i]][8] = beforetmp[0], beforetmp[1], beforetmp[2] # 이전꺼 가져와서
            nowtmp, beforetmp = beforetmp, nowtmp

    if myun == 'front':
        if dir == '+':
            move = ['L', 'U', 'R', 'D']
            beforetmp = [cube[move[3]][0], cube[move[3]][1], cube[move[3]][2]]
            for i in range(3):
                nowtmp = cube[move[i]][8], cube[move[i]][7], cube[move[i]][6]
                cube[move[i]][8], cube[move[i]][7], cube[move[i]][6] = beforetmp[0], beforetmp[1], beforetmp[2]
                nowtmp, beforetmp = beforetmp, nowtmp
            cube[move[3]][0], cube[move[3]][1], cube[move[3]][2] = nowtmp[0], nowtmp[1], nowtmp[2]

        if dir == '-':
            move = ['R', 'U', 'L', 'D']
            beforetmp = [cube[move[3]][0], cube[move[3]][1], cube[move[3]][2]]
            for i in range(3):
                nowtmp = cube[move[i]][8], cube[move[i]][7], cube[move[i]][6]
                cube[move[i]][8], cube[move[i]][7], cube[move[i]][6] = beforetmp[0], beforetmp[1], beforetmp[2]
                nowtmp = beforetmp
            cube[move[3]][0], cube[move[3]][1], cube[move[3]][2] = beforetmp[0], beforetmp[1], beforetmp[2]

    if myun == 'back':
        if dir == '+':
            move = ['R', 'U', 'L', 'D']
            beforetmp = [cube[move[3]][6], cube[move[3]][7], cube[move[3]][8]]
            for i in range(3):
                nowtmp = cube[move[i]][2], cube[move[i]][1], cube[move[i]][0]
                cube[move[i]][2], cube[move[i]][1], cube[move[i]][0] = beforetmp[0], beforetmp[1], beforetmp[2]
                nowtmp = beforetmp
            cube[move[3]][6], cube[move[3]][7], cube[move[3]][8] = beforetmp[0], beforetmp[1], beforetmp[2]

        if dir == '-':
            move = ['L', 'U', 'R', 'D']
            beforetmp = [cube[move[3]][6], cube[move[3]][7], cube[move[3]][8]]
            for i in range(3):
                nowtmp = cube[move[i]][2], cube[move[i]][1], cube[move[i]][0]
                cube[move[i]][2], cube[move[i]][1], cube[move[i]][0] = beforetmp[0], beforetmp[1], beforetmp[2]
                nowtmp = beforetmp
            cube[move[3]][6], cube[move[3]][7], cube[move[3]][8] = beforetmp[0], beforetmp[1], beforetmp[2]

    if myun == 'up':
        if dir == '+':
            move = ['B', 'R', 'F', 'L']
            cube['R'][0], cube['R'][3], cube['R'][6], cube['F'][2], cube['F'][1], cube['F'][0], cube['L'][8], cube['L'][5], cube['L'][2], cube['B'][6], cube['B'][7], cube['B'][8]\
                =\
            cube['B'][6], cube['B'][7], cube['B'][8], cube['R'][0], cube['R'][3], cube['R'][6], cube['F'][2], cube['F'][1], cube['F'][0], cube['L'][8], cube['L'][5], cube['L'][2]
        elif dir == '-':
            move = ['B', 'L', 'F', 'R']
            cube['L'][8], cube['L'][5], cube['L'][2], cube['F'][2], cube['F'][1], cube['F'][0], cube['R'][0], cube['R'][3], cube['R'][6], cube['B'][6], cube['B'][7], cube['B'][8]\
                =\
            cube['B'][6], cube['B'][7], cube['B'][8], cube['L'][8], cube['L'][5], cube['L'][2], cube['F'][2], cube['F'][1], cube['F'][0], cube['R'][0], cube['R'][3], cube['R'][6]


    if myun == 'down':
        if dir == '+':
            cube['L'][6], cube['L'][3], cube['L'][6], cube['F'][8], cube['F'][7], cube['F'][6], cube['R'][2], cube['R'][5], cube['R'][8], cube['B'][0], cube['B'][1], cube['B'][2] \
                = \
            cube['B'][0], cube['B'][1], cube['B'][2], cube['L'][6], cube['L'][3], cube['L'][0], cube['F'][8], cube['F'][7], cube['F'][6], cube['R'][2], cube['R'][5], cube['R'][8]
        elif dir == '-':
            cube['R'][2], cube['R'][5], cube['R'][8], cube['F'][8], cube['F'][7], cube['F'][6], cube['L'][6], cube['L'][3], cube['L'][0], cube['B'][0], cube['B'][1], cube['B'][2]\
                =\
            cube['B'][0], cube['B'][1], cube['B'][2], cube['R'][2], cube['R'][5], cube['R'][8], cube['F'][8], cube['F'][7], cube['F'][6], cube['L'][6], cube['L'][3], cube['L'][0]

cmd_to_long = {'L':'left', 'R':'right', 'B':'back', 'F':'front', 'U':'up', 'D':'down'}
T = int(input())
for _ in range(T):
    N = int(input())
    todo = list(input().split())
    cube = {
        'U': ['w'] * 9,
        'D': ['y'] * 9,
        'F': ['r'] * 9,
        'B': ['o'] * 9,
        'L': ['g'] * 9,
        'R': ['b'] * 9
    }
    for i in range(N):
        m = cmd_to_long[todo[i][0]]
        d = todo[i][1]
        cube_move(m, d)
        print(m, d)
        print(cube)

    print(cube['U'])