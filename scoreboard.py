from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    """
    Scoreboard class for snake game to keep track of the players score. Extends the Turtle class
    """
    def __init__(self):
        """
        Init the scoreboard. Writes the score at the top of the screen.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update()

    def update(self) -> None:
        """
        clears previous score and updates the text to the new score
        :return: None
        """
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        """
        Increments the score by 1 and updates the screen
        :return: None
        """
        self.score += 1
        self.update()

    def game_over(self) -> None:
        """
        Notifies the player that the game has ended and prints out the final score underneath.
        :return: None
        """
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)