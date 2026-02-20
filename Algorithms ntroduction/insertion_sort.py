def insertion_sort(arr):
    for j in range(1, len(arr)):
        for i in range(j, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                break

    return ' '.join(map(str, arr))

print(insertion_sort(arr=[int(x) for x in input().split()]))