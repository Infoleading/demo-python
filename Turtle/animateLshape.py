from turtle import *
from time import *
from rainbow import *

def draw_path(path, length, angle):
    for symbol in path:
        if symbol == 'F':
            down()
            forward(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)
        elif symbol == 'f':
            up()
            forward(length)
            
def apply_rule(rule, path):
    return path.replace('F', rule)


if __name__ == "__main__":
    # setup canva
    setup(1920, 990, -1, 0)
    screensize(6000, 3000, None)
    tracer(False)
    hideturtle()
    speed(0)
    up()
    goto(-200,0)
    bgcolor("#000000")
    # define model
    length = [50, 100, 60, 100, 200, 200, 100]
    angle = [90, 45, 60, 90, 90, 90, 90]
    path = [
        'F-F-F-F',
        'F',
        'F++F++F',
        'F-F-F-F',
        'F-F-F-F',
        'F-F-F-F',
        'F-F-F-F'
        ]
    rule = [
        'F-F+F+FF-F-F+F',
        'F-F++F-F',
        'F-F++F-F',
        'FF-F--F-F',
        'F-F+F-F-F',
        'F-FF--F-F',
        'FF-F-F-F-FF'
        ]
    # define test
    t=6  # 测试案例
    power = 3 # 应用规则次数 [0,~]
    # generate path
    for i in range(power):
        path[t] = apply_rule(rule[t],path[t])
    # animate
    head = 0
    hue = 0
    while True:
        clear()
        seth(head)
        RGB=HSB2RGB(hue, 1.0, 1.0)
        color(RGB[0], RGB[1], RGB[2])
        fillcolor(RGB[0], RGB[1], RGB[2])
        #begin_fill()
        draw_path(path[t], length[t]/2**power, angle[t])
        #end_fill()
        update()
        head+=1
        hue+=1
        sleep(0.001)
    exitonclick()