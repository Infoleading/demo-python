import turtle as tt
import rainbow as rb
import time

def drawHelix(angle, colorRating):
    hue = 0.0
    for i in range(500):
        hue += colorRating
        RGB = rb.HSB2RGB(hue, 1.0, 1.0)
        tt.color(RGB[0], RGB[1], RGB[2])
        tt.fd(i)
        tt.rt(angle)

def drawGalaxy():
    hue = 0.0
    for i in range(10000):
        hue += 0.3
        RGB = rb.HSB2RGB(hue, 1.0, 1.0)
        tt.color(RGB[0], RGB[1], RGB[2])
        tt.fd(i/20)
        tt.rt(i*8)

def drawGalaxy2():
    hue = 0.0
    for j in range(4):
        for i in range(500):
            tt.pendown()
            hue += 0.3
            RGB = rb.HSB2RGB(hue, 1.0, 1.0)
            tt.color(RGB[0], RGB[1], RGB[2])
            tt.fd(i/20)
            tt.rt(i*8)
        tt.penup()
        tt.goto(0,0)
        tt.seth(0)
        tt.rt((j+1)*90)

def animateHelix(velocity):
    tt.speed(0) # 作图速度 0-10, 10最快，0不限速
    tt.delay(0) # 内部延迟, 置0可以加速
    heading = 0
    rating = 0
    tt.tracer(False)
    tt.hideturtle()
    while True:
        tt.penup()
        tt.clear()
        tt.goto(0,0)
        tt.pendown()
        tt.seth(heading)
        #drawHelix(144, heading) # 转动五角星
        drawHelix(240, rating)
        tt.update()
        #time.sleep(0.001)
        heading+=velocity
        rating+=0.4

if __name__ == '__main__':
    tt.setup(0.5, 0.8, 0, 0)
    tt.speed(0)
    tt.bgcolor("green")
    tt.penup()
    tt.goto(0, 0)
    tt.pendown()
    tt.tracer()
    drawGalaxy2()
    #drawHelix(89, 0.5)
    #animateHelix(1)
    tt.update()
    tt.done()
