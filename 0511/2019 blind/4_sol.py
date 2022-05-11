import sys
sys.setrecursionlimit(10**6)

def find(chk, rooms):
    if chk not in rooms:
        rooms[chk] = chk+1
        return chk

    empty = find(rooms[chk], rooms)
    rooms[chk] = empty+1
    return empty

def solution(k, room_number):
    answer = []
    rooms = dict()

    for i in room_number:
        chk_in = find(i, rooms)
        answer.append(chk_in)
    return answer

print(solution(
    10, [1,3,4,1,3,1]
))