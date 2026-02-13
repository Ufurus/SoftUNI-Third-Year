from collections import deque
bee_groups = deque(list(map(int, input().split()))) # 42, 7, 28, 3
eaters_groups = list(map(int, input().split())) # 1, 5

while bee_groups and eaters_groups:

    current_bees = bee_groups.popleft()
    current_eaters = eaters_groups.pop()

    while current_bees > 0 and current_eaters > 0:
        if current_bees >= 7:
            current_bees -= 7
            current_eaters -= 1
        else:current_bees -= 7

    if current_bees > 0 and current_eaters <= 0:
        bee_groups.append(current_bees)
    elif current_bees <= 0 and current_eaters > 0:
        eaters_groups.append(current_eaters)

print("The final battle is over!")

if not bee_groups and not eaters_groups:
    print("But no one made it out alive!")
elif bee_groups:
    print(f"Bee groups left:", ", ".join(map(str, bee_groups)))
elif eaters_groups:
    print(f"Bee-eater groups left:", ", ".join(map(str, eaters_groups)))