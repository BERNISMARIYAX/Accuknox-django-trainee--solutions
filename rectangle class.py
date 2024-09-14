class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Function to get user input and create a Rectangle instance
def create_rectangle():
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers.")
        
        rect = Rectangle(length, width)
        return rect
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

# Example Usage
rectangle = create_rectangle()
if rectangle:
    for dimension in rectangle:
        print(dimension)
