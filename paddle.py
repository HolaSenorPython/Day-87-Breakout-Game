import turtle as t
WHITE = "#FFFFFF" # GET THE WHITE COLOR like in MAIN.PY
FULL_PADDLE_Y = -220
STARTING_POSITIONS = [(-40, FULL_PADDLE_Y), (-20, FULL_PADDLE_Y), (0, FULL_PADDLE_Y),
                      (20, FULL_PADDLE_Y), (40, FULL_PADDLE_Y)]
MOVE_DISTANCE = 20

class Paddle:
    # On initialization do this
    def __init__(self):
        self.FULL_PADDLE = [] # Will contain list of turtle objects later
        self.make_paddle() # do make paddle method
        self.paddle_tip = self.FULL_PADDLE[0] # Define where the head of the paddle is for movement
        self.move_d = MOVE_DISTANCE # This is an attribute that will hold the move distance value, can change later

    def make_paddle(self):
        for pos in STARTING_POSITIONS:
            self.add_paddle_piece(pos)

    def add_paddle_piece(self, position):
        paddle_piece = t.Turtle()
        paddle_piece.penup()
        paddle_piece.seth(180)
        paddle_piece.color(WHITE)
        paddle_piece.shape("square")
        paddle_piece.setpos(position)
        self.FULL_PADDLE.append(paddle_piece)

    def left(self):
        if self.FULL_PADDLE[0].xcor() > -335: # If the tip of the paddle's x cord is more than -300
            for piece in self.FULL_PADDLE:
                piece.goto(piece.xcor() - self.move_d, piece.ycor())

    def right(self):
        if self.FULL_PADDLE[-1].xcor() < 335: # If the TAIL of the paddle's x cord is less than 300
            for piece in self.FULL_PADDLE:
                piece.goto(piece.xcor() + self.move_d, piece.ycor())

    def get_faster(self): # Paddle will increase speed to be able to catch ball lol
        factor = 1.15 # 15% increase in speed
        self.move_d *= factor
