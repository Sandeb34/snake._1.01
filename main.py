# Old school snake game
from turtle import Screen
import time
from snake_game import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake eater")
screen.tracer(0)

# snake OBJECT Creates a snake from snake Class.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()   # Food goes to  new location
        snake.extend()   # After the snake will extend with one segment
        scoreboard.increase_score()

#     Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset()

# detect collision with tail. This loops through the list of segments
# and checks the distance of the snake's head in relation to the snake's body
# We sliced the list of snake.segments skip the first (snake head)
for segment in snake.segments:
    if segment == snake.head:
        pass
    elif snake.head.distance(segment) < 10:
        scoreboard.reset()
        snake.reset()



screen.exitonclick()


















screen.exitonclick()