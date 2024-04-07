from turtle import Turtle
import random


class Food(Turtle):
    """
    Food class for snake game. Extends the Turtle class.
    """
    def __init__(self):
        """
        init food
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.random_color()
        self.speed("fastest")
        self.refresh()

    def random_color(self) -> None:
        """
        gives food a random color
        :return: None
        """
        colors = ["tomato", "spring green", "medium orchid", "white", "orange", "yellow", "deep sky blue"]
        self.pencolor(random.choice(colors))

    def refresh(self) -> None:
        """
        re-initializes food at a random place on the screen
        :return: None
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)