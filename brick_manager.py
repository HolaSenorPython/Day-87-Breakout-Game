import turtle as t # A TURTLE IS ABOUT 20 BY 20, so lets try and make rows of brick objects
STARTING_X = -330 # Starting X value to make bricks from
X_INCREMENT = 60
Y_COORDS_PER_COLOR = [260, 240, 220, 200, 180, 160] # Ycoords for all the bricks
COLORS = ["#FF0000", # Red
          "#FF7F00", # Orange
          "#FFFF00", # Yellow
          "#00FF00", # Green
          "#00FFFF", # Cyan / aqua blue
          "#8B00FF"  # Violet
          ] # colors of the rainbow

class BrickManager:

    def __init__(self):
        self.all_bricks = []
        self.start_x = STARTING_X
        self.x_increment = X_INCREMENT
        self.y_coords_per_color = Y_COORDS_PER_COLOR
        self.colors = COLORS

    def make_bricks(self):
        designated_y_coord = 0 # starting index for the y cord list
        for color in self.colors: # For every color in colors
            for i in range(12): # Make a turtle, set its position to the starting X and increase by 60 (the x increment)
                                    # Because that is the size of a brick, and we don't want over-lapping bricks
                brick = t.Turtle() # We do this 12 times ( A perfect fit would be 11 and 2/3s, but We want it to look right)
                brick.penup()
                brick.shape("square")
                brick.shapesize(1, 3)
                brick.color(color)
                brick.setpos(self.start_x, self.y_coords_per_color[designated_y_coord])
                self.all_bricks.append(brick) # Add the brick to the all bricks list
                self.start_x += self.x_increment # Increase the starting x in the loop, so same color bricks move along the axis
            designated_y_coord += 1 # Move down for the next color, by changing the index when getting that list
            self.start_x = STARTING_X # Reset the starting x, so they all get made from same x cord

    def delete_brick(self, brick):
        self.all_bricks.remove(brick)