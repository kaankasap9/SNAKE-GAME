import CreateSnake
snake_parts=CreateSnake.snake_parts

def turn_right():

    if snake_parts[0].heading()!=180 and snake_parts[0].heading()!=0 :
        snake_parts[0].shape("snake_right_30.gif")
        if snake_parts[0].heading()==270:
            snake_parts[0].left(90)
        else:
            snake_parts[0].right(90)