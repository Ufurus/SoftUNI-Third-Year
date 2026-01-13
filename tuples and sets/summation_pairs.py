import time

numbers = [int(num) for num in input().split()]
target_number = int(input())

start = time.time()
for i in range(len(numbers)):
    if numbers[i] == '':
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == '':
            continue
        if numbers[i] + numbers[j] == target_number:
            print(f"{numbers[i]} + {numbers[i]} = {target_number}")
            numbers[i] = ''
            numbers[j] = ''

end = time.time()
print(f"Time range: {end-start}")