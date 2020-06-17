import turtle as tt
import rainbow as rb

def drawStar(angle=0, rate=0):
    hue = 0
    tt.seth(angle)
    tt.goto(0,0)
    for i in range(500):
        tt.fd(i)
        tt.rt(144)
        hue += rate
        RGB = rb.HSB2RGB(hue, 1.0, 1.0)
        tt.pencolor(RGB[0], RGB[1], RGB[2])
        hue+=3


if __name__ == "__main__":
    tt.screensize(800,600)
    tt.bgcolor('white')
    tt.speed(0)
    angle = 0
    tt.hideturtle()
    rate=1
    while True:
        tt.clear()
        tt.tracer(False)
        drawStar(angle, rate)
        tt.update()
        angle += 1
        rate += 1
    tt.done()
