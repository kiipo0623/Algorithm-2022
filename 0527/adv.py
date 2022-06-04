def int2str(s):
    hh = int(s[0:2])*3600
    mm = int(s[3:5])*60
    ss = int(s[6:8])
    return hh+mm+ss

def str2int(i):
    hh = str(i//3600)
    mm = str((i%3600)//60)
    ss = str(i%60)
    return hh.zfill(2)+':'+mm.zfill(2)+':'+ss.zfill(2)

def solution(play_time, adv_time, logs):
    MAX, ANS = 0, 0
    play_time = int2str(play_time)
    adv_time = int2str(adv_time)

    int_logs = []

    for log in logs:
        start, end = log.split("-")
        start, end = int2str(start), int2str(end)
        int_logs.append((start, end))

    int_logs.sort(key = lambda x : (x[1], x[0]))
    print(int_logs)

    # 탐색 자체는 시작시간으로 진행해야 함 ;; > 그건 어려우니까 데이터 저장할 때 idx 넣어서 idx 빠른 순으로
    # 이렇ㄱ ㅔ나누ㅝ봤자 다 포함한다면 ? 으미 X
    for i, (start, end) in enumerate(int_logs):
        tmp = 0
        if play_time >= start+adv_time:
            adv_start, adv_end = start, start+adv_time
        else:
            adv_start = start - (start+adv_time-play_time)
            adv_end = play_time # 잘못되었을 수도 있음
        # 앞쪽으로 탐색
        for idx in range(i-1, -1, -1):
            if int_logs[idx][1] > adv_start:
                # 꼬리 탐색 : sort되어 있으니까 괜찮음
                tmp += min(int_logs[idx][1], adv_end)- adv_start
            else:
                break

        # 뒤쪽으로 탐색 (자기 자신 포함)
        for idx in range(i, len(int_logs)):
            # 머리 탐색 :
            if int_logs[idx][0] < adv_end:
                tmp += adv_end - max(adv_start, int_logs[idx][0])
            else:
                break

        if tmp >= MAX:
            if tmp == MAX:
                ANS = min(ANS, adv_start)
            else:
                MAX = tmp
                ANS = adv_start
            print(str2int(ANS))

    return str2int(ANS)

# print(solution(
# "02:03:55", "00:14:15",
# ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# ))

print(solution(
"99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
))

print(solution(
"50:00:00"	, "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
))