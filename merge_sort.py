def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        # add lesser values into merged array
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif right[j] <= left[i]:
            merged.append(right[j])
            j += 1

    # add remaining values in merged array
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


arr = [3, 1, 70, 43, 2, 5, 10, 7]
arr = [3,2,4,4,5,22,7,7,6,5,66,4,43,6,23,3,3,5,65,77]
print(merge_sort(arr))