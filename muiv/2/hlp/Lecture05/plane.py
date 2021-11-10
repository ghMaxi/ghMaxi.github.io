import math

from airport import Airport
from window import LabelObject


class Plane(LabelObject):
    def __init__(self, id, start_airport: Airport):
        self.x = start_airport.x
        self.y = start_airport.y
        self.id = id
        self.target_airport = None
        self.start_airport = start_airport
        self.window = None

    def fly_to(self, target_airport: Airport, window):
        self.target_airport = target_airport
        self.window = window
        window.display(self)
        window.after(1000, self.step)

    def step(self):
        dir = self.target_airport.x - self.x, self.target_airport.y - self.y
        sq_distance = dir[0] ** 2 + dir[1] ** 2
        if sq_distance < 1:
            self.reached_target()
        else:
            distance = math.sqrt(sq_distance)
            self.x += dir[0] / distance
            self.x += dir[1] / distance
            self.window.after(1000, self.step)

    def reached_target(self):
        self.x = self.target_airport.x
        self.y = self.target_airport.y
        new_target = self.start_airport
        self.start_airport = self.target_airport
        self.fly_to(new_target, self.window)

    @property
    def symbol(self):
        return '✈'
