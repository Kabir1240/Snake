from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


"""
Main logic for the snake game using Turtle Graphics.
:return: None
"""

# initializes the snake, food and scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# initializes the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# listens for user inputs and makes the snake act accordingly
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


def user_prompt():
    responses = ["continue", "c", "quit", "q"]
    prompt_response = screen.textinput(title="Quit?", prompt="Enter 'continue' to keep playing or 'quit' to exit")
    while prompt_response.lower() not in responses:
        prompt_response = screen.textinput(title="Invalid",
                                           prompt="Enter 'continue' to keep playing or 'quit' to exit")

    if prompt_response in responses[:2]:
        return False
    else:
        return True


# main game loop
collision_occurred = False
user_continue_game = False
while not collision_occurred:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        food.random_color()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() >= 295 or snake.head.xcor() <= -295 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295:
        score.game_over()
        collision_occurred = True
        user_continue_game = not user_prompt()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            collision_occurred = True
            user_continue_game = not user_prompt()

    if collision_occurred:
        if user_continue_game:
            snake.reset()
            score.reset_score()
            screen.listen()
            collision_occurred = False
        if not user_continue_game:
            snake.remove_snake()
            screen.update()


# exit
screen.exitonclick()
