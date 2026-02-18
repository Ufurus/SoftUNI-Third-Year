def plant_garden(available_space: float, *plant_and_plant_space, **plants_to_grow):

    same_counter = 0
    final_result = []
    planted_plants = {}
    allowed_plants = {key:value for key,value in plant_and_plant_space}

    for plant, amount in sorted(plants_to_grow.items()):
        if plant not in allowed_plants:
            continue
        space_per_plant = allowed_plants[plant]
        max_possible_plants = int(available_space / space_per_plant)
        plants_to_plant = min(max_possible_plants, amount)

        if plants_to_plant > 0:
            planted_plants[plant] = plants_to_plant  # Record planted plants
            available_space -= plants_to_plant * space_per_plant  # Update available space
        if available_space <= 0.0:
            break

    if planted_plants == plants_to_grow:
        final_result.append(f"All plants were planted! Available garden space: {available_space} sq meters.")
    else:
        final_result.append(f"Not enough space to plant all requested plants!")

    final_result.append("Planted plants:")

    for key, value in planted_plants.items():
        final_result.append(f"{key}: {value}")

    return "\n".join(final_result).strip()

print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))