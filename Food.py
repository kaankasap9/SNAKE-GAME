import turtle,random
def random_food():
    food = turtle.Turtle()
    food.color("red")
    food.penup()
    food.shape("circle")
    food.shapesize(1)
    random_xcor = random.randint(-250, 250)
    random_ycor = random.randint(-250, 250)
    food.goto(random_xcor,random_ycor)
    return food