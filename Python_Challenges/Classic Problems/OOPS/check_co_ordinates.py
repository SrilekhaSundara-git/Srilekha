class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_a_rectangle(self, lowleft, upright):#=Point(3, 4)
        if lowleft[0] < self.x < upright[0] \
          and lowleft[1] < self.y < upright[1]:
            return True
        return False
    
    def distance_from_points(self, x, y):
        return ((self.x-x)**2 + (self.y-y)**2)**0.5

    def distance_from_pointse(self, points):
        return ((self.x-points.x)**2 + (self.y-points.y)**2)**0.5



point = Point(3, 4)
point_2 = Point(1, 2)
print(Point(3, 4).x)
print(point.x)
print(Point(5, 6).y)
print(point.y)

print(point.falls_in_a_rectangle((5, 6), (1, 2)))
print(point.distance_from_points(1,2))
print(point.distance_from_points(point_2.x, point_2.y))
print(point.distance_from_pointse(point_2))