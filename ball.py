import turtle as t
GOLD = "#d6b606"

class Ball:
    # On initialization of this ball...
    def __init__(self):
        self.ball = t.Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color(GOLD)
        self.x_move = 5 # X increment to move by
        self.y_move = 5 # Y increment to move by

    def move_ball(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_pos(self):
        self.ball.goto(0, -200) # Reset the ball's pos to next to paddle

    def get_faster(self):
        factor = 1.20 # 20% increase in speed
        self.x_move *= factor
        self.y_move *= factor
