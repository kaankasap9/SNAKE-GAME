from turtle import Turtle
snake_parts=[]
STARTİNG_CORX = [0, -20, -40]
def eat_self_control():
    for index in range(1,len(snake_parts)):
            if (snake_parts[0].xcor()>snake_parts[index].xcor()-5 and snake_parts[0].xcor()<snake_parts[index].xcor()+5) and (snake_parts[0].ycor()>snake_parts[index].ycor()-5 and snake_parts[0].ycor()<snake_parts[index].ycor()+5):
                return False
def eat():
    for i in range(0,3):
        tail = snake_parts[-1]
        new_part=Turtle()
        new_part.penup()
        new_part.shape("square")
        new_part.color("green")
        new_part.speed("fastest")
        new_xcor=tail.xcor()-1
        new_ycor=tail.ycor()-1
        new_part.goto(new_xcor,new_ycor)
        snake_parts.append(new_part)
def create_snake():
    for index in range(0, 3):
        turtle = Turtle()
        if index==0:
            turtle.shape("snake_right_30.gif")
        else:
            turtle.shape("square")
        turtle.color("green")
        turtle.penup()
        turtle.speed("fastest")
        turtle.goto(STARTİNG_CORX[index], 0)
        snake_parts.append(turtle)
def reset():
    snake_parts.clear()
    create_snake()