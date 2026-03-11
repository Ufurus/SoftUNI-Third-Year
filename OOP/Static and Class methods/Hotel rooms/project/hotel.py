from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        curr_room = next((x for x in self.rooms if x.number == room_number), None)
        if curr_room:
            curr_room.take_room(people)

    def free_room(self, room_number):
        curr_room = next((x for x in self.rooms if x.number == room_number), None)
        if curr_room:
            curr_room.free_room()

    def status(self):
        final_result = []
        self.guests = sum([x.guests for x in self.rooms if x.guests > 0])
        final_result.append(f"Hotel {self.name} has {self.guests} total guests")
        free_rooms = [x.number for x in self.rooms if not x.is_taken]
        taken_rooms = [x.number for x in self.rooms if x.is_taken]
        final_result.append(f"Free rooms: {', '.join(str(x) for x in free_rooms)}")
        final_result.append(f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}")
        return '\n'.join(final_result)

