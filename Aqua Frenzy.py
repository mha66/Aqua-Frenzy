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

# def normalize(x_size, y_size, *coordinates):
#     tmp = []
#     for i in range(len(coordinates)):
#         if i%2 == 0:
#             tmp.append(coordinates[i] * 2/x_size - 1)
#         else:
#             tmp.append(-coordinates[i] * 2/y_size + 1)
#     return tmp

def fish(x, y, r, g, b, size=1.0, reverse=False):
        glPushMatrix()
        glScale(size, size, 0)
        glTranslate(x, y, 0)
        if reverse:
            glRotate(180, 0, 1, 0)
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


def main():
    pg.init()

    display = (800,800)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    glOrtho(-1, 1, -1, 1, -1, 1)
    #glClearColor(65/255, 142/255, 188/255, 1) 
    glDisable(GL_DEPTH_TEST)  
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT)
        rectangle_gradient(-1, -0.7, 1, 1, 23, 20, 188, 65, 142, 188)
        rectangle_gradient(-1, -1, 1, -0.7, 187, 134, 23, 240, 180, 58)
        # triangle(*normalize(471, 397, 148, 159, 156, 203, 182, 203), 1, 0, 0)
        # triangle(*normalize(471, 397, 148, 245, 156, 203, 182, 203), 1, 0, 0)
        fish(0.4, 0.2, 255, 0, 0, 0.6, True)
        
        # triangle(-0.2, -0.2, 0.2, -0.2, 0, 0.2, 1,0,0)
        pg.display.flip()
        pg.time.wait(10)


main()