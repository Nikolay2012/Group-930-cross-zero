'''
    
'''

import turtle 

t1 = turtle.Turtle()
t1.width(3)
t1.speed(0)
t1.hideturtle()

def draw_table():
    x_cor = 0
    y_cor = 0
    # малюємо три квадрати в один ряд
    for count2 in range(3):
        for count1 in range(3):
            t1.penup()
            t1.goto(x_cor, y_cor)
            t1.pendown()
            #малюємо один квадрат
            for count in range(4):
                t1.left(90)
                t1.forward(100)
            x_cor += 100 
        x_cor = 0
        y_cor -= 100
        
