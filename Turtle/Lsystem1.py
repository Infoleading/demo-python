from turtle import *

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
    speed(0)
    tracer(False)
    setup(1600, 820, 0, 0)
    screensize(6000, 6000, None)
    up()
    forward(-500)
    
    length = [50, 100, 60, 100, 40, 100, 100]
    angle = [90, 45, 60, 90, 90, 90, 90]
    path = [
        'F-F-F-F',
        'F',
        'F++F++F',
        '-F',
        'F+F+F+F',
        'F-F-F-F',
        'F-F-F-F'
        ]
    rule = [
        'F-F+F+FF-F-F+F',
        'F-F++F-F',
        'F-F++F-F',
        'F+F-F-F+F',
        'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',
        'FF-F-F-F-FF',
        'FF-F--F-F'
        ]
    t=6  # 测试案例 [0, ~]
    power = 4 # 应用规则次数 [0,~]
    for i in range(power):
        path[t] = apply_rule(rule[t],path[t])
    

    draw_path(path[t], length[t]/2**power, angle[t])
    exitonclick()
