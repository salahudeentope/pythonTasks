import math


def area_of_a_circle(radius=input('input the radius of the circle here in cm: ')):
    """"
    A python function to create a console program to compute the area of a circle 
    from user supplied input. The supplied input has a to a positive number and 
    cannot be a string.
    """""
    try:
        assert float(radius) >= 0
        area = math.pi * pow(float(radius), 2)
    except AssertionError:
        return 'The radius of the circle cannot be a negative number'
    except ValueError:
        return "The radius of the circle has to be a number not string"
    else:
        return f"Area of the circle with radius {radius}cm is {round(area, 2)}cm\u00b2"


if __name__ == '__main__':
    print(area_of_a_circle())
