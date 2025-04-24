import pygame as pg
import math as mm
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

#(2/size)*x - 1

def triangle(x1, y1, x2, y2, x3, y3, r, g, b):
    glBegin(GL_TRIANGLES)
    glColor3f(r/255, g/255, b/255)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def triangle_gradient(x1, y1, x2, y2, x3, y3, r1, g1, b1, r2, g2, b2):
    glBegin(GL_TRIANGLES)
    glColor3f(r1/255, g1/255, b1/255)
    glVertex2f(x1, y1)
    glColor3f(r2/255, g2/255, b2/255)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
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


def circle(xc, yc, radius, num_segments, r, g, b):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r/255, g/255, b/255)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        x = xc + radius * mm.cos(angle)
        y = yc + radius * mm.sin(angle)
        glVertex2f(x, y)
    glEnd()

def ellipse(xc, yc, radius_x, radius_y, num_segments, r, g, b):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r/255, g/255, b/255)
    for i in range(num_segments):
        angle = 2*mm.pi*i/num_segments
        x = xc + radius_x * mm.cos(angle)
        y = yc + radius_y * mm.sin(angle)
        glVertex2f(x, y)
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

def quad_bezier_curve(x1, y1, x2, y2, x3, y3, r, g, b, fill=False):
    if fill:
        glBegin(GL_POLYGON)
    else:
        glBegin(GL_LINE_STRIP)    

    glColor3f(r/255, g/255, b/255)
    t=0
    while t <= 1:
        xA = (1-t)*x1 + t*x2
        yA = (1-t)*y1 + t*y2
        
        xB = (1-t)*x2 + t*x3
        yB = (1-t)*y2 + t*y3

        xP = (1-t)*xA + t*xB
        yP = (1-t)*yA + t*yB
    
        glVertex2f(xP, yP)
        t += 0.01

    glEnd()

def cubic_bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4, r, g, b, fill=False):
    if fill:
        glBegin(GL_POLYGON)
    else:
        glBegin(GL_LINE_STRIP)    

    glColor3f(r/255, g/255, b/255)
    t=0
    while t <= 1:
        xA = (1-t)*x1 + t*x2
        yA = (1-t)*y1 + t*y2
        
        xB = (1-t)*x2 + t*x3
        yB = (1-t)*y2 + t*y3

        xC = (1-t)*x3 + t*x4
        yC = (1-t)*y3 + t*y4

        xP = (1-t)*xA + t*xB
        yP = (1-t)*yA + t*yB

        xQ = (1-t)*xB + t*xC
        yQ = (1-t)*yB + t*yC

        xR = (1-t)*xP + t*xQ
        yR = (1-t)*yP + t*yQ
    
        glVertex2f(xR, yR)
        t += 0.01

    glEnd()


def fish(x, y, r, g, b, size=1.0, reverse=False):
        glPushMatrix()
        glScalef(size, size, 0)
        glTranslatef(x, y, 0)
        if reverse:
            glRotatef(180, 0, 1, 0)

        #tail fins
        triangle(-0.376, 0.189, -0.333, -0.023, -0.235, -0.023, r, g, b)
        triangle(-0.376, -0.234, -0.333, -0.023, -0.235, -0.023, r, g, b)
        #body
        ellipse(0.05, -0.038, 0.333, 0.16, 180, r, g , b)
        circle(0.25, 0.02, 0.02, 180, 0, 0, 0)
        #lower fins
        triangle(0.08, -0.325, 0.1, -0.19, 0.214, -0.15, r, g, b)
        triangle(-0.21, -0.24, -0.2, -0.13, -0.1, -0.15, r, g, b)
        #upper fins
        triangle(0.1, 0.25, -0.05, 0.1, 0.15, 0.1, r, g, b)
        triangle(-0.09, 0.2, -0.1, 0.1, 0.1, 0.1, r, g, b)

        glPopMatrix()

def shark(x, y, size=1.0, reverse=False):
        upper_color = (151, 156, 168)
        lower_color = (180, 186, 191)
        glPushMatrix()
        glScalef(size, size, 0)
        glTranslatef(x, y, 0)
        if reverse:
            glRotatef(180, 0, 1, 0)

        #snout
        triangle(-0.4, 0.08, -0.4, -0.08, -0.55, 0.02, *upper_color)
        #tail fins
        triangle(0.46, 0, 0.9, 0.4, 0.65, 0, *upper_color)
        triangle(0.46, 0, 0.7, -0.35, 0.65, 0, *upper_color)
        #upper fin
        triangle(-0.35, -0.04, 0.1, -0.04, 0, 0.35, *upper_color)
        #lower fins
        triangle(0.15, -0.1, 0.32, -0.1, 0.3, -0.17, *lower_color)
        triangle(-0.25, -0.1, 0, -0.1, 0.05, -0.2, *lower_color)
        #body
        ellipse_gradient(0, 0, 0.5, 0.13, 180, *upper_color, *lower_color, 0.55)
        #eye
        circle(-0.4, 0.03, 0.015, 180, 0, 0, 0)

        glPopMatrix()

def tropical_fish(x, y, size=1.0, reverse=False):
        glPushMatrix()
        glScalef(size, size, 0)
        glTranslatef(x, y, 0)
        if reverse:
            glRotatef(180, 0, 1, 0)

        #outer fins
        cubic_bezier_curve(-0.2, 0.02, -0.12, 0.16, 0.08, 0.16, 0.2, 0, 252, 218, 0, True)
        cubic_bezier_curve(-0.2, -0.02, -0.12, -0.16, 0.08, -0.16, 0, 0, 252, 218, 0, True)
        #tail fin
        triangle(-0.16, 0, -0.26, 0.1, -0.26, -0.1, 252, 218, 0)
        #lower fin
        triangle_gradient(0.01, -0.13, 0.1, -0.08, 0.09, -0.05, 252, 218, 0, 67, 98, 154)
        #body
        quad_bezier_curve(-0.2, 0, 0.05, 0.2, 0.2, 0, 86, 112, 181, True)
        quad_bezier_curve(-0.2, 0, 0.05, -0.2, 0.2, 0.01, 86, 112, 181, True)
        #side fin
        triangle_gradient(0.02, 0.02, 0.1, -0.02, 0.09, -0.05, 252, 218, 0, 67, 98, 154)
        #eye
        circle(0.11, 0.04, 0.01, 180, 0, 0, 0)

        glPopMatrix()


def main():
    pg.init()

    display = (1600,1000)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -2.4)

    #glOrtho(-1, 1, -1, 1, -1, 1)
    glDisable(GL_DEPTH_TEST)  #remove this
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT)

        #background
        rectangle_gradient(-2, -0.7, 2, 1, 23, 20, 188, 65, 142, 188)
        rectangle_gradient(-2, -1, 2, -0.7, 187, 134, 23, 240, 180, 58)
        
        shark(0, 0)
        fish(0.4, 0.8, 255, 0, 0, 0.6, True)
        tropical_fish(-0.8, 0.5, 0.7)
        
        pg.display.flip()
        pg.time.wait(10)


main()