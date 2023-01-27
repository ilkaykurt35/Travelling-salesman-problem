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

for i in range(10):
    Point(''.join(random.choice(string.ascii_lowercase) for i in range(3)), random.randint(10,100), random.randint(10,100))

x = []
y = []
n = []
startPoint = Point.listOfInstances[0]
x.append(startPoint.x)
y.append(startPoint.y)
n.append(startPoint.name)
startPoint.visited = True

i = 0
pt = startPoint
while i < len(Point.listOfInstances)-1:
    pt = pt.nearestPoint()
    x.append(pt.x)
    y.append(pt.y)
    n.append(pt.name)
    pt.visited = True
    i+=1

x.append(startPoint.x)
y.append(startPoint.y)
