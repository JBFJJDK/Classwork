x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
if (x1 == x2 and y1 < y2):
    print("You have entered two points that failed to create a rectangle. Exiting the program")
else:
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    result = (x > x1 and x < x2 and y > y1 and y < y2)
    print(result)