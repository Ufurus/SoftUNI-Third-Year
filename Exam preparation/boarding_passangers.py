def boarding_passengers(capacity, *kwargs):
    total_capacity = capacity
    boarded_people = {}
    waiting_people = False

    for i in kwargs:
        key, value = i[1], i[0]
        if value <= total_capacity:
            if key not in boarded_people:
                boarded_people[key] = 0
            boarded_people[key] += value
            total_capacity -= value
        else:
            waiting_people = True
            if capacity <= 0:
                break

    sorted_list = sorted(boarded_people.items(), key=lambda x: (-x[1], x[0]))
    message = ""

    if not waiting_people:
        message = f"All passengers are successfully boarded!"
    elif total_capacity <= 0:
        message = "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        message = f"Partial boarding completed. Available capacity: {total_capacity}."

    final_list = []
    final_list.append("Boarding details by benefit plan:")
    for i in sorted_list:
        final_list.append(f"## {i[0]}: {i[1]} guests")
    final_list.append(f"{message}")
    return '\n'.join(final_list)

print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
