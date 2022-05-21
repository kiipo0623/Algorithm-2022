import math
x = 0
y = 1
# 시계방향 회전
print(x*round(math.cos(90)) - y*round(math.sin(90)))
print(x*round(math.sin(90)) + y*round(math.cos(90)))
# 반시계방향 회
print(x*round(math.cos(-90)) - y*round(math.sin(-90)))
print(x*round(math.sin(-90)) + y*round(math.cos(-90)))