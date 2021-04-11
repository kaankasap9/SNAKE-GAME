import CreateSnake
snake_parts=CreateSnake.snake_parts
def turn_up():
    if snake_parts[0].heading()!=270:
        snake_parts[0].shape("snake_up_30.gif")
        snake_parts[0].setheading(90)

