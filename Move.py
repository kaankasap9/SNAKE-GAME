import turtle
import time,CreateSnake,Food,Score

snake_parts=CreateSnake.snake_parts
screen=turtle.Screen()

def move():
    game_on = True
    turtle.color('red')
    style = ('Courier', 10, 'italic')
    turtle.penup()
    turtle.goto(150, 280)
    score = Score.SCORE
    higscore=Score.highscore
    food=Food.random_food()
    while game_on:
        turtle.write(f'SCORE İS : {score}    HİGHSCORE İS : {higscore} ', font=style, align='center')
        turtle.hideturtle()
        food_x = food.xcor()
        food_y = food.ycor()
        screen.update()
        time.sleep(0.1)
        if snake_parts[0].xcor()>280 or snake_parts[0].xcor()<-280 or snake_parts[0].ycor()>280 or snake_parts[0].ycor()<-280:
            return False
        for num in range(len(snake_parts)-1,0,-1):
            new_x = snake_parts[num-1].xcor()
            new_y = snake_parts[num - 1].ycor()
            snake_parts[num].goto(new_x,new_y)
        if (snake_parts[0].xcor()>food_x-20 and snake_parts[0].xcor()<food_x+20) and (snake_parts[0].ycor()>food_y-20 and snake_parts[0].ycor()<food_y+20):
            food.hideturtle()
            turtle.clear()
            score+=1
            if score>=int(higscore):
                higscore=score
                with open("highscore",mode="w") as file:
                    file.write(f"{score}")
                    file.close()
            food=Food.random_food()
            CreateSnake.eat()
        snake_parts[0].forward(20)
        x = CreateSnake.eat_self_control()
        if x == False:
            print("HIT THE TAİL GG")
            return False


