import turtle


def draw_square(tur):
	for x in xrange(1,5):
		tur.forward(90)
		tur.right(90)

def draw ():
	window = turtle.Screen()
	window.bgcolor("blue")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	i=1
	while  i<40 :
		draw_square(brad)
		brad.right(10)
		i=1+1
	window.exitonclick()
	
draw()

