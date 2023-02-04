import turtle

t4 = turtle.Turtle()
t4.width(5)
t4.color("darkgreen")
t4.speed(0)
t4.hideturtle()

def draw_line(x, y):
    t4.penup()
    t4.goto(x, y)
    t4.pendown()
    t4.goto(x + 200, y)
    

    