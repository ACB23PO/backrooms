import time

class Map:
    def __init__(self, map_name, map_description):
        self._map_name = map_name
        self._map_description = map_description
        self.map_array = ()
        print("------------------------------")
        print("You hear a low somber voice echo in your ears")
        print("Eyes still adjusting, you barely make out the words...")
        print("UNKNOWN: welcome stranger, fancy seeing a human down here.")
        time.sleep(1)
        print("I'm sorry, I truly am. There is no escape, don't bother.")
        time.sleep(1)
        print("Escaping from {self.map_name} HA!")
        time.sleep(1)
        print(self._map_description)
        time.sleep(1)
        print("You wake up.")

    @staticmethod
    def create_map(self):
        for room in self.map_array:
            pass