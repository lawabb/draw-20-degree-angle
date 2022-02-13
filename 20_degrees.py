#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math
from matplotlib import animation
import numpy as np
import time
from sys import version_info

if version_info[0] < 3:
    import animate_player_py2 as animate_player
else:
    import animate_player_py3 as animate_player

r = 10.0        # circle radius
#r = r/math.cos(math.radians(20)) # make the x result = 20

#ang = 19.11      # draw target angle in degrees - for comparison
ang = 20.0

fig, ax = plt.subplots() 
fig.set_size_inches((20, 15))
fig.set_dpi(100)

text = ax.text(5.5, -1.0, "", fontsize=14)
    
def init():
    ax.set_xlim(-2*r, 2*r)
    ax.set_ylim(-1.5*r, 1.5*r)
    return c3,
    
def create_circle(pos, color):
    circle = plt.Circle(pos, color=color, radius= r, fill=False)
    return circle

def newline(a, b, color=None):
   # a is list of x values
   # b is a list of y values
    l = mlines.Line2D(a, b, color=color)
    ax.add_line(l)
    return l
    
def animate(i):
    x, y = c3.center 
    y = r * np.sin(np.radians(i))
    x = r * np.cos(np.radians(i))
    c3.center = (x, y)
    test_line.set_data([x6, x], [y6, y])
    x8, y8, angle = circle_point(x6, y6, x, y)
    ext_line.set_data([x, x8], [y, y8])
    origin_angle_line.set_data([0,x], [0,y])
    return test_line, c3, angle
    
def circle_point(x1, y1, x2, y2, rad=r):
    dx = x2 - x1
    dy = y2 - y1
    h = math.sqrt(dx**2 + dy**2)
    x8 = rad*dx/h +x2
    y8 = rad*dy/h +y2
    
    # if y8 hits zero then
    # stop the animation and calculate the angle
    # use rounding to hide float exactness errors
    
    if x8 >= 0:
        x = x8 + r/2.0
    else:
        anim.stop("Stop")
        x = x8 + r/2.0
        
    y = (math.sqrt(3))/2.0 * r - y8
    
    angle = np.rad2deg(math.atan(y/x))
    result = "x8 = %.10f  \ny8 = %.4f \nangle = %.4f degrees" % (x8 , y8, angle)
    #print(x)
    #print(y)
    print (result)
    print()
    
    if round(y8, 10) == 0 :
        anim.stop(result)
        
    return x8, y8, angle
    
    
# vertical line points
x1 = 0
y1 = 0
x2 = 0
y2 = r

# horizontal line points
x3 = -2*r
y3 = 0
x4 = 2*r
y4 = 0

# make the circles
c1= create_circle((-r, 0), 'blue')
c2= create_circle((0, 0), 'red')
c3 = create_circle((r, 0), 'green')
c3.set_linestyle('dashed')
c3.set_visible(True)

# point p5 is the '20' degree angled corner on the right- for reference
x5 = r  + ((r*math.sqrt(3) - 3*r*math.tan(math.radians(ang)))  /  (2*math.tan(math.radians(ang))))
y5 = 0

# point p6 is the top of red, blue circle intersection
x6  = -r/2.0
y6 = (math.sqrt(3)*r)/2.0

# add circles
ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(c3)

# make and add the lines
ver = newline([x1, x2], [-y2, y2], 'gray')
hor = newline([x3, x4], [y3, y4], 'gray')

# 'slope20' is the 20 degree purple reference line that we are endeavouring to draw using the green circle
slope20 = newline([x5, x6], [y5, y6], 'purple')
slope20.set_linestyle('dashed')
slope20.set_marker('o')
#Show or hide target
slope20.set_visible(True)

# when test_line and slope (@ 20 degrees) are the same we have our solution
test_line = newline([r, r/2], [y5, y6], 'black')
test_line.set_marker('o')

ext_line = newline([x6, x6], [y6,y6], 'orange')
ext_line.set_linestyle('dashed')
ext_line.set_marker('o')

origin_angle_line = newline([0, 0], [y5, y6], 'yellow')

# (r, 0) is rotating circle start point
xdata, ydata = r, 0

# for standard animation uncomment below
#anim = animation.FuncAnimation(fig, animate, init_func=init,  frames=360, interval=50, blit=True)
anim = animate_player.Player(fig, animate, text, init_func=init,  frames=360, mini=0, maxi=360)
                       
plt.plot()
plt.show()
