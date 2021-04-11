import CreateSnake
snake_parts = CreateSnake.snake_parts
def turn_down():
    if snake_parts[0].heading()!=90:
        snake_parts[0].shape("snake_down_30.gif")
        snake_parts[0].setheading(270)

