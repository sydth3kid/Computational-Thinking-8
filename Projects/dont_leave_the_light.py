# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, random, time
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
s2 = create_sprite ("unnamed" ,0,0)
s1 = create_sprite ("syd" ,0,0)
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

# def game_end():

# TODO - pick keys for each control

# Section 4: Game Loop


window.listen()
lives = 3




timer = 0
while True:
	timer +=1
	 
    
 	# TODO - code for automatic actions

	s2.setheading(random.randint(0, 360))
	time.sleep(0.1)
	s2.forward(20)
	
	#for i in range (30)

	if get_distance(s1,s2) > 100:
		lives -=1
	if s2.xcor()>250:
		s2.goto(250,s2.ycor())

	if s2.ycor()>250:
		s2.goto(s2.xcor(),250)

	if s2.xcor()<-250:
		s2.goto(-250,s2.ycor ())

	if s2.ycor()<-250:
		s2.goto(s2.xcor(),-250)


	

	window.update()
	if timer == (500):
		break
	if lives == 0:
		break
print("Game Over!")