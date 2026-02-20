def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid_index = (left + right) // 2
        mid_element = arr[mid_index]
        if mid_element == target:
            return mid_index
        if mid_element < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1

print(binary_search(arr = [int(x) for x in input().split()], target=int(input())))