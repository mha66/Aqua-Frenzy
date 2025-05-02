import pygame as pg
import math as mm
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

def line(x1, y1, x2, y2, r, g, b):
    #glLineWidth()
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


def rectangle(x1, y1, x2, y2, r, g, b):
    glBegin(GL_QUADS)
    glColor3f(r/255, g/255, b/255)
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


def basic_fish(x, y, size=1.0, reverse=False):
    fin_color = (183, 52, 34)
    body_color = (255, 111, 28)
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, size, 0)
    if reverse:
        glRotatef(180, 0, 1, 0)

    #tail fins
    triangle(-0.376, 0.189, -0.333, -0.023, -0.235, -0.023, *fin_color)
    triangle(-0.376, -0.234, -0.333, -0.023, -0.235, -0.023, *fin_color)
    #lower fins
    triangle(0.08, -0.325, 0.1, -0.19, 0.214, -0.15, *fin_color)
    triangle(-0.21, -0.24, -0.2, -0.13, -0.1, -0.15, *fin_color)
    #upper fins
    triangle(0.1, 0.25, -0.05, 0.1, 0.15, 0.1, *fin_color)
    triangle(-0.09, 0.2, -0.1, 0.1, 0.1, 0.1, *fin_color)
    #body
    ellipse(0.05, -0.038, 0.333, 0.16, 180, *body_color)
    #gills
    quad_bezier_curve(0.19, 0.07, 0.12, 0, 0.19, -0.12, *fin_color, fill=False)
    #eye
    circle(0.25, 0.02, 0.03, 180, 255, 255, 255)
    circle(0.25, 0.02, 0.02, 180, 0, 0, 0)
    #mouth
    line(0.3, -0.05, 0.38, -0.05, *fin_color)

    glPopMatrix()

def shark(x, y, size=1.0, reverse=False):
    upper_color = (151, 156, 168)
    lower_color = (180, 186, 191)
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, size, 0)
    if reverse:
        glRotatef(180, 0, 1, 0)

    #snout
    triangle(-0.4, 0.08, -0.4, -0.08, -0.55, 0.02, *upper_color)
    #tail
    triangle(0.46, 0, 0.9, 0.4, 0.65, 0, *upper_color)
    triangle(0.46, 0, 0.7, -0.35, 0.65, 0, *upper_color)
    #upper fins
    triangle(-0.35, -0.04, 0.1, -0.04, 0, 0.35, *upper_color)
    triangle(0.23, -0.02, 0.37, -0.02, 0.34, 0.15, *upper_color)
    #lower fins
    triangle(0.15, -0.1, 0.32, -0.1, 0.3, -0.17, *lower_color)
    triangle(-0.25, -0.1, 0, -0.1, 0.05, -0.2, *lower_color)
    #body
    ellipse_gradient(0, 0, 0.5, 0.13, 180, *upper_color, *lower_color, 0.55)
    #gills
    for i in range(4):
        x1 = -0.28 + i*0.02
        x2 = -0.25 + i*0.02
        quad_bezier_curve(x1, 0.07, x2, 0, x1, -0.07, 0, 0, 0, fill=False)
    #eye
    circle(-0.4, 0.03, 0.015, 180, 0, 0, 0)

    glPopMatrix()

def tropical_fish(x, y, size=1.0, reverse=False):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, size, 0)
    if reverse:
        glRotatef(180, 0, 1, 0)

    #outer fins
    cubic_bezier_curve(-0.2, 0.02, -0.12, 0.16, 0.08, 0.16, 0.2, 0, 252, 218, 0)
    cubic_bezier_curve(-0.2, -0.02, -0.12, -0.16, 0.08, -0.16, 0, 0, 252, 218, 0)
    #tail fin
    triangle(-0.16, 0, -0.26, 0.1, -0.26, -0.1, 252, 218, 0)
    #lower fin
    triangle_gradient(0.01, -0.13, 0.1, -0.08, 0.09, -0.05, 252, 218, 0, 67, 98, 154)
    #body
    quad_bezier_curve(-0.2, 0, 0.05, 0.2, 0.2, 0, 86, 112, 181)
    quad_bezier_curve(-0.2, 0, 0.05, -0.2, 0.2, 0.01, 86, 112, 181)
    #side fin
    triangle_gradient(0.02, 0.02, 0.1, -0.02, 0.09, -0.05, 252, 218, 0, 67, 98, 154)
    #eye
    circle(0.11, 0.04, 0.015, 180, 255, 255, 255)
    circle(0.11, 0.04, 0.01, 180, 0, 0, 0)

    glPopMatrix()

