import turtle as t
import rainbow as rb

i = 0
t.speed(0)
while i<500:
    hue = i
    RGB = rb.HSB2RGB(hue, 1.0, 1.0)
    t.color(RGB[0], RGB[1], RGB[2])
    t.forward(i)
    t.left(121)
    i = i+3