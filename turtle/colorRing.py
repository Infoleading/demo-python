import turtle as tt
import rainbow as rb

def drawRing(accuracy, width):
    hue = 0.0
    tt.pensize(width+1)
    for i in range(20):
        radius = 300-i*width # 每次画圆的半径都减小width个象素，
        for j in range(int(360/accuracy)):
            hue += accuracy
            RGB = rb.HSB2RGB(hue, 1.0, 1.0)
            #print(str(hue)+"->"+str(RGB))
            tt.color(RGB[0], RGB[1], RGB[2])
            tt.circle(radius, accuracy)
        tt.penup()
        x,y=tt.pos()
        tt.sety(y+width)  # 画下一个圆时上移 width 象素
        tt.pendown()

if __name__ == '__main__':
    tt.screensize(400, 300)
    tt.speed(0) # 作图速度 0-10, 10最快，0不限速
    tt.delay(0) # 内部延迟, 置0可以加速
    tt.hideturtle()
    tt.tracer(True) # 作图过程（轨迹）不显示
    tt.penup()
    tt.setpos(0,-300)
    tt.pendown()
    drawRing(1,10) # 第一参数色环精度， 第二参数色环宽度
    tt.update() # 刷新画面
    tt.done()
