# you will demonstrate class inheritance by creating a parent class for OfficeFurniture and a child class for Desk. You will instantiate and display an object for each class
# In the first step, you will create a parent class for OfficeFurniture
# Set the class variables to be a category (desk, chair, filing cabinet would be example values), material, length, width, height, and price. 
# Include a method that returns a string about the object. Implement the __str__ method
# In the second step create a subclass for Desk that includes location_of_drawers (left, right, both are options) and number_drawers.
# Override the parents __str__ method to include drawer location and count.
# Implement each class in a separate file. Import these into your main program. Your main program should implement and display an instance of each, the parent class and the c
import desk

class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
        

    # def __str__(self):
    #     return f'The {self.category} is made of {self.material} and is {self.length} inches long, {self.width} inches wide, {self.height} inches tall, and costs ${self.price}.'

    def set_category(self, category):
        self.category = category
        
    def set_material(self, material):
        self.material = material
    
    def set_length(self, length):
        self.length = length
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
        
    def set_price(self, price):
        self.price = price
    
    def get_category(self):
        return self.category

    def get_material(self):
        return self.material
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_price(self):
        return self.price
    
    
    
    
class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_of_drawers):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_of_drawers = number_of_drawers
        
    # def __str__(self):
    #     return f'The {self.category} is made of {self.material} and is {self.length} inches long, {self.width} inches wide, {self.height} inches tall, and costs ${self.price}. It has {self.number_of_drawers} drawers on the {self.location_of_drawers}.'
    
    def set_location_of_drawers(self, location_of_drawers):
        self.location_of_drawers = location_of_drawers
        
    def set_number_of_drawers(self, number_of_drawers):
        self.number_of_drawers = number_of_drawers
    
    def get_location_of_drawers(self):
        return self.location_of_drawers
    
    def get_number_of_drawers(self):
        return self.number_of_drawers
    
    def get_dimensions(self):
        return f'{self.length} x {self.width} x {self.height}'