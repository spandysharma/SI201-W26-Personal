import math

class Rectangle():
    # Create the constructor "__init__" method

    # YOUR CODE HERE
    def __init__(self, user_width, user_height):
        self.width = user_width
        self.height = user_height


    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"



    # Create the "area_calculator" method

    # YOUR CODE HERE



    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE
    pass


    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()