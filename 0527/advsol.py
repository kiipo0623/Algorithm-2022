def str2int(s):
    hh = int(s[0:2])*3600
    mm = int(s[3:5])*60
    ss = int(s[6:8])
    return hh+mm+ss

def int2str(i):
    hh = str(i//3600)
    mm = str((i%3600)//60)
    ss = str(i%60)
    return hh.zfill(2)+':'+mm.zfill(2)+':'+ss.zfill(2)

def solution(play_time, adv_time, logs):
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    all_time = [0 for i in range(play_time+1)] # 시간에다가 사람을 적립

    for l in logs:
        start, end = l.split('-')
        end, start = str2int(end), str2int(start)
        all_time[start] += 1 # 메모하는 방식 (시작과 끝점에 대해)
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        # 내 칸에 앞에거 가져와서 더해라
        # start/end체크한거에 대해서
        all_time[i] += all_time[i-1]

    for i in range(1, len(all_time)):
        # 두번하는 이유? 마지막으로 갱신 ?
        # 전체 누적값에 대해서
        all_time[i] += all_time[i-1]

    most_view = all_time[adv_time] # 가장 많이 본 시간
    max_time = 0 # 시작 시간
    # 끝났을 떄의 인간 수가 기준이므로
    for i in range(adv_time, play_time):
        if most_view < all_time[i] - all_time[i-adv_time]:
            most_view = all_time[i] - all_time[i-adv_time]
            max_time = i - adv_time + 1

    return int2str(max_time)

print(solution(
"02:03:55", "00:14:15",
["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
))

print(solution(
"99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
))

print(solution(
"50:00:00"	, "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
))