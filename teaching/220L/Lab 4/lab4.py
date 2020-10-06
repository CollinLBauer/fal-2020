# Name: <your name>
# lab4.py

from graphics import *


def patterns():
	print("Generates the first n elements of several patterns.")
	num_elements = int(input("How many elements do you want to see? "))
	functions = [pattern_a, pattern_b, pattern_c, pattern_d, pattern_e]
	for func in functions:
		func(num_elements)


def pattern_a(n):
	print("Pattern A: ", end='')
	for i in range(n):
		print(2 * i + 2, end=' ')
	print()


def pattern_b(n):
	print("Pattern B: ", end='')


def pattern_c(n):
	print("Pattern C: ", end='')


def pattern_d(n):
	print("Pattern D: ", end='')


def pattern_e(n):
	print("Pattern E: ", end='')


def draw_shapes():
	# how many times the user can move the circle
	NUM_CLICKS = 5

	# create the window
	width = 800
	height = 400
	win = GraphWin("Drawing Shapes", width, height)

	# display instructions
	instr_pt = Point(width / 2, height - 10)
	instructions = Text(instr_pt, "Click to move circle")
	instructions.draw(win)
	
	# build the circle
	shape = Circle(Point(50, 50), 20)
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	
	# allow the user to click multiple times
	for i in range(NUM_CLICKS):
		pt = win.getMouse()
		center = shape.getCenter()

		# move amount is the distance from center to the click point
		dx = pt.getX() - center.getX()
		dy = pt.getY() - center.getY()
		shape.move(dx, dy)

	# clean up
	instructions.setText("Click again to close")
	win.getMouse()
	win.close()


def main():
	patterns()
	# hw_stats()
	# draw_shapes()


main()
