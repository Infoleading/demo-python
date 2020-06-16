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
    speed(0)
    tracer(True)
    length = [50, 100, 60, 60]
    angle = [90, 45, 60, 45]
    path = [
        'F-F-F-F',
        'F',
        'F++F++F',
        'FF-F++++F--F++++F-FF++++'
        ]
    rule = [
        'F-F+F+FF-F-F+F',
        'F-F++F-F',
        'F-F++F-F',
        'FF-F++++F--F++++F-FF++++'
        ]
    t=3  # 测试案例
    power = 3 # 应用规则次数 [0,~]
    for i in range(power):
        path[t] = apply_rule(rule[t],path[t])
        
    draw_path(path[t], length[t]/2**power, angle[t])
    exitonclick()