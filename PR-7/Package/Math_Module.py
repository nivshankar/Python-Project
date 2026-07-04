import math

def factorial_num():

    n = int(input("Enter Number : "))

    print("Factorial :", math.factorial(n))

def circle_area():

    r = float(input("Enter Radius : "))

    area = 3.14 * r * r

    print("Area :", area)

def trigono():

    a = float(input("Enter Angle : "))

    rad = math.radians(a)

    print("Sin :", math.sin(rad))
    print("Cos :", math.cos(rad))
