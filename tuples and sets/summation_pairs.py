import time

numbers = [int(num) for num in input().split()]
target_number = int(input())

found_numbers = {}

start = time.time()
for i in numbers:
    for j in numbers:
        if i + j == target_number:
            if i not in found_numbers and j not in found_numbers:
                if i != j:
                    found_numbers[i] = j

for first_num,second_num in found_numbers.items():
    print(f"{first_num} + {second_num} = {first_num + second_num}")

end = time.time()
print(f"Time range: {end-start}")