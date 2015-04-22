from math import sin, cos, tan, radians
import copy


class GeoMath:
    EPS = 10 ** -6
    
    def eq(a, b):
        return abs(a - b) <= GeoMath.EPS
    
    def less(a, b):
        return a < b - GeoMath.EPS
    
    def greater(a, b):
        return a > b + GeoMath.EPS


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)
    
    def __str__(self):
        return "%s %s"%(self.x, self.y)
    
    def __repr__(self):
        return "Point(%s, %s)"%(self.x, self.y)
    
    def __eq__(self, other):
        return GeoMath.eq(self.x, other.x) and GeoMath.eq(self.y, other.y)
    
    def __add__(self, vector):
        return Point(self.x + vector.x, self.y + vector.y)
    
    def __radd__(self, vector):
        return self + vector
    
    def __sub__(self, vector):
        return Point(self.x - vector.x, self.y - vector.y)
    
    def __rsub__(self, vector):
        return self - vector
    
    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
    
    def rotate(self, centre, angle, rads=False):
        if not rads:
            angle = radians(angle)
        v = Vector(centre, self).rotate(angle, rads=True)
        return centre + v


class Vector:
    def __init__(self, first, second):
        if type(first) == Point:
            self.x = second.x - first.x
            self.y = second.y - first.y
        else:
            self.x = first
            self.y = second
    
    def __str__(self):
        return "%s %s"%(self.x, self.y)
    
    def __repr__(self):
        return "Vector(%s, %s)"%(self.x, self.y)
    
    def __eq__(self, other):
        return GeoMath.eq(self.x, other.x) and GeoMath.eq(self.y, other.y)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        elif type(other) == tuple:
            return Vector(self.x * other[0][0] + self.y * other[0][1], self.x * other[1][0] + self.y * other[1][1])
        else:
            return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, k):
        return Vector(self.x * k, self.y * k)
    
    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k)

    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
    
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __pow__(self, other):
        return self.x * other.y - self.y * other.x
    
    def rotate(self, angle, rads=False):
        if not rads:
            angle = radians(angle)
        sin_ = sin(angle)
        cos_ = cos(angle)
        return self * ((cos_, -sin_), (sin_, cos_))


