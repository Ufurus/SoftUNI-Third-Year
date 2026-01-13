numbers = [float(num) for num in input().split()]
items = ()
total_items = {}

for num in numbers:
    items += num,

for item in items:
    if item not in total_items:
        total_items[item] = items.count(item)

for key,value in total_items.items():
    print(f"{key:.1f} - {value} times")