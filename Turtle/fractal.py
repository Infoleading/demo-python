import turtle as tt

def draw_binary_tree(length, angle):
    if length < 3:
        return
    elif length < 21:
        tt.color("orange")
        tt.pensize(length*0.5)
    else:
        tt.color("green")
        tt.pensize(length*0.1)

    tt.pendown()
    tt.fd(length)

    tt.rt(angle)
    draw_binary_tree(length-10, angle)

    tt.lt(2*angle)
    draw_binary_tree(length-10, angle)

    tt.penup()
    tt.rt(angle)
    tt.bk(length)

if __name__ == '__main__':
    tt.setup(0.5, 0.7, 0, 0)
    tt.speed(0)
    tt.delay(0)
    tt.penup()
    tt.goto(0,-300)
    tt.pendown()
    tt.bgcolor("white")
    tt.seth(90)
    #tt.bgpic("nature.jpg")
    draw_binary_tree(100, 30)
    tt.done()
