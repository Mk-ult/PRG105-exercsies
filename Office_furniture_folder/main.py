# you will demonstrate class inheritance by creating a parent class for OfficeFurniture and a child class for Desk. You will instantiate and display an object for each class
# In the first step, you will create a parent class for OfficeFurniture
# Set the class variables to be a category (desk, chair, filing cabinet would be example values), material, length, width, height, and price. 
# Include a method that returns a string about the object. Implement the __str__ method
# In the second step create a subclass for Desk that includes location_of_drawers (left, right, both are options) and number_drawers.
# Override the parents __str__ method to include drawer location and count.
# Implement each class in a separate file. Import these into your main program. Your main program should implement and display an instance of each, the parent class and the child class.
import office_furniture
import desk
    
    
def main():
    parent_class = office_furniture.OfficeFurniture('chair', 'wood', "60 inches", "30 inches", "30 inches", "200.00")
    child_class = desk.Desk('desk', 'oak', "48 inches", "30 inches", "30 inches", "$100.00" , 'left', "3")
    print(parent_class)
    print()
    print(child_class)


main()