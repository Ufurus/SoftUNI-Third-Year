from collections import deque
substances = [int(x) for x in input().split(", ")]
crystal_energy = deque([int(x) for x in input().split(", ")])
potions_count = 0

all_potions = {"Brew of Immortality": 110,
               "Essence of Resilience": 100,
               "Draught of Wisdom": 90,
               "Potion of Agility": 80,
               "Elixir of Strength": 70}

crafted_potions = []

while substances and crystal_energy and potions_count < 5:

    current_substance = substances.pop()
    current_energy = crystal_energy.popleft()

    total_sum = current_substance + current_energy
    for potion, value in all_potions.items():
        if all_potions[potion] == total_sum:
            if potion not in crafted_potions:
                crafted_potions.append(potion)
                potions_count += 1
                break

    else:
        a = sorted(all_potions.items(), key=lambda x: (x[1],x[0]), reverse=True)
        for potion, value in a:
            if all_potions[potion] <= total_sum:
                if potion not in crafted_potions:
                    crafted_potions.append(potion)
                    new_energy = current_energy - 20
                    if new_energy > 0:
                        crystal_energy.append(new_energy)
                    potions_count += 1
                    break
        else:
            new_energy = current_energy - 5
            if new_energy > 0:
                crystal_energy.append(new_energy)

if potions_count == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances[::-1]])}")

if crystal_energy:
    print(f"Crystals: {', '.join([str(x) for x in crystal_energy])}")