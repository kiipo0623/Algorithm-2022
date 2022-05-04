def str2int(string):
    hour = int(string[0:2])
    minute = int(string[3:5])
    second = int(string[6:8])
    return (hour*3600) + (minute*60) + second

def int2str(number):
    hour, minute = divmod(number, 3600)
    minute, second = divmod(minute, 60)
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    second = str(second).zfill(2)
    return hour+':'+minute+':'+second


def solution(play_time, adv_time, logs):
    int_play_time = str2int(play_time)
    int_adv_time = str2int(adv_time)
    int_logs = []

    for log in logs:
        s, e = log.split('-')
        tmp = []
        tmp.append(str2int(s))
        tmp.append(str2int(e))
        int_logs.append(tmp)

    int_logs.sort()

    max_starttime, max_runtime = 0, 0
    # 어디를 시작 지점으로 잡으면 좋을지?
    for idx, int_log in enumerate(int_logs):
        adv_start = int_log[0]
        adv_fin = int_log[0] + int_adv_time
        tmp_runtime = 0

        tmp_runtime += min(adv_fin-adv_start, int_log[1]-adv_start)

        # 다른 비디오 탐색
        for another in int_logs[:idx]:
            if another[1] > adv_start:
                tmp_runtime += min(adv_fin, another[1]) - max(adv_start, another[0])

        for another in int_logs[idx+1:]:
            if another[0] < adv_fin:
                tmp_runtime += min(adv_fin, another[1]) - max(adv_start, another[0])
            else:
                break

        # 최고의 시간 업데이트
        if tmp_runtime > max_runtime:
            max_starttime = adv_start
            if adv_fin > int_play_time:
                update = max_starttime - (adv_fin - int_play_time)
                max_starttime = max(0, update)
            max_runtime = tmp_runtime

    return int2str(max_starttime)

print(solution(
"02:03:55", "00:14:15",  ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
))
print(solution(
"99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
))
print(solution(
"50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
))