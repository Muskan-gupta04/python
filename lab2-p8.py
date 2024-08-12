
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

sides = sorted([a, b, c])
a, b, c = sides

if c**2 == a**2 + b**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
