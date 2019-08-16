#!/usr/bin/env python2
"""
    Barrier class.

"""

from config import BARRIER_COLOR

class Barrier:
    """ The barrier class implementation. """
    stroke_weight = 2
    barrier_color = BARRIER_COLOR
    
    def __init__(self, start_point, end_point, barrier_color=barrier_color):
        """ Initialization of the barrier object. It's represented as a line segment."""
        self.p1 = start_point.copy()
        self.p2 = end_point.copy()

        self.slope = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        self.prependicular_slope = -1 / (self.slope+.001)

        self.length = self.p1.dist(self.p2)

        self.b1 = self.p2.y - self.slope * self.p2.x

        self.barrier_color = barrier_color

    def show(self):
        """ Draw the barrier object on the screen. """
        stroke(self.barrier_color)
        strokeWeight(self.stroke_weight)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def on_line(self, vector, tolorance=3):
        """ checks whether the given point vector(PVector) is on the barrier or not. """
        d1 = self.p1.dist(vector)
        d2 = self.p2.dist(vector)

        return abs(self.length - d1 - d2) < tolorance

    def point_distance(self, vector):
        """ Returns the shortest distance between the given point vector(PVector) and the barrier object. """
        b2 = vector.y - self.prependicular_slope * vector.x

        P = PVector()
        P.x = (self.b1 - b2) / (self.prependicular_slope - self.slope)
        P.y = self.slope * P.x + self.b1

        return P.dist(vector)
    
    def collision(self, vector, tolorance=3):
        """ Returns true if the given point vector(PVector) collides with the barrier object. """
        d = self.point_distance(vector)
        return d <= tolorance and self.on_line(vector)
