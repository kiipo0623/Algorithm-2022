def dd(r_pos, c_pos):
    d1max = min((N-1-r_pos)//2, r_pos)
    d2max = min((N-1-r_pos)//2, N-1-r_pos)
    print("d1", d1max, "d2", d2max)

def xy():
    xy_candidate = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            xy_candidate.append((i, j))
    print(xy_candidate)

    for xy in xy_candidate:
        print("xy ", xy)
        dd(xy[0], xy[1])


N = int(input())
xy()
