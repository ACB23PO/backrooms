from room import Room
from objects.items.key import Key
from characters.player import Player

class LockedRoom(Room):
    def __init__(self, key_required : Key, room_name, room_position, room_objects=..., locked_state=True):
        super().__init__(room_name, room_position, room_objects)
        self._locked_state = locked_state

    def try_unlock_room(self, player : Player):
        if player.inventory().GetItem(self.key_required):
            print(f"Used {self.key_required}")
            self._locked_state = False
            print("Unlocked the door!")