import turtle

window = turtle.Screen()
window.bgcolor("blue")

def draw_square():
	v=0
	while  v<4:
		brad.forward(100)
		brad.right(90)
		v=v+1

def draw_triangle():
	i=0
	while i<3:
		azert.forward(100)
		azert.right(120)
		i=i+1

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(2)
draw_square()

angle = turtle.Turtle()
angle.shape("arrow")
angle.color("green")
angle.circle(100)

azert = turtle.Turtle()
azert.shape("circle")
azert.color("black")
draw_triangle()

window.exitonclick()

#--------------------------------------------------

import turtle


def draw_square(tur):
	for x in xrange(1,5):
		tur.forward(100)
		tur.right(100)

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





