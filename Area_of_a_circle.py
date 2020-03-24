import math


def area_of_a_circle(radius=input('input the radius of the circle here in cm: ')):
    area = math.pi * pow(float(radius), 2)
    return f"Area of the circle with radius {radius}cm is {round(area, 2)}cm\u00b2"


if __name__ == '__main__':
    print(area_of_a_circle())
