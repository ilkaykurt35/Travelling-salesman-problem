# Travelling-salesman-problem

We develop code to build a perspective on the traveling salesman problem with python

1) this program generates a random map of n points on a 2D plane.
2) accepts a random point as the starting point and creates the shortest possible route back to the starting point by traversing all points on the map
3) always proceeds by choosing the closest point first.
4) When it is equidistant from more than one point, it calculates the entire remaining path for each point that is equidistant and prefers the shortest one.
5) so it doesn't calculate the whole map over and over for each point
