import turtle as t
import rainbow as r

t.speed(0)
for i in range(500):
    RGB = r.HSB2RGB(i, 1.0, 1.0)
    t.pencolor(RGB[0], RGB[1], RGB[2])
    t.circle(i)
    t.left(5)