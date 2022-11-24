"""This is a module to be shared"""
from math import sqrt
from point import Point as pt
def calculate_distance(point_a, point_b):
    """this funtion computes the distance btw point a and b"""
    return sqrt((point_a.getX()-point_b.getX())**2 +(point_a.getY()-point_b.getY())**2)

def prompt_for_point():
    x_value=float(input("inserire la x..."))
    y_value=float(input("inserire la y..."))
    return pt(x_value,y_value) #il Point() è un problema perche non lo conosce [ho un return Point(x_value,y_value)]