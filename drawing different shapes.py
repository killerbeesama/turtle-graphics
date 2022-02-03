from turtle import Turtle,Screen

t = Turtle()

def draw_shapes(times):
    for _ in range(times):
        t.forward(80)
        t.right(360/times)

times = 3
for _ in range(5):
    draw_shapes(times)
    times += 1


screen = Screen()
screen.exitonclick()
