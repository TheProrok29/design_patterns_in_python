from structural.composite.point import Point
from structural.composite.segment import Segment
from structural.composite.triangle import Triangle

point_a1 = Point(3, 5)
point_a2 = Point(10, 10)

point_a1.move(-1, -3)
print('///////////////')
point_b1 = Point(-3, 1)
point_b2 = Point(7, 11)

point_c1 = Point(1, 0)
point_c2 = Point(0, 1)

seg1 = Segment(point_a1, point_a2)
seg2 = Segment(point_b1, point_b2)
seg3 = Segment(point_c1, point_c2)

seg2.move(5, 5)
print('///////////////')

triangle = Triangle(seg1, seg2, seg3)
triangle.move(11.5, 12.25)
