from turtle import *

def draw_path(path, length, angle):
    for symbol in path:
        if symbol == 'F':
            forward(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)
            
def apply_rule(rule, path):
    return path.replace('F', rule)


if __name__ == "__main__":
    setup(1920, 990, -1, 0)
    screensize(6000, 3000, None)
    tracer(True)
    speed(0)
    length = [50, 100, 60, 500]
    angle = [90, 45, 60, 90]
    path = [
        'F-F-F-F',
        'F',
        'F++F++F',
        'F-F-F-F'
        ]
    rule = [
        'F-F+F+FF-F-F+F',
        'F-F++F-F',
        'F-F++F-F',
        'F-FF--F+F'
        ]
    t=2  # 测试案例
    power = 3 # 应用规则次数 [0,~]
    for i in range(power):
        path[t] = apply_rule(rule[t],path[t])
        
    draw_path(path[t], length[t]/2**power, angle[t])
    exitonclick()