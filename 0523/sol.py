from itertools import permutations
def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak] # %하기 귀찬아서

    for i, start in enumerate(weak): # 매번 순서 정하는거 (시작점)
        for friends in permutations(dist): # 순서 배정
            count = 1 # 몇명 쓰는지
            position = start

            for friend in friends:
                position += friend

                if position < weak_point[i+L-1]: # 다음 반복문
                    count += 1
                    # 아직 방문 안한것 중ㅇ ㅔ제일 앞에 잇는거
                    position = [w for w in weak_point[i+1:i+L] if w > position][0]

                else: # 종료
                    cand.append(count)
                    break

    return min(cand) if cand else -1