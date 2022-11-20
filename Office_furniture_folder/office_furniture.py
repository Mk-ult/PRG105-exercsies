# you will demonstrate class inheritance by creating a parent class for OfficeFurniture and a child class for Desk. You will instantiate and display an object for each class
# In the first step, you will create a parent class for OfficeFurniture
# Set the class variables to be a category (desk, chair, filing cabinet would be example values), material, length, width, height, and price. 
# Include a method that returns a string about the object. Implement the __str__ method
# In the second step create a subclass for Desk that includes location_of_drawers (left, right, both are options) and number_drawers.
# Override the parents __str__ method to include drawer location and count.
# Implement each class in a separate file. Import these into your main program. Your main program should implement and display an instance of each, the parent class and the c

class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
    
    # Mutator Methods

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
    
    def __str__(self):
        return "\nCategory: " + self.__category + "\nMaterial: " + self.__material + "\nLength: " + str(self.__length) + "\nWidth: " + str(self.__width) + "\nHeight: " + str(self.__height) + "\nPrice: $" + str(self.__price)
    