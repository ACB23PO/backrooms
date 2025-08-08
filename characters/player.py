from objects.game_object import GameObject
from characters.inventory import Inventory

class Player:
    max_health = 100
    max_thirst = 100

    def __init__(self, health=100, thirst=0, start_pos = (0,0)):
        self._health = health
        self._inventory = {
            # "crumpled_note" : 
        }
        self._start_pos = start_pos
        self._thirst = thirst

    @staticmethod
    def die(reason : str):
        print(f"You died from {reason}")
        play_state = input("Play again? (Type P to play or Q to quit!) ").lower
        match play_state:
            case "p":
                #TODO
                print("plays game again...")
            case "q":
                print("Exiting game...")
                raise SystemExit

    @property
    def health(self):
        return self._health

    def display_health(self):
        return f"Your current health is : {self.health()}"

    @health.setter
    def health(self, new_health, health_changer):
        if self.health() + new_health == 0:
            self.die(health_changer)
        elif self.health() + new_health > Player.max_health:
            self.health() = Player.max_health
        else:
            self.health() += new_health

        if new_health > 0:
            print(f"You healed, your new health is {self.health()}")
        elif new_health < 0:
            print(f"You took some damage from {health_changer}")
        else:
            print("Your health was not changed...")

    @property
    def thirst(self):
        return self.thirst()
    
    @staticmethod
    def display_thirst(self):
        if self.thirst() == 0:
            return f"You are not thirsty."
        elif self.thirst() >= 50:
            return f"You are slightly thirsty."
        elif self.thirst() >= 80:
            return f"You are running very low on water"
        elif self.thirst() >= 100:
            self.die("thirst")

    @thirst.setter
    def thirst(self, new_thirst):
        if self.thirst() + new_thirst == 100:
            self.die("thirst")

    @property 
    def inventory(self):
        return self._inventory
