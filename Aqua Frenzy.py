import pygame as pg
import math as mm
import random
from shapes import *
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class Fish:
    def __init__(self, x=0, y=0, size=1.0, reverse=False):
        self.x = x
        self.y = y
        self.size = size
        self.reverse = reverse
        self.speed = random.uniform(0.005, 0.015)

    def update_position(self):
        if(self.reverse):
            self.x -= self.speed
        else:
            self.x += self.speed




class BasicFish(Fish):
    def __init__(self, x=0, y=0, size=1.0, reverse=False, fin_color = (183, 52, 34), body_color = (255, 111, 28)):
        super().__init__(x, y, size, reverse)
        self.fin_color = fin_color
        self.body_color = body_color

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size, 0)
        if self.reverse:
            glRotatef(180, 0, 1, 0)

        #tail fins
        triangle(-0.376, 0.189, -0.333, -0.023, -0.235, -0.023, *self.fin_color)
        triangle(-0.376, -0.234, -0.333, -0.023, -0.235, -0.023, *self.fin_color)
        #lower fins
        triangle(0.08, -0.325, 0.1, -0.19, 0.214, -0.15, *self.fin_color)
        triangle(-0.21, -0.24, -0.2, -0.13, -0.1, -0.15, *self.fin_color)
        #upper fins
        triangle(0.1, 0.25, -0.05, 0.1, 0.15, 0.1, *self.fin_color)
        triangle(-0.09, 0.2, -0.1, 0.1, 0.1, 0.1, *self.fin_color)
        #body
        ellipse(0.05, -0.038, 0.333, 0.16, 180, *self.body_color)
        #gills
        quad_bezier_curve(0.19, 0.07, 0.12, 0, 0.19, -0.12, *self.fin_color, fill=False)
        #eye
        circle(0.25, 0.02, 0.03, 180, 255, 255, 255)
        circle(0.25, 0.02, 0.02, 180, 0, 0, 0)
        #mouth
        line(0.3, -0.05, 0.38, -0.05, *self.fin_color)

        glPopMatrix()

class Shark(Fish):
    def __init__(self, x=0, y=0, size=1.0, reverse=False):
        super().__init__(x, y, size, reverse)
        self.upper_color = (151, 156, 168)
        self.lower_color = (180, 186, 191)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size, 0)
        #to match with the rest of fish
        if not self.reverse:
            glRotatef(180, 0, 1, 0)

        #snout
        triangle(-0.4, 0.08, -0.4, -0.08, -0.55, 0.02, *self.upper_color)
        #tail
        triangle(0.46, 0, 0.9, 0.4, 0.65, 0, *self.upper_color)
        triangle(0.46, 0, 0.7, -0.35, 0.65, 0, *self.upper_color)
        #upper fins
        triangle(-0.35, -0.04, 0.1, -0.04, 0, 0.35, *self.upper_color)
        triangle(0.23, -0.02, 0.37, -0.02, 0.34, 0.15, *self.upper_color)
        #lower fins
        triangle(0.15, -0.1, 0.32, -0.1, 0.3, -0.17, *self.lower_color)
        triangle(-0.25, -0.1, 0, -0.1, 0.05, -0.2, *self.lower_color)
        #body
        ellipse_gradient(0, 0, 0.5, 0.13, 180, *self.upper_color, *self.lower_color, 0.55)
        #mouth
        line(-0.46, -0.05, -0.4, -0.04, 0, 0, 0)
        #gills
        for i in range(4):
            x1 = -0.28 + i*0.02
            x2 = -0.25 + i*0.02
            quad_bezier_curve(x1, 0.07, x2, 0, x1, -0.07, 0, 0, 0, fill=False)
        #eye
        circle(-0.4, 0.03, 0.015, 180, 0, 0, 0)

        glPopMatrix()

class TropicalFish(Fish):
    def __init__(self, x=0, y=0, size=1.0, reverse=False, fin_color = (252, 218, 0), body_color = (86, 112, 181), gradient_color = (67, 98, 154)):
        super().__init__(x, y, size, reverse)
        self.fin_color = fin_color
        self.body_color = body_color
        self.gradient_color = gradient_color

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size, 0)
        if self.reverse:
            glRotatef(180, 0, 1, 0)

        #outer fins
        cubic_bezier_curve(-0.2, 0.02, -0.12, 0.16, 0.08, 0.16, 0.2, 0, *self.fin_color)
        cubic_bezier_curve(-0.2, -0.02, -0.12, -0.16, 0.08, -0.16, 0, 0, *self.fin_color)
        #tail fin
        triangle(-0.16, 0, -0.26, 0.1, -0.26, -0.1, *self.fin_color)
        #lower fin
        triangle_gradient(0.01, -0.13, 0.1, -0.08, 0.09, -0.05, *self.fin_color, *self.gradient_color)
        #body
        quad_bezier_curve(-0.2, 0, 0.05, 0.2, 0.2, 0, *self.body_color)
        quad_bezier_curve(-0.2, 0, 0.05, -0.2, 0.2, 0.01, *self.body_color)
        #side fin
        triangle_gradient(0.02, 0.02, 0.1, -0.02, 0.09, -0.05, *self.fin_color, *self.gradient_color)
        #mouth
        line(0.13, -0.015, 0.18, -0.015, 0, 0, 0)
        #eye
        circle(0.11, 0.04, 0.015, 180, 255, 255, 255)
        circle(0.11, 0.04, 0.01, 180, 0, 0, 0)

        glPopMatrix()

