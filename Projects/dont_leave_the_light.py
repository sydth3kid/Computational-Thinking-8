# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
s1 = create_sprite ("sydney" ,0,0)
s2 = create_sprite ("red circle" ,0,0)
set_background ("Black")
score=0

# Section 3: Controls
def up():
	s1.setheading(90)
	s1.forward(10)

def down():
	s1.setheading(270)
	s1.forward(10)

def left():
	s1.setheading(0)
	s1.forward(10)

def right():
	s1.setheading(180)
	s1.forward(10)

window.onkeypress (up, "w")
window.onkeypress (down, "s")
window.onkeypress (left, "d")
window.onkeypress (right, "a")
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()
lives = 3


while True:

	 
    
 	# TODO - code for automatic actions






	window.update()

	if lives == 0: 
		break
	

print("Game Over")


