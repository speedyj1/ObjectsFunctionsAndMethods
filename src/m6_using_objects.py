"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jack Speedy.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    #two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()
    centerpoint = rg.Point(100, 100)
    radius = 30
    circle = rg.Circle(centerpoint, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    centerpoint2 = rg.Point(200, 200)
    radius2 = 25
    circle2 = rg.Circle(centerpoint2, radius2)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()
    x_coordinate = 300
    y_coordinate = 100
    center = rg.Point(x_coordinate, y_coordinate)
    radius = 30
    circle = rg.Circle(center, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    point1x = 100
    point1y = 150
    point2x = 200
    point2y = 50
    point1 = rg.Point(point1x, point1y)
    point2 = rg.Point(point2x, point2y)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.fill_color = 'red'
    rectangle.attach_to(window)
    window.render()
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(x_coordinate)
    print(y_coordinate)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print((point1x + point2x)/2, (point1y + point2y)/2)
    print((point1x + point2x)/2)
    print((point1y + point2y)/2)
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()
    x1 = 50
    y1 = 50
    x2 = 100
    y2 =100
    start1 = rg.Point(x1, y1)
    end1 = rg.Point(x2, y2)
    line1 = rg.Line(start1, end1)
    line1.attach_to(window)
    x2_1 = 100
    y2_1 = 150
    x2_2 = 200
    y2_2 = 250
    start2 = rg.Point(x2_1, y2_1)
    end2 = rg.Point(x2_2, y2_2)
    line2 = rg.Line(start2, end2)
    line2.thickness = 10
    line2.attach_to(window)
    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
