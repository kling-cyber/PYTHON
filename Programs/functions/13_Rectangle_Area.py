# 13. Calculate Area of Rectangle

def rectangle_area(length, width):
    return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Area =", rectangle_area(length, width))
