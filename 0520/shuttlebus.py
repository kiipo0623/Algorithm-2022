from collections import defaultdict
def timechange(time):
    hour = int(time[:2])*60
    minute = int(time[3:])
    return hour+minute

def strchange(time):
    hour = str(time//60).zfill(2)
    minute = str(time%60).zfill(2)
    return hour+':'+minute

def solution(n, t, m, timetable):
    answer = ''
    # 버스 시간표
    bus_time = []
    bus_start = timechange("09:00")

    for i in range(n):
        bus_time.append(bus_start)
        bus_start += t

    for idx, crew in enumerate(timetable):
        timetable[idx] = timechange(crew)

    # 크루별 출근시간
    timetable.sort()

    # 출발시간 : 크루시간
    bus_crew = defaultdict(list)
    print(bus_crew)

    # 버스 시간표 처음부터 보면서 자기보다 크거나 같은 시간에 들어간다
    # 빈칸 없으면 버스 계속 밀린다
    for crew in timetable:
        flag = False
        for idx, bus in enumerate(bus_time):
            if bus >= crew:
                flag = True
                bus_canride, bus_idx = bus, idx
                break
        if not flag:
            continue

        while True:
            if not bus_crew.get(bus_canride) or len(bus_crew[bus_canride]) < m:
                bus_crew[bus_canride].append(crew)
                break
            else:
                bus_idx += 1
                if bus_idx == len(bus_time):
                    break
                bus_canride = bus_time[bus_idx]

    lastbus = bus_time[-1]
    if len(bus_crew[lastbus]) < m:
        return strchange(lastbus)
    elif len(set(bus_crew[lastbus])) == 1:
        return strchange(bus_crew[lastbus][0]-1)
    else:
        return strchange(bus_crew[lastbus][-1]-1)

print(solution(
10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
))