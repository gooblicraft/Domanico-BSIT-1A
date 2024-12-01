class Dog:
    """A simple dog class"""
    
    def __init__(self, name, age):
        """Initialize the attributes of name and age"""
        
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate sitting command for the dog"""
        
        print(f"{self.name} is now sitting")
        
    def rolled_over(self):
        """Simulate rolling command for the dog"""
        
        print(f"{self.name} rolled over")
        

my_dog = Dog('Jayvee', 5)

print(f"My dog {my_dog.name} age is {my_dog.age}")

class Restaurant:
    def __init__(self, name, type, year):
        self.name = name
        self.type = type
        self.year = year
        
    def detailed_info(self):
        info = f"NAME: {self.name}, TYPE: {self.type}, YEAR: {self.year}"
        return info.title()
    
my_restaurant = Restaurant('Paplap', 'coffee', 2023)

print(my_restaurant.detailed_info())