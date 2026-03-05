# my answer
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        self.distance_from_xy(self.__x, self.__y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        return sum(self.__points)

point1 = Point(0, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_point(point3))
# print(point3.distance_from_point(point1))

triangle = Triangle(point1.distance_from_point(point2), point2.distance_from_point(point3), point3.distance_from_point(point1))
print(triangle.perimeter())

# THE REAL ANSWER
# import math

# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         print(self.__vertices)
#         per = 0
#         for i in range(3):
#             per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
#             print((i + 1) % 3)
#         return per


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())
    
    