def clown_fish(x, y, size=1.0, reverse=False):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, size, 0)
    if reverse:
        glRotatef(180, 0, 1, 0)
        
    #fins
    #upper
    quad_bezier_curve(-0.15, 0.1, 0.03, 0.27, 0.1, 0.07, 244, 89, 48)
    cubic_bezier_curve(-0.35, 0, -0.3, 0.18, -0.16, 0.22, -0.05, 0.1, 244, 89, 48)

    #lower
    cubic_bezier_curve(-0.35, 0, -0.3, -0.15, -0.16, -0.2, -0.1, -0.1, 244, 89, 48)
    quad_bezier_curve(-0.03, -0.07, -0.05, -0.26, 0.08, -0.09, 244, 89, 48)

    #tail
    cubic_bezier_curve(-0.5, 0, -0.49, 0.1, -0.47, 0.15, -0.35, 0, 244, 89, 48)
    cubic_bezier_curve(-0.5, 0, -0.49, -0.1, -0.47, -0.15, -0.35, 0.02, 244, 89, 48)

    #body
    cubic_bezier_curve(-0.4, 0, -0.2, 0.1, -0, 0.25, 0.2, 0, 242, 111, 51)
    cubic_bezier_curve(-0.4, 0, -0.2, -0.1, -0, -0.25, 0.2, 0.02, 242, 111, 51)

    #eye
    circle(0.13, 0.03, 0.017, 180, 255, 255, 255)
    circle(0.13, 0.03, 0.013, 180, 0, 0, 0)

    #stripes
    #right
    quad_bezier_curve(0.07, 0.11, -0.05, 0, 0.07, -0.1, 255, 255, 255)
    quad_bezier_curve(0.07, 0.11, -0.05, 0, 0.07, -0.1, 0, 0, 0, fill=False, loop=True)
    
    #center
    quad_bezier_curve(-0.09, 0.135, -0.19, 0, -0.09, -0.13, 255, 255, 255)
    quad_bezier_curve(-0.09, 0.135, -0.19, 0, -0.09, -0.13, 0, 0, 0, fill=False)
    quad_bezier_curve(-0.09, 0.135, 0.01, 0, -0.095, -0.13, 255, 255, 255)
    quad_bezier_curve(-0.09, 0.135, 0.01, 0, -0.095, -0.13, 0, 0, 0, fill=False)

    #left
    quad_bezier_curve(-0.3, 0.055, -0.35, 0, -0.3, -0.05, 255, 255, 255)
    quad_bezier_curve(-0.3, 0.055, -0.35, 0, -0.3, -0.05, 0, 0, 0, fill=False)
    quad_bezier_curve(-0.3, 0.055, -0.2, 0, -0.305, -0.05, 255, 255, 255)
    quad_bezier_curve(-0.3, 0.055, -0.2, 0, -0.305, -0.05, 0, 0, 0, fill=False)

    glPopMatrix()

def bubble(x, y, radius=0.05):
    glPushMatrix()
    glTranslatef(x, y, 0)
    circle(0, 0, radius, 180, 180, 180, 200, 0.3)
    circle(-radius * 0.3, radius * 0.3, radius * 0.3, 180, 180, 180, 200, 0.6)
    circle(0, 0, radius, 180, 180, 180, 200, fill=False)
    glPopMatrix()

def star(x, y, size=1.0):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, size, 0)
    #base (sides)
    triangle(-0.07, 0.02, 0.07, 0.02, 0, -0.03, 255, 215, 0)
    #upper
    triangle(-0.02, 0.02, 0.02, 0.02, 0, 0.07, 255, 215, 0)
    #bottom left
    triangle(-0.03, 0, 0, -0.03, -0.04, -0.06, 255, 215, 0)
    #bottom right
    triangle(0.03, 0, 0, -0.03, 0.04, -0.06, 255, 215, 0)
    #bubble
    circle(0, 0, 0.08, 180, 180, 180, 200, 0.3)
    circle(0, 0, 0.08, 180, 180, 180, 200, fill=False)
    glPopMatrix()


