c = [i for i in range(5)]
from itertools import combinations
print(list(map(set, combinations(c, 3))))