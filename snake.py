from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Snake class for the snake game. Snake is a list of several Turtle objects. segments[0] is the head.
    """
    def __init__(self):
        """
        init the snake.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        """
        Creates the snake. Initially 3 Turtle objects right next to each other.
        :return: None
        """
        x = 0
        for i in range(3):
            self.add_segment((x, 0))
            x -= 20

    def extend(self) -> None:
        """
        Extends the snake by one block.
        :return: None
        """
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position) -> None:
        """
        Adds a segment to the snake
        :param position: position to initialize the new Turtle object
        :return: None
        """
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def move(self) -> None:
        """
        Moves the snake forward
        :return: None
        """
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        """
        Turns the snake head upwards
        :return: None
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """
        Turns the snake head Downwards
        :return: None
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """
        Turns the snake head left
        :return: None
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """
        Turns the snake head right
        :return: None
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)