def star_3D(x, y, z=0, size=1.0, depth=0.02, angle=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(size, size, 0)

    glPushMatrix()
    glRotatef(angle, 1, 1, 1)

    d = depth/2
    #front
    #base (sides)
    triangle_3D(-0.07, 0.02, d, 0.07, 0.02, d, 0, -0.03, d, 255, 215, 0)
    #upper
    triangle_3D(-0.02, 0.02, d, 0.02, 0.02, d, 0, 0.07, d, 255, 215, 0)
    #bottom left
    triangle_3D(-0.03, 0, d, 0, -0.03, d, -0.04, -0.06, d, 255, 215, 0)
    #bottom right
    triangle_3D(0.03, 0, d, 0, -0.03, d, 0.04, -0.06, d, 255, 215, 0)

    #back
    #base (sides)
    triangle_3D(-0.07, 0.02, -d, 0.07, 0.02, -d, 0, -0.03, -d, 255, 215, 0)
    #upper
    triangle_3D(-0.02, 0.02, -d, 0.02, 0.02, -d, 0, 0.07, -d, 255, 215, 0)
    #bottom left
    triangle_3D(-0.03, 0, -d, 0, -0.03, -d, -0.04, -0.06, -d, 255, 215, 0)
    #bottom right
    triangle_3D(0.03, 0, -d, 0, -0.03, -d, 0.04, -0.06, -d, 255, 215, 0)
    
    #sides
    #left
    quad_3D(0, 0.07, d, 0, 0.07, -d, -0.04, -0.06, -d, -0.04, -0.06, d, 255, 215, 0)
    
    #right
    quad_3D(0, 0.07, d, 0, 0.07, -d, 0.04, -0.06, -d, 0.04, -0.06, d, 255, 215, 0)

    #top
    quad_3D(-0.07, 0.02, d, -0.07, 0.02, -d, 0.07, 0.02, -d, 0.07, 0.02, d, 255, 215, 0)

    #bottom
    #left face
    quad_3D(-0.07, 0.02, d, -0.07, 0.02, -d, 0.04, -0.06, -d, 0.04, -0.06, d, 255, 215, 0)
    #right face
    quad_3D(0.07, 0.02, d, 0.07, 0.02, -d, -0.04, -0.06, -d, -0.04, -0.06, d, 255, 215, 0)

    glPopMatrix()

    circle(0, 0, 0.09, 180, 180, 180, 200, 0.3)
    circle(0, 0, 0.09, 180, 180, 180, 200, fill=False)

    glPopMatrix()

def extra_life(x, y, size=1.0):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(size, size, 0)
    #+
    rectangle(-0.04, -0.03, -0.02, 0.03, 255, 215, 0)
    rectangle(-0.06, -0.01, 0, 0.01, 255, 215, 0)
    #1
    rectangle(0.02, -0.03, 0.04, 0.04, 255, 215, 0)
    #bubble
    circle(0, 0, 0.08, 180, 180, 180, 200, 0.3)
    circle(0, 0, 0.08, 180, 180, 180, 200, fill=False)
    glPopMatrix()

def draw_text(text, x, y, font_size=32, color=(255, 255, 255)):
    font = pg.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, color)
    text_data = pg.image.tostring(text_surface, "RGBA", True)
    glRasterPos2d(x, y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def draw_image(image_surface, x, y):
    image_data = pg.image.tostring(image_surface, "RGBA", True)
    glRasterPos2d(x, y)
    glDrawPixels(image_surface.get_width(), image_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, image_data)

def main():
    pg.init()
  
    display = (1600,1000)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -2.415)

    # glOrtho(-1.6, 1.6, -1, 1, -1, 1)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glEnable(GL_DEPTH_TEST)  
    glDepthFunc(GL_LEQUAL)

    background = pg.image.load("assets/background.jpeg")

    angle = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #background
        draw_image(background, -1.6, -1)
        #rectangle_gradient(-2, -0.7, 2, 1, 23, 20, 188, 65, 142, 188)
        #rectangle_gradient(-2, -1, 2, -0.7, 187, 134, 23, 240, 180, 58)
        
        shark(0, 0)
        basic_fish(0.4, 0.7, 0.6, True)
        tropical_fish(-0.6, 0.3, 0.7)
        clown_fish(-0.9, 0.7, 0.8)

        bubble(-1.2, 0, 0.05)
        star(-1.1, -0.3)
        extra_life(-1.15, -0.6)

        star_3D(-1.4, -0.3, 0, angle=angle)

        draw_text("Score: 123", -1.55, 0.87, 50)
        draw_text("Lives: 3", 1.25, 0.87, 50)
        angle += 1

        pg.display.flip()
        pg.time.wait(10)

main()
