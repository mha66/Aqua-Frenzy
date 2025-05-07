import math as mm
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

def line(x1, y1, x2, y2, r, g, b):
    glBegin(GL_LINES)
    glColor3f(r/255, g/255, b/255)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def triangle(x1, y1, x2, y2, x3, y3, r, g, b):
    glBegin(GL_TRIANGLES)
    glColor3f(r/255, g/255, b/255)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def triangle_3D(x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b):
    glBegin(GL_TRIANGLES)
    glColor3f(r/255, g/255, b/255)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y2, z2)
    glVertex3f(x3, y3, z3)
    glEnd()

def triangle_gradient(x1, y1, x2, y2, x3, y3, r1, g1, b1, r2, g2, b2):
    glBegin(GL_TRIANGLES)
    glColor3f(r1/255, g1/255, b1/255)
    glVertex2f(x1, y1)
    glColor3f(r2/255, g2/255, b2/255)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def rectangle(x1, y1, x2, y2, r, g, b, a=1):
    glBegin(GL_QUADS)
    glColor4f(r/255, g/255, b/255, a)
    glVertex2f(x1, y1)
    glVertex2f(x1, y2)
    glVertex2f(x2, y2)
    glVertex2f(x2, y1)
    glEnd()

def rectangle_gradient(x1, y1, x2, y2, r1, g1, b1, r2, g2, b2):
    glBegin(GL_QUADS)
    glColor3f(r1/255, g1/255, b1/255)
    glVertex2f(x1, y1)
    glColor3f(r2/255, g2/255, b2/255)
    glVertex2f(x1, y2)
    glVertex2f(x2, y2)
    glColor3f(r1/255, g1/255, b1/255)
    glVertex2f(x2, y1)
    glEnd()

def quad_3D(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, r, g, b):
    glBegin(GL_QUADS)
    glColor3f(r/255, g/255, b/255)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y2, z2)
    glVertex3f(x3, y3, z3)
    glVertex3f(x4, y4, z4)
    glEnd()

def circle(xc, yc, radius, num_segments, r, g, b, a=1, fill=True):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
    else:
        glBegin(GL_LINE_LOOP)

    glColor4f(r/255, g/255, b/255, a)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        x = xc + radius * mm.cos(angle)
        y = yc + radius * mm.sin(angle)
        glVertex2f(x, y)
    glEnd()

def circle_3D(xc, yc, zc, radius, num_segments, r, g, b, a=1, fill=True):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
    else:
        glBegin(GL_LINE_LOOP)

    glColor4f(r/255, g/255, b/255, a)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        x = xc + radius * mm.cos(angle)
        y = yc + radius * mm.sin(angle)
        glVertex3f(x, y, zc)
    glEnd()

def ellipse(xc, yc, radius_x, radius_y, num_segments, r, g, b, fill=True):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
    else:
        glBegin(GL_LINE_LOOP)

    glColor3f(r/255, g/255, b/255)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        x = xc + radius_x * mm.cos(angle)
        y = yc + radius_y * mm.sin(angle)
        glVertex2f(x, y)
    glEnd()

def ellipse_3D(xc, yc, zc, radius_x, radius_y, num_segments, r, g, b, fill=True):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
    else:
        glBegin(GL_LINE_LOOP)

    glColor3f(r/255, g/255, b/255)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        x = xc + radius_x * mm.cos(angle)
        y = yc + radius_y * mm.sin(angle)
        glVertex3f(x, y, zc)
    glEnd()

def ellipse_gradient(xc, yc, radius_x, radius_y, num_segments, r1, g1, b1, r2, g2, b2, ratio = 0.5):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r1/255, g1/255, b1/255)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        if i >= num_segments * ratio:
             glColor3f(r2/255, g2/255, b2/255)
        x = xc + radius_x * mm.cos(angle)
        y = yc + radius_y * mm.sin(angle)
        glVertex2f(x, y)
    glEnd()

def quad_bezier_curve(x1, y1, x2, y2, x3, y3, r, g, b, fill=True, loop=False):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
    elif loop:
        glBegin(GL_LINE_LOOP)
    else:
        glBegin(GL_LINE_STRIP)   
    
    glColor3f(r/255, g/255, b/255)
    t=0
    while t <= 1:
        s = 1-t
        xA = s*x1 + t*x2
        yA = s*y1 + t*y2
        
        xB = s*x2 + t*x3
        yB = s*y2 + t*y3

        xP = s*xA + t*xB
        yP = s*yA + t*yB
    
        glVertex2f(xP, yP)
        t += 0.01

    glEnd()

def cubic_bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4, r, g, b, fill=True):
    if fill:
        glBegin(GL_POLYGON)
    else:
        glBegin(GL_LINE_STRIP)    

    glColor3f(r/255, g/255, b/255)
    t=0
    while t <= 1:
        s = 1-t
        xA = s*x1 + t*x2
        yA = s*y1 + t*y2
        
        xB = s*x2 + t*x3
        yB = s*y2 + t*y3

        xC = s*x3 + t*x4
        yC = s*y3 + t*y4

        xP = s*xA + t*xB
        yP = s*yA + t*yB

        xQ = s*xB + t*xC
        yQ = s*yB + t*yC

        xR = s*xP + t*xQ
        yR = s*yP + t*yQ
    
        glVertex2f(xR, yR)
        t += 0.01

    glEnd()

