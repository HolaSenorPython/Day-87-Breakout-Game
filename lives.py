from turtle import Turtle # Import turtle class
COLOR = "red"
FONT = ("Comic Sans MS", 36, "bold")

class Lives(Turtle): # Inherit from turtle
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.penup()
        self.hideturtle()
        # Add black stroke
        self.color("black")
        self.setpos(230, 280)
        self.write(arg=f"Lives: {self.lives}", font=FONT, align="center")
        # Now write colored text
        self.color(COLOR)
        self.goto(225, 280)  # Where to place the scoreboard text
        self.write(arg=f"Lives: {self.lives}", font=FONT, align="center")

    def lose_life(self):
        self.lives -= 1
        self.clear() # Clear all text
        # Add black stroke
        self.color("black")
        self.setpos(230, 280)
        self.write(arg=f"Lives: {self.lives}", font=FONT, align="center")
        # Now write colored text
        self.color(COLOR)
        self.goto(225, 280)  # Where to place the scoreboard text
        self.write(arg=f"Lives: {self.lives}", font=FONT, align="center")