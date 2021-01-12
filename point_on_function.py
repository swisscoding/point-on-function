#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Check if point is on function graph | ----\n", fg("red")))

# options
print(stylize("Options:", fg("green")))
print("'1' for linear function (f(x) = mx + q)\n'2' for second grade quadratic function (f(x) = ax² + bx + c)\n'3' for simple exponential function (f(x) = abˣ)\n")

# user interaction
choice = input(": ")
point = [float(i) for i in input("Point (x, y): ").rstrip().split(", ")]

# functions
def linear(point):
    print("\nFunction => f(x) = mx + q")
    slope = float(input("Enter slope (m): "))
    intercept = float(input("Enter y intercept (q): "))
    if slope * point[0] + intercept == point[1]:
        return 1
    return stylize(f"\nPoint ({point[0]}, {point[1]}) is not on this linear function.\n", fg("red"))

def quadratic(point):
    print("\nFunction => f(x) = ax² + bx + c")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    if a * point[0]**2 + b * point[0] + c == point[1]:
        return 1
    return stylize(f"\nPoint ({point[0]}, {point[1]}) is not on this quadratic function.\n", fg("red"))

def exponential(point):
    print("\nFunction => f(x) = abˣ")
    a = float(input("a: "))
    b = float(input("b: "))
    if a * b**point[0] == point[1]:
        return 1
    return stylize(f"\nPoint ({point[0]}, {point[1]}) is not on this exponential function.\n", fg("red"))

# output
if choice == "1":
    result = linear(point)
    if result == 1:
        print(stylize(f"\nPoint ({point[0]}, {point[1]}) is on this linear function.\n", fg("green")))
    else:
        print(result)

elif choice == "2":
    result = quadratic(point)
    if result == 1:
        print(stylize(f"\nPoint ({point[0]}, {point[1]}) is on this quadratic function.\n", fg("green")))
    else:
        print(result)

elif choice == "3":
    result = exponential(point)
    if result == 1:
        print(stylize(f"\nPoint ({point[0]}, {point[1]}) is on this exponential function.\n", fg("green")))
    else:
        print(result)

else:
    exit("\nInvalid Input\n")
