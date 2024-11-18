import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Circle Area (radius=3):", circle_area(3))
