def convert(n, base):
    arr = '0123456789ABCDEF'
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]

def getN(n, base):
    rev_base = ''
    while n>0:
        n, r = divmod(n, base)
        rev_base = str(r) + rev_base
    return rev_base

print(getN(10, 2))