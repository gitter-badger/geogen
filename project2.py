from dGeometry import *
from tkinter import *
import random

noes = ['NO', 'no', 'No', 'nO']
yeses = ['YES', 'YEs', 'YeS', 'Yes', 'yES', 'yEs', 'yeS', 'yes']

print('Create points randomly?')
randomness = input()
if randomness in noes:
    randomness = 'No'
    print('Each coordinate must be greater than 9 but lesser than 741')
    print('Each coordinate must be an integer')
    print('A:')
    A = Point(*map(int, input().split()))
    print('B:')
    B = Point(*map(int, input().split()))
    print('C:')
    C = Point(*map(int, input().split()))
    AB = Vector(A, B)
    BC = Vector(B, C)
    if AB ** BC == 0:
        print('Yor points are on the single line!')
        print('Points will be randomly created')
        randomness = 'Yes'

if randomness not in yeses and randomness not in noes:
    print('You have written something unreadable')
    print('Points will be randomly created')
    randomness = 'Yes'

if randomness == 'No':
    temp = [A.x, A.y, B.x, B.y, C.x, C.y]
    for element in temp:
            if element > 740:
                print('One of your coordinates is too big!')
                print('Points will be randomly created')
                randomness = 'Yes'
                break
            if element < 10:
                print('One of your coordinates is too small!')
                print('Points will be randomly created')
                randomness = 'Yes'
                break

temp = True
del temp

if randomness in noes:
        print('Thank you!')
        
font = ('Cleargothic', '12', 'bold')

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
        canv.draw(MbXa)
        canv.draw(McXb)
        canv.draw(MaXc)
        canv.draw(MbXc)
        canv.draw(McXa)
        canv.draw(MaXb)
        canv.draw(MbYa)
        canv.draw(McYb)
        canv.draw(MaYc)
        canv.draw(MbYc)
        canv.draw(McYa)
        canv.draw(MaYb)       
        
def biss(event):
        canv.draw(AIa)
        canv.draw(BIb)
        canv.draw(CIc)

GeoMath.EPS = 10 ** -5

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

ab = AB.length()
bc = BC.length()
ac = AC.length()

all_points.extend([(A, 'A'), (B, 'B'), (C, 'C')])
all_segments.extend([(AB, 'AB'), (BC, 'BC'), (AC, 'AC')])

Ma = Point(abs(B.x + C.x) / 2, abs(B.y + C.y) / 2)
Mb = Point(abs(A.x + C.x) / 2, abs(A.y + C.y) / 2)
Mc = Point(abs(B.x + A.x) / 2, abs(B.y + A.y) / 2)
medianBC = Segment(A, Ma)
medianAC = Segment(B, Mb)
medianAB = Segment(C, Mc)

Ia = Point(C.x - (C.x - B.x) * ac / (ac + ab), C.y - (C.y - B.y) * ac / (ac + ab))
Ib = Point(A.x - (A.x - C.x) * ab / (bc + ab), A.y - (A.y - C.y) * ab / (bc + ab))
Ic = Point(B.x - (B.x - A.x) * bc / (bc + ac), B.y - (B.y - A.y) * bc / (bc + ac))

temp = 1 / (bc / (ac + ab))
I = Point((A.x + temp * Ia.x) / (1 + temp), (A.y + temp * Ia.y) / (1 + temp))
del temp

AIa = Segment(A, Ia)
BIb = Segment(B, Ib)
CIc = Segment(C, Ic)
AI = Segment(A, I)
BI = Segment(B, I)
CI = Segment(C, I)
IIa = Segment(I, Ia)
IIb = Segment(I, Ib)
IIc = Segment(I, Ic)
AIb = Segment(A, Ib)
BIc = Segment(B, Ic)
CIa = Segment(C, Ia)
AIc = Segment(A, Ic)
BIa = Segment(B, Ia)
CIb = Segment(C, Ib)

all_segments.extend([(IIa, "IIa"), (IIb, "IIb"), (IIc, 'IIc')])
all_segments.extend([(AIa, "AIa"), (BIb, "BIb"), (CIc, 'CIc')])
all_segments.extend([(AIc, "AIc"), (BIa, "BIa"), (CIb, 'CIb')])
all_segments.extend([(AIb, "AIb"), (BIc, "BIc"), (CIa, 'CIa')])
all_segments.extend([(AI, "AI"), (BI, "BI"), (CI, 'CI')])
all_points.extend([(Ia, "Ia"), (Ib, "Ib"), (Ic, 'Ic')])

line_AIa = Line(AIa)
line_BIb = Line(BIb)
line_CIc = Line(CIc)

all_points.extend([(Ma, "Ma"), (Mb, "Mb"), (Mc, 'Mc')])
all_segments.extend([(medianBC, "AMa"), (medianAC, "BMb"), (medianAB, 'CMc')])

ABC = Triangle(A, B, C)
M = ABC.medianCross()

all_points.extend([(M, "M"), (I, 'I')])
        
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

line_MaMb = Line(medLineC)
line_McMa = Line(medLineB)
line_MbMc = Line(medLineA)

Xa = line_AIa & line_MaMb
Xb = line_BIb & line_MbMc
Xc = line_CIc & line_McMa

Ya = line_AIa & line_McMa
Yb = line_BIb & line_MaMb
Yc = line_CIc & line_MbMc

MbXa = Segment(Mb, Xa)
McXa = Segment(Mc, Xa)
MaXb = Segment(Ma, Xb)
McXb = Segment(Mc, Xb)
MaXc = Segment(Ma, Xc)
MbXc = Segment(Mb, Xc)

MbYa = Segment(Mb, Ya)
McYa = Segment(Mc, Ya)
MaYb = Segment(Ma, Yb)
McYb = Segment(Mc, Yb)
MaYc = Segment(Ma, Yc)
MbYc = Segment(Mb, Yc)

all_segments.extend([(MbXa, "MbXa"), (McXb, "McXb"), (MaXc, 'MaXc')])
all_segments.extend([(MbXc, "MbXc"), (McXa, "McXa"), (MaXb, 'MaXb')])
all_points.extend([(Xa, "Xa"), (Xb, "Xb"), (Xc, 'Xc')])

all_segments.extend([(MbYa, "MbYa"), (McYb, "McYb"), (MaYc, 'MaYc')])
all_segments.extend([(MbYc, "MbYc"), (McYa, "McYa"), (MaYb, 'MaYb')])
all_points.extend([(Ya, "Ya"), (Yb, "Yb"), (Yc, 'Yc')])


for point in all_points:
        canv.create_text(point[0].x, point[0].y, text=point[1], fill='red', font=font)

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

button3 = Button(root, text = 'Bisectors')
button3.bind('<Button-1>', biss)
button3.pack()

for i in range(len(all_segments)):
    for j in range(i + 1, len(all_segments)):
        if GeoMath.eq(all_segments[i][0].length(), all_segments[j][0].length()):
            print(all_segments[i][1] + '=' + all_segments[j][1])

print('Press Medians button to show medians')
print('Press Medium lines button to show medium lines')
print('Press Bisectors button to show bisectors')

root.mainloop()