class Line:
    def __init__(self, *args):
        if len(args) == 1:
            self.p1 = args[0].p1
            self.p2 = args[0].p2
        elif len(args) == 2:
            self.p1 = args[0]
            self.p2 = args[1]
        elif len(args) == 3:
            a, b, c = args
            if b != 0:
                self.p1 = Point(0, -c / b)
                self.p2 = Point(1, -(a + c) / b)
            else:
                self.p1 = Point(-c / a, 0)
                self.p2 = Point(-c / a, 1)
        else:
            self.p1 = Point(args[0], args[1])
            self.p2 = Point(args[2], args[3])
    
    def __contains__(self, point):
        return GeoMath.eq(Triangle(self.p1, self.p2, point).area(), 0)
    
    def intersections(self, other):
        if type(other) == Line:
            if GeoMath.eq(Vector(self.p1, self.p2) ** Vector(other.p1, other.p2), 0):
                if GeoMath.eq(Triangle(self.p1, self.p2, other.p1).area(), 0):
                    return float("inf")
                else:
                    return 0
            else:
                return 1
    
    def __eq__(self, other):
        return self.intersections(other) == float("inf")
    
    def __str__(self):
        return "%s %s %s %s"%(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
    def __repr__(self):
        return "Line(P(%s, %s), P(%s, %s))"%(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
    def equation(self):
        a = self.p2.y - self.p1.y
        b = self.p1.x - self.p2.x
        c = self.p2.x * self.p1.y - self.p1.x * self.p2.y
        return (a, b, c)
    
    def __and__(self, other):
        e1, e2 = self.equation(), other.equation()
        a1, b1, c1 = e1
        a2, b2, c2 = e2
        x = (b2 * c1 - c2 * b1) / (a2 * b1 - b2 * a1)
        y = (a2 * c1 - c2 * a1) / (b2 * a1 - a2 * b1)
        return Point(x, y)
    
    def perpendicular(self, point):
        lineVector = Vector(self.p1, self.p2)
        perpLineVector = Vector(-lineVector.y, lineVector.x)
        point2 = point + perpLineVector
        return Line(point, point2)


class Triangle:
    def __init__(self, *args):
        self.p = [None] * 3
        if len(args) == 3:
            self.p[0] = args[0]
            self.p[1] = args[1]
            self.p[2] = args[2]
        else:
            self.p[0] = Point(args[0], args[1])
            self.p[1] = Point(args[2], args[3])
            self.p[2] = Point(args[4], args[5])
    
    def __str__(self):
        return "%s %s %s %s %s %s"%(self.p[0].x, self.p[0].y, self.p[1].x, self.p[1].y, self.p[2].x, self.p[2].y)
    
    def __repr__(self):
        return "Triangle(P(%s, %s), P(%s, %s), P(%s, %s))"%(self.p[0].x, self.p[0].y, self.p[1].x, self.p[1].y, self.p[2].x, self.p[2].y)
    
    def area(self):
        vector1 = Vector(self.p[0], self.p[1])
        vector2 = Vector(self.p[0], self.p[2])
        return (vector1 ** vector2) / 2
    
    def median(self, num):
        M = Segment(self.p[(num + 1) % 3], self.p[(num - 1) % 3]).split(1)
        return Line(self.p[num], M)
    
    def medianCross(self):
        x = (self.p[0].x + self.p[1].x + self.p[2].x) / 3
        y = (self.p[0].y + self.p[1].y + self.p[2].y) / 3
        return Point(x, y)
    
    def bisectorCross(self):
        x1, x2, x3 = self.p[0].x, self.p[1].x, self.p[2].x
        y1, y2, y3 = self.p[0].y, self.p[1].y, self.p[2].y
        a, b, c = dist(self.p[1], self.p[2]), dist(self.p[0], self.p[2]), dist(self.p[0], self.p[1])
        
        x = (a * x1 + b * x2 + c * x3) / (a + b + c)
        y = (a * y1 + b * y2 + c * y3) / (a + b + c)
        return Point(x, y)
    
    def altitudeCross(self):
        side1 = Line(self.p[0], self.p[1])
        side2 = Line(self.p[0], self.p[2])
        alt1 = side1.perpendicular(self.p[2])
        alt2 = side2.perpendicular(self.p[1])
        return alt1 & alt2
    
    def outcircle(self):
        a = Segment(self.p[0], self.p[1])
        b = Segment(self.p[1], self.p[2])
        
        Ma = a.split(1)
        Mb = b.split(1)
        
        MHa = Line(a.p1, a.p2).perpendicular(Ma)
        MHb = Line(b.p1, b.p2).perpendicular(Mb)
        
        O = MHa & MHb
        r = dist(O, self.p[0])
        
        return Circle(O, r)


class Ray:
    def __init__(self, first, second):
        self.point = first
        if type(second) == Point:
            self.vector = Vector(first, second)
        else:
            self.vector = second
    
    def __str__(self):
        return "%s %s %s %s"%(self.point.x, self.point.y, self.vector.x, self.vector.y)
    
    def __repr__(self):
        return "Ray(P(%s, %s), V(%s, %s))"%(self.point.x, self.point.y, self.vector.x, self.vector.y)
    
    def __contains__(self, point):
        v = Vector(self.point, point)
        return GeoMath.eq(self.vector ** v, 0) and not GeoMath.less(self.vector * v, 0)


class Segment:
    def __init__(self, *args):
        if len(args) == 2:
            self.p1 = args[0]
            self.p2 = args[1]
        else:
            self.p1 = Point(args[0], args[1])
            self.p2 = Point(args[2], args[3])
    
    def __contains__(self, other):
        return other in Ray(self.p1, self.p2) and other in Ray(self.p2, self.p1)
    
    def __str__(self):
        return "%s %s %s %s"%(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
    def __repr__(self):
        return "Segment(P(%s, %s), P(%s, %s))"%(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    
    def split(self, ratio):
        x = (self.p1.x + ratio * self.p2.x) / (1 + ratio)
        y = (self.p1.y + ratio * self.p2.y) / (1 + ratio)
        return Point(x, y)
    
    def length(self):
        return dist(self.p1, self.p2)


class Polygon:
    def __init__(self, *args):
        if type(args[0]) == Point:
            self.points = args
        else:
            self.points = [Point(args[i * 2], args[i * 2 + 1]) for i in range(len(args) // 2)]
    
    def __repr__(self):
        return "Polygon(" + ", ".join(["P(%s, %s)"%(self.points[i].x, self.points[i].y) for i in range(len(self.points))]) + ")"
    
    def area(self):
        area = 0
        for i in range(len(self.points) - 1):
            area += Triangle(0, 0, self.points[i].x, self.points[i].y, self.points[i + 1].x, self.points[i + 1].y).area()
        area += Triangle(0, 0, self.points[-1].x, self.points[-1].y, self.points[0].x, self.points[0].y).area()
        return area
    
    def rotate(self, centre, angle, rads=False):
        if not rads:
            angle = radians(angle)
        points = [None] * len(self.points)
        for i in range(len(points)):
            points[i] = self.points[i].rotate(centre, angle, rads=True)
        return Polygon(points)

    def coords(self, offset, centre=None, angle=0, rads=False):
        if not centre:
            centre = Point(0, 0)
        if not rads:
            angle = radians(angle)

        coords = [None] * len(self.points) * 2
        for i in range(len(self.points)):
            if centre:
                pNew = self.points[i].rotate(centre, angle, rads=True)
            coords[i * 2] = pNew.x + offset.x
            coords[i * 2 + 1] = pNew.y + offset.y
        return coords


class Circle:
    def __init__(self, *args):
        if len(args) == 2:
            self.p = args[0]
            self.r = args[1]
        else:
            self.p = Point(args[0], args[1])
            self.r = args[2]
    
    def __str__(self):
        return "%s %s %s"%(self.p.x, self.p.y, self.r)
    
    def __repr__(self):
        return "Circle(P(%s, %s), %s)"%(self.p.x, self.p.y, self.s)
    
    def __and__(self, other):
        if type(other) == Line:
            distance = dist(self.p, other)
            if GeoMath.greater(distance, self.r):
                return []
            else:
                OH = Vector(other.p1, other.p2).rotate(90)
                OH /= OH.length()
                h = distance
                OH *= h
                H = self.p + OH
                if H not in other:
                    H = self.p - OH
                
                if GeoMath.eq(distance, self.r):
                    return [H]
                else:
                    oa = (self.r ** 2  - h ** 2) ** 0.5
                    OA = Vector(other.p1, other.p2)
                    OA /= OA.length()
                    OA *= oa
                    return [H + OA, H - OA]
        elif type(other) == Circle:
            distance = dist(self.p, other.p)
            r1, r2 = self.r, other.r
            O1, O2 = self.p, other.p
            if r1 < r2:
                r1, r2 = r2, r1
                O1, O2 = O2, O1
            O1O2 = Vector(O1, O2)
            
            if GeoMath.greater(distance, r1 + r2): # d > r1 + r2
                return []
            elif GeoMath.eq(distance, r1 + r2): # d = r1 + r2
                O1O2 = Vector(self.p, other.p)
                return [self.p + O1O2 / O1O2.length() * r1]
            elif GeoMath.less(distance, r1 + r2): # d < r1 + r2:
                if GeoMath.eq(distance, 0):    # d = 0:
                    if GeoMath.eq(r1, r2):     #     r1 = r2
                        return float("inf")
                    else:                      #     r1 != r2
                        return []
                elif GeoMath.less(distance, r1 - r2): # d < r1 - r2
                    return []
                elif GeoMath.eq(distance, r1 - r2):   # d = r1 - r2
                    return [O1 + O1O2 / O1O2.length() * r1]
                elif GeoMath.greater(distance, r1 - r2): # d > r1 - r2
                    o1h = (r1 ** 2 - r2 ** 2 + distance ** 2) / 2 / distance
                    O1H = O1O2 / O1O2.length() * o1h
                    H = O1 + O1H
                    h = (r1 ** 2 - o1h ** 2) ** 0.5
                    HA = O1H.rotate(90) / O1H.length() * h
                    return [H + HA, H - HA]      
    
    def tangentPoints(self, point):
        distance = dist(self, point)
        if GeoMath.less(distance, self.r):
            return []
        elif GeoMath.eq(distance, self.r):
            return [point]
        else:
            c = distance
            b = self.r
            a = (c ** 2 - b ** 2) ** 0.5
            
            x = a ** 2 / c
            h = a * b / c
            
            PO = Vector(point, self.p)
            PO /= PO.length()
            PH = PO * x
            H = point + PH
            PO.rotate(90)
            PO *= h
            A = H + PO
            B = H - PO
            return [A, B]



def dist(first, second):
    if type(first) == type(second) == Point:
        return Point.distance(first, second)
    elif type(first) == Line and type(second) == Point:
        t = Triangle(first.p1, first.p2, second)
        base = dist(first.p1, first.p2)
        return 2 * abs(t.area()) / base
    elif type(first) == Point and type(second) == Line:
        return dist(second, first)
    elif type(first) == Segment and type(second) == Point:
        segmV1 = Vector(first.p1, first.p2)
        segmV2 = -segmV1
        segmToPointV1 = Vector(first.p1, second)
        segmToPointV2 = Vector(first.p2, second)
        if GeoMath.less(segmV1 * segmToPointV1, 0):
            return dist(first.p1, second)
        elif GeoMath.less(segmV2 * segmToPointV2, 0):
            return dist(first.p2, second)
        else:
            return dist(Line(first.p1, first.p2), second)
    elif type(first) == Point and type(second) == Segment:
        return dist(second, first)
    elif type(first) == Circle and type(second) == Point:
        return dist(first.p, second)
    elif type(first) == Point and type(second) == Circle:
        return dist(second, first)