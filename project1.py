from dGeometry import *
from tkinter import *
import random

print('Random points?')
randomness = input()
if randomness == 'No' or randomness == 'NO' or randomness == 'no':
    randomness = 'No'
    print('A:')
    A = Point(*map(int, input().split()))
    print('B:')
    B = Point(*map(int, input().split()))
    print('C:')
    C = Point(*map(int, input().split()))
    print('Thank you!')
    AB = Vector(A, B)
    BC = Vector(B, C)
    if AB ** BC == 0:
        randomness = 'Yes'
        
font = ('Cleargothic', '15', 'bold')

def _create_circle(self, x, y, r, **kwargs):
        self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
Canvas.create_circle = _create_circle

def _draw(self, other, *args):
        other.draw(self, *args)
Canvas.draw = _draw

def medians(event):
        canv.draw(medianAC)
        canv.draw(medianBC)
        canv.draw(medianAB)

def medls(event):
        canv.draw(medLineA)
        canv.draw(medLineC)
        canv.draw(medLineB)

GeoMath.EPS = 10 ** -7

root = Tk()
canv = Canvas(root, width = 750, height = 750, bg = 'white')

all_points = []
all_segments = []

AB = Vector(Point(1, 1), Point(1, 1))
BC = Vector(Point(1, 1), Point(1, 1))

while AB ** BC == 0 and randomness != 'No':
    A = Point(random.randrange(10, 740), random.randrange(10, 740))
    B = Point(random.randrange(10, 740), random.randrange(10, 740))
    C = Point(random.randrange(10, 740), random.randrange(10, 740))
    AB = Vector(A, B)
    BC = Vector(B, C)
    AC = Vector(A, C)

AB = Segment(A, B)
AC = Segment(A, C)
BC = Segment(B, C)

all_points.extend([(A, 'A'), (B, 'B'), (C, 'C')])
all_segments.extend([(AB, 'AB'), (BC, 'BC'), (AC, 'AC')])

Ma = Point(abs(B.x + C.x) / 2, abs(B.y + C.y) / 2)
Mb = Point(abs(A.x + C.x) / 2, abs(A.y + C.y) / 2)
Mc = Point(abs(B.x + A.x) / 2, abs(B.y + A.y) / 2)
medianBC = Segment(A, Ma)
medianAC = Segment(B, Mb)
medianAB = Segment(C, Mc)

all_points.extend([(Ma, "Ma"), (Mb, "Mb"), (Mc, 'Mc')])
all_segments.extend([(medianBC, "AMa"), (medianAC, "BMb"), (medianAB, 'CMc')])

ABC = Triangle(A, B, C)
M = ABC.medianCross()
all_points.extend([(M, "M")])

for point in all_points:
        canv.create_text(point[0].x, point[0].y, text=point[1], fill='red', font=font)
        
canv.draw(AC)
canv.draw(BC)
canv.draw(AB)
canv.pack()

MMa = Segment(M, Ma)
MMb = Segment(M, Mb)
MMc = Segment(M, Mc)
all_segments.extend([(MMa, "MMa"), (MMb, "MMb"), (MMc, 'MMc')])

medLineA = Segment(Mb, Mc)
medLineB = Segment(Ma, Mc)
medLineC = Segment(Mb, Ma)
all_segments.extend([(medLineC, "MaMb"), (medLineA, "MbMc"), (medLineB, 'McMa')])

AM = Segment(A, M)
BM = Segment(B, M)
CM = Segment(C, M)
all_segments.extend([(AM, "AM"), (BM, "BM"), (CM, 'CM')])

AMb = Segment(A, Mb)
BMc = Segment(B, Mc)
CMa = Segment(C, Ma)
all_segments.extend([(AMb, "AMb"), (BMc, "BMc"), (CMa, 'CMa')])

AMc = Segment(A, Mc)
BMa = Segment(B, Ma)
CMb = Segment(C, Mb)
all_segments.extend([(AMc, "AMc"), (BMa, "BMa"), (CMb, 'CMb')])

button1 = Button(root, text = 'Medians')
button1.bind('<Button-1>', medians)
button1.pack()

button2 = Button(root, text = 'Medium lines')
button2.bind('<Button-1>', medls)
button2.pack()

for i in range(len(all_segments)):
    for j in range(i + 1, len(all_segments)):
        if GeoMath.eq(all_segments[i][0].length(), all_segments[j][0].length()):
            print(all_segments[i][1] + '=' + all_segments[j][1])

root.mainloop()