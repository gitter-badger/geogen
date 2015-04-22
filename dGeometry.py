from Geometry import *

def _drawPoint(self, canvas, size=3):
    canvas.create_circle(self.x, self.y, size, fill="black", outline="black")
Point.draw = _drawPoint

def _drawCircle(self, canvas):
    canvas.create_circle(self.p.x, self.p.y, self.r, fill="", outline="black")
Circle.draw = _drawCircle

def _drawSegment(self, canvas):
    canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
Segment.draw = _drawSegment

def _drawTriangle(self, canvas):
    canvas.create_polygon(self.p[0].x, self.p[0].y, self.p[1].x, self.p[1].y, self.p[2].x, self.p[2].y, fill="", outline="black")
Triangle.draw = _drawTriangle

def _drawLine(self, canvas):
    s = Segment(self & Line(0, 0, 0, 1), self & Line(500, 500, 500, 501))
    s.draw(canvas)
Line.draw = _drawLine

def _drawVector(self, canvas, start):
    canvas.create_line(start.x, start.y, self.x + start.x, self.y + start.y)
Vector.draw = _drawVector