import time
import random
from rooms.room import Room

class Map:
    def __init__(self, map_name="MAP_NAME", map_description="THIS IS A MAP"):
        self._map_name = map_name
        self._map_description = map_description
        self.map_matrix = ()
    
    def __str__(self):
        print("----------------------------------------------------------")
        print("[You hear a low somber voice echo in your ears]")
        time.sleep(4)
        print("[Eyes still adjusting, you barely make out the words...]")
        time.sleep(4)
        print("'UNKNOWN: welcome stranger, fancy seeing a human down here.'")
        time.sleep(4)
        print("'I'm sorry, I truly am. There is no escape, don't bother.'")
        time.sleep(4)
        print(f"'Escaping from {self._map_name} HA!'")
        time.sleep(4)
        print(f"'This is a {self._map_description}'")
        time.sleep(4)
        print("[You wake up.]")
        print("----------------------------------------------------------")
        return "LOADING..."

    @staticmethod
    def generate_map(self):
        print("GENERATING MAP...")

        for row in self.map_matrix:
            for column in row:
                pass
                #self.map_matrix.append(room)
    
    @staticmethod
    def random_room():
        pass