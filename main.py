import turtle
import CreateSnake,Move,TurnLeft,TurnRight,turn_up,turn_down,lose_screen
screen=turtle.Screen()
turtle.register_shape("snake_down_30.gif")
turtle.register_shape("snake_up_30.gif")
turtle.register_shape("snake_right_30.gif")
turtle.register_shape("snake_left_30.gif")
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.onkey(key="Left", fun=TurnLeft.turn_left)
screen.onkey(key="Right", fun=TurnRight.turn_right)
screen.onkey(key="Up", fun=turn_up.turn_up)
screen.onkey(key="Down", fun=turn_down.turn_down)
snake=CreateSnake
move_obj=Move
game_on=True
snake.create_snake()
while game_on==True:
    screen.tracer(0)
    x=move_obj.move()
    if x==False:
        game_on=False
screen.clear()
lose_screen.lose()