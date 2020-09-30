# Name: <your name>
# lab5.py

from graphics import *


def converter():
    # Authors: RoxAnn H. Stalvey, Walter Pharr, Anthony Morrell
    # Illustrates getting numeric input through graphics window
    width = 300
    height = 200
    win = GraphWin("Unit Conversion", width, height)

    # Specify the message for the input box
    box_desc = Text(Point(100, 50), "Input: ")
    box_desc.draw(win)

    # Create the Entry object and set its default text to a number
    #   allowing the user to see what type of value is expected
    input_box = Entry(Point(200, 50), 5)
    input_box.setText("0")
    input_box.draw(win)

    # Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    # This button isn't necessary, but it makes a nice point for the user
    #   to click. If you click anywhere in the window, the code reacts
    #   the same way.
    btn_x = width / 2
    btn_y = height / 2
    button = Text(Point(btn_x, btn_y), "Click")
    button.draw(win)
    border = Rectangle(Point(btn_x - 35, btn_y - 20), Point(btn_x + 35, btn_y + 20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover input and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    input_value = eval(input_box.getText())

    # Display output and change button
    output.setText("value entered = " + str(input_value))
    button.setText("Quit")

    # Wait for another click to exit
    win.getMouse()
    win.close()


def map_plan():
    width = 800
    height = 600
    win = GraphWin("Complex Location Planner", width, height)

    # Draw the background map
    # Make sure that north-charleston.gif is in the same folder as
    #   this Python file
    background = Image(Point(width/2, height/2), "north-charleston.gif")
    background.draw(win)

    # Add your code here:

    # Wait for click to close the window
    win.getMouse()
    win.close()
