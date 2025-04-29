import pygame as pg
import math as mm
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


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

def quad_bezier_curve(x1, y1, x2, y2, x3, y3, r, g, b, fill=True):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
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

def quad_bezier_shape(x1, y1, x2, y2, x3, y3, r, g, b, x_offset, y_offset, x_center, y_center, fill=True):
    glColor3f(r/255, g/255, b/255)
    if fill:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x_center, y_center)
    else:
        glBegin(GL_LINE_STRIP)   
    
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

    x2 += x_offset
    y2 += y_offset
    t=1
    while t >= 0:
        s = 1-t
        xA = s*x1 + t*x2
        yA = s*y1 + t*y2
        
        xB = s*x2 + t*x3
        yB = s*y2 + t*y3

        xP = s*xA + t*xB
        yP = s*yA + t*yB
    
        glVertex2f(xP, yP)
        t -= 0.01

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
    glScalef(size, size, 0)
    glTranslatef(x, y, 0)
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
    circle(0.25, 0.02, 0.02, 180, 0, 0, 0)

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
    circle(0.11, 0.04, 0.01, 180, 0, 0, 0)

    glPopMatrix()

def bubble(x, y, radius=0.05):
    glPushMatrix()
    glTranslatef(x, y, 0)
    circle(0, 0, radius, 180, 180, 180, 200, 0.3)
    circle(-radius * 0.3, radius * 0.3, radius * 0.3, 180, 180, 180, 200, 0.6)
    circle(0, 0, radius, 180, 180, 180, 200, 1, False)
    glPopMatrix()

def star(x, y, size=1.0):
    glPushMatrix()
    glScalef(size, size, 0)
    glTranslatef(x, y, 0)
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
    circle(0, 0, 0.08, 180, 180, 180, 200, 1, False)
    glPopMatrix()

def convert_image_to_texture(image):
    texture_data = pg.image.tostring(image, "RGBA", True)
    width = image.get_width()
    height = image.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id, width, height

def create_text_texture(text, font_size=32, color=(255, 255, 255)):
    font = pg.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, color)
    return convert_image_to_texture(text_surface)

def create_texture(filename):
    texture_surface = pg.image.load(filename)
    return convert_image_to_texture(texture_surface)

def draw_texture(texture_id, x, y, width, height):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glColor3f(1, 1, 1) #to ensure texture color is not affected by previous glColor3f() calls

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)
    glTexCoord2f(1, 0)
    glVertex2f(x + width, y)
    glTexCoord2f(1, 1)
    glVertex2f(x + width, y + height)
    glTexCoord2f(0, 1)
    glVertex2f(x, y + height)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def main():
    pg.init()
  
    display = (1600,1000)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    #gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    #glTranslatef(0, 0, -2.4)

    glOrtho(-1.6, 1.6, -1, 1, -1, 1)
    glDisable(GL_DEPTH_TEST)  #remove this

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    text_texture, text_width, text_height = create_text_texture("Score: 123", 64)
    texture, width, height = create_texture("assets/background.jpeg")
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT)

        #background
        draw_texture(texture, -1.6, -1, 3.5, 2)
        #rectangle_gradient(-2, -0.7, 2, 1, 23, 20, 188, 65, 142, 188)
        #rectangle_gradient(-2, -1, 2, -0.7, 187, 134, 23, 240, 180, 58)
        
        shark(0, 0)
        basic_fish(0.4, 0.8, 0.6, True)
        tropical_fish(-0.8, 0.5, 0.7)
    
        bubble(-1.2, 0, 0.05)
        star(-1.1, -0.4)
        
        #quad_bezier_shape(0, 0, 0.2, -0.4, 0.4, 0.4, 0, 0, 0, 0.1, 0.4, 0.25, 0)



        draw_texture(text_texture, -1.55, 0.9, 0.4, 0.1)

        pg.display.flip()
        pg.time.wait(10)


main()