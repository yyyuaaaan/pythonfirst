"""__author__ = 'anyu'
Implement the “paint fill” function that one might see on many image editing programs.
That is, given a screen (represented by a 2-dimensional array of Colors), a point, and a new color,
fill in the surrounding area until you hit a border of that color.


"""
def paint(screen, point, color): # screen is border curve
    if point not in screen: return #assume click inside the screen area
    elif screen.point.color is not color:
        screen.point.color = color
        paint(screen,point.up,color)
        paint(screen,point.down,color)
        paint(screen,point.left,color)
        paint(screen,point.right,color)
    return

color = {"blue","red","yellow"}

