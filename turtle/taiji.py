from turtle import *

def drawTaiji(radius1, radius2, color1, color2):
    bgcolor("green")
    clear()
    penup()
    goto(0,radius1)
    pendown()

    seth(180)
    color(color1,color1)
    begin_fill()
    circle(radius1,180)
    seth(180)
    circle(-radius1/2,180)
    circle(radius1/2,180)
    end_fill()

    seth(0)
    color(color2,color2)
    begin_fill()
    circle(-radius1,180)
    circle(-radius1/2,180)
    circle(radius1/2,180)
    end_fill()

    penup()
    (x,y)=pos()
    goto(0,y-radius1/2-radius2)
    pendown()
    color(color2,color2)
    begin_fill()
    circle(-radius2,360)
    end_fill()
    penup()
    (x,y)=pos()
    goto(0,y-radius1)
    pendown()
    color(color1,color1)
    begin_fill()
    circle(-radius2,360)
    end_fill()

if __name__ == '__main__':
    reset()
    speed(1)
    drawTaiji(300,50,"white","black")
    done()

