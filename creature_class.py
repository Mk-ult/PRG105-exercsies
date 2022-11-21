# Download the file creature_class.py Download creature_class.py a description of the class Creature.
# Using the class Creature for the parent class, create a sub-class of Creature called Orc.
# Orc should have attributes for weapon (string), max_hit_points (integer), and current_hit_points (integer)
# Create appropriate setter and getter methods and an appropriate __str__() method.
# For all Orcs, the friendly attribute should be set to False and the type_of_creature should be "Orc".

# Then, using the class Orc for the parent class, create a sub-class of Orc called OrcBoss
# OrcBoss should include attributes for name (string) and a special_move (string).
# Create appropriate setter and getter methods and an appropriate __str__() method.
# You will then create a simple program that creates an instance of each of the three classes and uses the __str__() method to display them


class Creature:
    def __init__(self, type_of_creature, friendly, position, image):
        # type_of_creature is a short string
        self.type_of_creature = type_of_creature
        # friendly should have a True/False value
        self.friendly = friendly
        # The position should be a tuple like (x, y, z) where x, y, z are integers
        self.position = position
        # The image should be a string holding an image name
        self.image = image

    # mutators (setters)
    def set_type_of_creature(self, type_of_creature):
        self.type_of_creature = type_of_creature

    def set_friendly(self, friendly):
        self.friendly = friendly

    def set_position(self, position):
        self.position = position

    def set_image(self, image):
        self.image = image

    # accessors (getters)
    def get_type_of_creature(self):
        return self.type_of_creature

    def get_friendly(self):
        return self.friendly

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

    # return a string describing the creature
    def __str__(self):
        if self.friendly:
            description = f"This friendly {self.type_of_creature} is located at "
        else:
            description = f"This unfriendly {self.type_of_creature} is located at "
        return description + str(self.position) + " and uses the image asset: " + str(self.image)

class Orc(Creature):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points):
        super().__init__("Orc", False, position, image)
        self.weapon = weapon
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points
    
    def set_weapon(self, weapon):
        self.weapon = weapon
    
    def set_max_hit_points(self, max_hit_points):
        self.max_hit_points = max_hit_points
    
    def set_current_hit_points(self, current_hit_points):
        self.current_hit_points = current_hit_points
    
    def get_weapon(self):
        return self.weapon
    
    def get_max_hit_points(self):
        return self.max_hit_points
    
    def get_current_hit_points(self):
        return self.current_hit_points
    
    def __str__(self):
        description = f"This Orc uses a(n) {self.weapon} and has HP: {self.current_hit_points}/{self.max_hit_points}.\n"
        description += super().__str__()
        return description
    
class OrcBoss(Orc):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points, name, special_move):
        super().__init__(position, image, weapon, max_hit_points, current_hit_points)
        self.name = name
        self.special_move = special_move
    
    # setters for OrcBoss attributes
    def set_name(self, name):
        self.name = name
    
    def set_special_move(self, special_move):
        self.special_move = special_move
    
    # getters for OrcBoss attributes
    def get_name(self):
        return self.name
    
    def get_special_move(self):
        return self.special_move
    
    # return a string describing the creature
    def __str__(self):
        description = f"{self.name} is an Orc boss with {self.special_move} as a special move.\n"
        description += super().__str__()
        return description

def main():
    
    creature1 = Creature("rabbit", False, (10, 250, 10), "bunnies.gif")
    creature2 = Orc((-100, 200, 50), "orc.gif", "axe", 150, 150)
    creature3 = OrcBoss((-100, 200, 50), "orc.gif", "sword", 350, 200, "Austin", "Fireball")

    print(creature1)
    print()
    print(creature2)
    print()
    print(creature3)
    print()
    
main()