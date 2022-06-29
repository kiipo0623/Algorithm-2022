# quick sort
# pivot 정하고 왼쪽 오른쪽 나누는 것
def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    small, same, big = [], [], []
    for item in arr:
        if item < pivot:
            small.append(item)
        elif item > pivot:
            big.append(item)
        else:
            same.append(item)
    return quicksort(small) + same + quicksort(big)

test = [3, 20 ,2, 5, 3, 6]
print(quicksort(test))