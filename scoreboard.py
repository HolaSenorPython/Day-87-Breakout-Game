from turtle import Turtle # Import turtle class
FONT = ("Comic Sans MS", 36, "bold")
COLOR = "gold"

class ScoreBoard(Turtle): # Scoreboard will inherit from Turtle, making it a turtle object that we can mod

    def __init__(self):
        super().__init__()
        # Set the scoreboard's properties on init
        self.score = 0
        self.penup()
        self.hideturtle()
        # Now add a little black stroke
        self.setpos(-230, 280)
        self.color("black")
        self.write(arg=f"Score: {self.score}", font=FONT, align="center")
        # Write real colored text
        self.color(COLOR)
        self.goto(-225, 280) # Where to place the scoreboard text
        self.write(arg=f"Score: {self.score}", font=FONT, align="center")

    def point(self): # This is what will be done when user gains a point
        self.score += 1
        self.clear() # Clear all text
        # Now add a little black stroke
        self.setpos(-230, 280)
        self.color("black")
        self.write(arg=f"Score: {self.score}", font=FONT, align="center")
        # Write real colored text
        self.color(COLOR)
        self.goto(-225, 280)  # Where to place the scoreboard text
        self.write(arg=f"Score: {self.score}", font=FONT, align="center")

    def you_win(self): # Game over screen
        self.clear() # Clear all text
        self.color(COLOR)
        self.setpos(0, -50)
        self.write(arg=f"You win!\nFinal score: {self.score}", font=("Comic Sans MS", 40, "bold"), align="center")

    def game_over(self):
        self.clear()
        self.color("black")
        self.setpos(0, -50)
        self.write(arg=f"You Lose!\nFinal score: {self.score}", font=("Comic Sans MS", 40, "bold"), align="center")
