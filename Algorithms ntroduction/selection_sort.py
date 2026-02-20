def selection_sort(arr):
    for idx in range(len(arr)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(arr)):
            if arr[curr_idx] < arr[min_idx]:
                min_idx = curr_idx
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

    return ' '.join(map(str, arr))

print(selection_sort(arr=[int(x) for x in input().split()]))