class ClownFish(Fish):
    def __init__(self, x=0, y=0, size=1.0, reverse=False):
        super().__init__(x, y, size, reverse)
        self.fin_color = (244, 89, 48)
        self.body_color = (242, 111, 51)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size, 0)
        if self.reverse:
            glRotatef(180, 0, 1, 0)
        
        #fins
        #upper
        quad_bezier_curve(-0.15, 0.1, 0.03, 0.27, 0.1, 0.07, *self.fin_color)
        cubic_bezier_curve(-0.35, 0, -0.3, 0.18, -0.16, 0.22, -0.05, 0.1, *self.fin_color)

        #lower
        cubic_bezier_curve(-0.35, 0, -0.3, -0.15, -0.16, -0.2, -0.1, -0.1, *self.fin_color)
        quad_bezier_curve(-0.03, -0.07, -0.05, -0.26, 0.08, -0.09, *self.fin_color)

        #tail
        cubic_bezier_curve(-0.5, 0, -0.49, 0.1, -0.47, 0.15, -0.35, 0, *self.fin_color)
        cubic_bezier_curve(-0.5, 0, -0.49, -0.1, -0.47, -0.15, -0.35, 0.02, *self.fin_color)

        #body
        cubic_bezier_curve(-0.4, 0, -0.2, 0.1, -0, 0.25, 0.2, 0, *self.body_color)
        cubic_bezier_curve(-0.4, 0, -0.2, -0.1, -0, -0.25, 0.2, 0.02, *self.body_color)

        #mouth
        line(0.11, -0.015, 0.17, -0.015, 0, 0, 0)

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

class Player(BasicFish):
    def __init__(self, x=0, y=0, size=1, reverse=False, fin_color=(183, 52, 34), body_color=(255, 111, 28)):
        super().__init__(x, y, size, reverse, fin_color, body_color)
        
    def update_position(self, x, y):
        self.reverse = x-self.x < 0
        self.x += 0.1*(x-self.x)
        self.y += 0.1*(y-self.y)

class Item:
    def __init__(self, x=0, y=0, size=1.0):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random.uniform(0.005, 0.01)

    def update_position(self):
        self.y += self.speed

class Bubble(Item):

    def draw(self):
        glPushMatrix()
        radius = 0.05 * self.size
        glTranslatef(self.x, self.y, 0)
        circle(0, 0, radius, 180, 180, 180, 200, 0.3)
        circle(-radius * 0.3, radius * 0.3, radius * 0.3, 180, 180, 180, 200, 0.6)
        circle(0, 0, radius, 180, 180, 180, 200, fill=False)
        glPopMatrix()

class ExtraLife(Item):

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size, 0)
        #+
        rectangle(-0.04, -0.03, -0.02, 0.03, 255, 215, 0)
        rectangle(-0.06, -0.01, 0, 0.01, 255, 215, 0)
        #1
        rectangle(0.02, -0.03, 0.04, 0.04, 255, 215, 0)
        #bubble
        circle(0, 0, 0.08, 180, 180, 180, 200, 0.3)
        circle(0, 0, 0.08, 180, 180, 180, 200, fill=False)
        glPopMatrix()

class Star(Item):

    def __init__(self, x=0, y=0, size=1):
        super().__init__(x, y, size)
        self.angle = 0
    
    def update_position(self):
        super().update_position()
        self.angle += 1

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        glScalef(self.size, self.size, 0)

        glPushMatrix()
        glRotatef(self.angle, 1, 1, 1)

        d = 0.01
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

        #bubble
        circle(0, 0, 0.09, 180, 180, 180, 200, 0.3)
        circle(0, 0, 0.09, 180, 180, 180, 200, fill=False)

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

    #enable transparency
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glEnable(GL_DEPTH_TEST)  
    glDepthFunc(GL_LEQUAL)

    background = pg.image.load("assets/background.jpeg")

    player = Player(0, 0, 0.6)
    fishList = [BasicFish(1.6, 0.6, 0.9, True, fin_color=(86, 112, 181), body_color=(252, 218, 0)),
                Shark(size=0.8),
                TropicalFish(-1.6, -0.5),
                ClownFish(1.6, -0.7, reverse=True)]
    
    items = [Bubble(0, -1, 1.5), Star(-0.5, -1), ExtraLife(0.5, -1)]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            #elif event.type == pg.MOUSEMOTION:

        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #background
        draw_image(background, -1.6, -1)
        
        for fish in fishList:
            fish.update_position()
            fish.draw()

        for item in items:
            item.update_position()
            item.draw()

        x, y = pg.mouse.get_pos()
        player.update_position(x*3.2/display[0] - 1.6, 1 - y*2/display[1])
        player.draw()

        # basic_fish(1, 0.8, 0.5, fin_color=(86, 112, 181), body_color=(252, 218, 0))
        

        draw_text("Score: 123", -1.55, 0.87, 50)
        draw_text("Lives: 3", 1.25, 0.87, 50)

        pg.display.flip()
        pg.time.wait(10)

main()
