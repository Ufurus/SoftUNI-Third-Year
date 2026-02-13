def accommodate(*guest_groups, **rooms):
    accommodated_guests = {}
    not_accommodations_count = 0
    final_result = []

    total_rooms = sorted(rooms.items(), key=lambda x: (x[1], x[0]))

    for guest in guest_groups:
        is_accommodated = False

        for room_key,capacity in total_rooms:
            if capacity >= guest:
                room_id = room_key.split("_")[1]
                if room_id not in accommodated_guests:
                    accommodated_guests[room_id] = guest
                    total_rooms.remove((room_key, capacity))
                    is_accommodated = True
                    break

        if not is_accommodated:
            not_accommodations_count += guest

    if accommodated_guests:
        final_result.append(f"A total of {len(accommodated_guests)} accommodations were completed!")
        for room_number in sorted(accommodated_guests.keys()):
            final_result.append(f"<Room {room_number} accommodates {accommodated_guests[room_number]} guests>")
    else:
        final_result.append(f"No accommodations were completed!")

    if not_accommodations_count > 0:
        final_result.append(f"Guests with no accommodation: {not_accommodations_count}")

    if total_rooms:
        final_result.append(f"Empty rooms: {len(total_rooms)}")

    return "\n".join(final_result).strip()

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))