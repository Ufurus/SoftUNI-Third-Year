clothes = [int(num) for num in input().split()]
rack_id = int(input())
total_racks = 0

while clothes:
    total_racks += 1
    current_rack = rack_id
    while clothes and clothes[-1] <= current_rack:
        current_rack -= clothes.pop()

print(total_racks)