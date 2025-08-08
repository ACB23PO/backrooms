class Room:
    def __init__(self, room_name, room_position, room_objects = []):
        self._room_name = room_name
        self._room_position = room_position
        self._room_objects = room_objects

    def inspect_room(self):
        for room_object in self._room_objects:
            print(room_object, end=", ")