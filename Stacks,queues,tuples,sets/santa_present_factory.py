from collections import deque

crafting_materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
toy_prices = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}

first_pair = ["Doll", "Wooden train"]
second_pair = ["Bicycle", "Teddy bear"]

while crafting_materials and magic_level:

    current_box = crafting_materials[-1]
    current_magic = magic_level[0]
    result = current_box * current_magic

    if result in toy_prices.values():
        for toy, price in toy_prices.items():
            if toy_prices[toy] == result:
                toys[toy] += 1
                crafting_materials.pop()
                magic_level.popleft()
    elif result < 0:
        crafting_materials.pop()
        magic_level.popleft()
        crafting_materials.append(current_box + current_magic)

    elif result > 0:
        magic_level.popleft()
        crafting_materials[-1] += 15
    else:
        if current_magic == 0:
            magic_level.popleft()
        if current_box == 0:
            crafting_materials.pop()

if (toys["Doll"] and toys["Wooden train"]) or (toys["Teddy bear"] and toys["Bicycle"]):
    print("The presents are crafted! Merry Christmas!")

    if crafting_materials:
        print("Materials left: " + ", ".join(str(x) for x in reversed(crafting_materials)))
    if magic_level:
        print("Magic left: "+", ".join(str(x) for x in magic_level))

    total_presents = sorted(first_pair + second_pair)
    for present in total_presents:
        if present in toys:
            if toys[present]:
                print(f"{present}: {toys[present]}")

else:
    print("No presents this Christmas!")
    if crafting_materials:
        print("Materials left: "+ ", ".join(str(x) for x in reversed(crafting_materials)))
    elif magic_level:
        print("Magic left: "+", ".join(str(x) for x in magic_level))
    total_presents = sorted(first_pair + second_pair)
    for present in total_presents:
        if present in toys:
            if toys[present]:
                print(f"{present}: {toys[present]}")
