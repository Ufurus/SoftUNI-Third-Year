number_of_guests = int(input())
guests_first = set()
guests_second = set()

while True:
    reservation_code = input()
    if reservation_code == "END":
        break

    if reservation_code not in guests_first:
        guests_first.add(reservation_code)
    else:
        guests_second.add(reservation_code)

print(len(guests_first.difference(guests_second)))
guests_not_arrived = sorted(list(guests_first.difference(guests_second)))
for guest in guests_not_arrived:
    print(guest)