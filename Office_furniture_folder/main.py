# you will demonstrate class inheritance by creating a parent class for OfficeFurniture and a child class for Desk. You will instantiate and display an object for each class
# In the first step, you will create a parent class for OfficeFurniture
# Set the class variables to be a category (desk, chair, filing cabinet would be example values), material, length, width, height, and price. 
# Include a method that returns a string about the object. Implement the __str__ method
# In the second step create a subclass for Desk that includes location_of_drawers (left, right, both are options) and number_drawers.
# Override the parents __str__ method to include drawer location and count.
# Implement each class in a separate file. Import these into your main program. Your main program should implement and display an instance of each, the parent class and the child class.


class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
        

    def __str__(self):
        return f'The {self.category} is made of {self.material} and is {self.length} inches long, {self.width} inches wide, {self.height} inches tall, and costs ${self.price}.'

    def set_category(self, category):
        self.__category = category
        
    def set_material(self, material):
        self.__material = material
    
    def set_length(self, length):
        self.__length = length
    
    def set_width(self, width):
        self.__width = width
    
    def set_height(self, height):
        self.__height = height
        
    def set_price(self, price):
        self.__price = price
    
    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material
    
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_price(self):
        return self.__price
    
    
    
class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_of_drawers):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_of_drawers = number_of_drawers
        
    def __str__(self):
        return f'The {self.category} is made of {self.material} and is {self.length} inches long, {self.width} inches wide, {self.height} inches tall, and costs ${self.price}. It has {self.number_of_drawers} drawers on the {self.location_of_drawers}.'
    
    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers
        
    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers
    
    def get_location_of_drawers(self):
        return self.__location_of_drawers
    
    def get_number_of_drawers(self):
        return self.__number_of_drawers
    
    
def main():
    parent_class = OfficeFurniture('desk', 'wood', 60, 30, 30, 200)
    child_class = Desk('desk', 'wood', 48, 30, 30, 100, 'left', 3)
    print(f"Category: {parent_class.get_category()}, Material: {parent_class.get_material()}, Length: {parent_class.get_length()}, Width: {parent_class.get_width()}, Height: {parent_class.get_height()}, Price: {parent_class.get_price()}")
    print(f"Category: {child_class.get_category()}, Material: {child_class.get_material()}, Length: {child_class.get_length()}, Width: {child_class.get_width()}, Height: {child_class.get_height()}, Price: {child_class.get_price()}, Location of Drawers: {child_class.get_location_of_drawers()}, Number of Drawers: {child_class.get_number_of_drawers()}")
    
main()
    
    
    
    


