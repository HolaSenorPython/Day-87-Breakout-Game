from turtle import Screen
from paddle import Paddle # Import the Paddle class from paddle.py
from ball import Ball # Import Ball class from ball.py
from brick_manager import BrickManager # Import Brickmanager class from the file
from scoreboard import ScoreBoard # Import Scoreboard class from scoreboard
from lives import Lives # Import the LIVES class from lives
import time # Use later for updating screen and stuff
#----------SCREEN AND UI SETUP---------#
BLUE = "#005EB8"
WHITE = "#FFFFFF"
screen = Screen()
screen.setup(width=700, height=700)
screen.colormode(255)
screen.bgcolor(BLUE)
screen.title("Breakout!")
screen.tracer(0)
#---------OBJECT INITIALIZING AND SCREEN RESPONSE--------#
paddle = Paddle()
ball = Ball()
brick_manager = BrickManager()
scoreboard = ScoreBoard()
lives = Lives()
screen.listen() # Screen should listen for key presses!
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")
#---------GAME LOGIC----------#
game_on = True
brick_manager.make_bricks() # Make all the bricks before starting while loop
while game_on:
    # Keep screen updating
    time.sleep(0.0167) # About 60 FPS according to ChatGPT
    screen.update()
    ball.move_ball() # Keep that ball moving

    # Detect ball collision with WALL and ceiling
    if ball.ball.xcor() <= -330 or ball.ball.xcor() >= 330:
        ball.bounce_x()
    elif ball.ball.ycor() >= 320: # If ball hits ceiling, bounce
        ball.bounce_y()

    # Detect ball collision with paddle
    for segment in paddle.FULL_PADDLE: # Loop through every paddle piece, and if the ball is close enough to one, bounce
        if ball.ball.distance(segment) <= 20 and ball.y_move < 0: # ALso ensure the ball is moving down towards paddle
            ball.bounce_y()                                                     # before bouncing (has a negative y)

    # Detect ball collision with BRICK
    for brick in brick_manager.all_bricks: # Loop through EVERY BRICK
        if ball.ball.distance(brick) <= 30: # If a ball is close enough...
            ball.bounce_y() # Ball should bounce
            brick.hideturtle() # Hide the brick from screen
            brick_manager.delete_brick(brick) # Delete that brick/turtle from the list permanently 😈
            scoreboard.point() # Add a point to the score!

    # Detect ball going off-screen (bottom)
    if ball.ball.ycor() <= -330:
        lives.lose_life() # You lose a life
        ball.reset_pos() # Send it back
        ball.bounce_y() # Face upwards
        time.sleep(1) # Wait a second

    # If your score is divisible by 10, and NOT 0, make the game harder (ball faster)
    if scoreboard.score % 10 == 0 and scoreboard.score != 0:
        scoreboard.score += 1 # Add an extra point so it doesn't get stuck, but also as bonus
        ball.get_faster() # Increase ball speed
        paddle.get_faster() # Increase paddle speed

    # If there are no more bricks, end the game (YOU WIN!)
    if len(brick_manager.all_bricks) == 0:
        scoreboard.you_win()
        game_on = False

    # If there are no more LIVES... (YOU LOSE GAME OVER)
    if lives.lives == 0:
        scoreboard.game_over()
        game_on = False

screen.exitonclick() # keep window open, similar to main loop in tkinter
