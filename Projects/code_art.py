#begining
import turtle
#artstartshere
turtle.Screen(). bgcolor("black")
t = turtle.Turtle()
t2 = turtle.Turtle()
t.goto(0, 0)
t.color("yellow")
colors = ["pink","blue","green"]
t.speed(10)
for i in range(1000):
    t.forward(134 + i)
    t.left(70)
    t2.color( colors[i % 3 ])
    t2.forward( 123 + i )
    t2.left( 60 + 1 )

#end
turtle.exitonclick()