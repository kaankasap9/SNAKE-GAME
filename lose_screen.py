import turtle
def lose():
    screen=turtle.Screen()
    screen.bgcolor("black")
    turtle.color('red')
    style = ('Courier', 30, 'italic')
    turtle.write('YOU LOSE!', font=style, align='center')
    turtle.hideturtle()
    screen.exitonclick()
