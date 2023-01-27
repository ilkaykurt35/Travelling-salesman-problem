import math
import numpy as np
import matplotlib.pyplot as plt
import random
import string

class Point():
    listOfInstances = []
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.visited = False
        Point.listOfInstances.append(self)
    def calculateWay(self):
        pass
    def nearestPoint(self):
        distances = []
        instances = []
        for i in Point.listOfInstances:
            if i.visited == False and i is not self:
                distances.append(Point.distanceBetweenPoints(self, i))
                instances.append(i)
        if distances.count(min(distances)) > 1:
            # return self.calculateWay()
            return instances[distances.index(min(distances))]
        else:
            return instances[distances.index(min(distances))]
        
    @staticmethod
    def distanceBetweenPoints(a,b):
        ab = math.sqrt((abs(a.x-b.x))**2+(abs(a.y-b.y))**2)
        return ab 