import turtle as t

def HSB2RGB(h, s, v):
    h1 = h%360
    hi = int((h1)/60)%6
    f = h1/60- hi
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    RGB = [0.0, 0.0, 0.0]

    if hi==0:
        RGB = [v, t, p]
    elif hi==1:
        RGB = [q, v, p]
    elif hi==2:
        RGB = [p, v, t]
    elif hi==3:
        RGB = [p, q, v]
    elif hi==4:
        RGB = [t, p, v]
    elif hi==5:
        RGB = [v, p, q]

    return RGB

def rainbow():
    hue = 0.0
    t.color(1, 0, 0)
    t.hideturtle()
    t.speed(100)
    t.pensize(3)
    t.penup()
    t.goto(-400, -300)
    t.pendown()
    t.right(110)
    for i in range(110):
        t.circle(1000)
        t.right(0.13)
        hue += 3
        RGB = HSB2RGB(hue, 1.0, 1.0)
        t.color(RGB[0], RGB[1], RGB[2])
    t.penup()

if __name__ == '__main__':
    t.screensize(400,300)
    t.colormode(1.0)
    rainbow()
    t.done()
