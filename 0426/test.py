t = [[1,2], [3,4], [5,6]]
print(list(map(list, zip(*t)))[::-1])

