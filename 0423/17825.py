# cnt : 몇번째인지 horse:4개짜리 리스트(idx, map), grade:현재 점수
def bt(cnt, horse, grade):
    global answer
    print("갓 시작", cnt, horse, grade)

    if cnt == 10:
        answer = max(answer, grade)
        return

    flag = False
    for i in range(4):
        # 시작점에서 겹치는 경우
        print("now horse", i)
        if horse[i] == (0, 0):
            print("시작점에서 겹치는 경우")
            if flag: # 이미 해당 위치 이동 완료
                print("이미 해당 위치 이동 완료")
                continue
            else:
                flag = True

        # 끝지점이면 패스
        if horse[i] == (21, 0) or horse[i] == (8, 1) or horse[i] == (7, 2) or horse[i] == (8, 3):
            print("끝지점이면 패스")
            continue

        # 어떻게든 이동을 시작하는 경우
        print("어떻게든 이동을 시작하는 경우")
        idx, map = horse[i]
        now = idx+d[cnt]
        print("idx", idx, "map", map, "now", now)

        # 끝나는 경우
        if (map == 0 and now >= 21) or (map in [1, 3] and now>=8) or (map==2 and now >= 7):
            print("끝나는 경우")
            if (map == 0 and now > 21):
                horse[i] = (21, 0)
            elif (map in [1, 3] and now>=8):
                horse[i] = (8, 1)
            elif (map==2 and now > 7):
                horse[i] = (7, 2)
            bt(cnt+1, horse, grade)
            horse[i] = (idx, map)
            continue

        # 다른 말이 도착지에 있으면 continue
        for k in range(4):
            if horse[k] == (now, map):
                print("다른 말이 도착지에 있으면 continue")
                continue

        # 파란색 위치면 값 더하고 map 변경해서 호출
        if map==0 and (yutmap[map][now] == 10 or yutmap[map][now] == 20 or yutmap[map][now] == 30):
            print("파란색 위치면 값 더하고 map 변경해서 호출")
            if yutmap[map][now] == 10:
                horse[i] = (0, 1)
            elif yutmap[map][now] == 20:
                horse[i] = (0, 2)
            elif yutmap[map][now] == 30:
                horse[i] = (0, 3)
            bt(cnt+1, horse, grade+yutmap[map][now])
            print("----------", horse[i], idx, map)
            horse[i] = (idx, map)
            continue

        # 아니면 점수 더하고 갱신
        print("아니면 점수 더하고 갱신")
        horse[i] = (now, map)
        bt(cnt+1, horse, grade+yutmap[map][now])
        horse[i] = (idx, map)
        continue



main = [i for i in range(0, 42, 2)]
main.append(0)
ten = [10, 13,16, 19, 25, 30, 35, 40, 0]
twenty = [20, 22, 24, 25, 30, 35, 40, 0]
thirty = [30, 28, 27, 26, 25, 30, 35, 40, 0]
yutmap = [main, ten, twenty, thirty]

d = list(map(int, input().split()))
answer = 0
bt(0, [(0, 0), (0, 0), (0, 0), (0, 0)], 0)

print(answer)