def calc_num(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + calc_num(numbers, idx + 1)

nums = [int(x) for x in input().split()]
print(calc_num(nums, 0))