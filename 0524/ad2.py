def str2int(time):
    hh = int(time[:2])*3600
    mm = int(time[3:5])*60
    ss = int(time[6:])
    return hh+mm+ss

def int2str(time):
    hh = str(time//3600).zfill(2)
    mm = str((time%3600)//60).zfill(2)
    ss = str(time%60).zfill(2)
    return hh+':'+mm+':'+ss

def solution(play_time, adv_time, logs):
    answer, best = 0, 0
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    new_log = []

    for idx, log in enumerate(logs):
        s, e = log.split('-')
        tmp = []
        tmp.append(str2int(s))
        tmp.append(str2int(e))
        new_log.append(tuple(tmp))

    new_log.sort()

    # 각 로그에 대해서 시작 시점 구하기 > idx에서부터 탐색X 맨앞부터 탐색
    for idx, log in enumerate(new_log):
        start, end = log
        if start + adv_time <= play_time:
            starttime = start
            endtime = starttime+adv_time

        else:
            starttime = start - (start+adv_time-play_time)
            endtime = starttime + adv_time

# 범위에 포함된 것 : 1)완전 포함 2) 범위를 포함 3) 시작에 걸침 4) 끝에 걸
        play_sum = 0
        for s, e in new_log:
            if s > endtime:
                break

            if s >= starttime and e <= endtime:
                play_sum += e-s
            elif s <= starttime and e >= endtime:
                play_sum += endtime - starttime
            elif starttime <= s <= endtime:
                play_sum += endtime - s
            elif s <= endtime <= e:
                play_sum += e - starttime

        print(int2str(starttime), int2str(play_sum))

        if play_sum > best:
            best = play_sum
            answer = starttime

    return int2str(answer)

# print(solution(
#     "02:03:55", "00:14:15",
#     ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# ))

print(solution(
"99:59:59"	, "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
))