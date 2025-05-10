import random
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from shapes import *

class Item:
    def __init__(self, x=0, y=0, size=1.0, move_down = False):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random.uniform(0.005, 0.01)
        if move_down:
            self.speed *= -1
        self.collider = None    #collider defined in child classes

    def update_position(self):
        self.y += self.speed
        self.collider.update_position(self.x, self.y)

#circle collider
class ItemCollider:
    def __init__(self, x, y, r, scale=1.0):
        self.x = x
        self.y = y
        self.r = scale*r

    def update_position(self, x, y):
        self.x = x
        self.y = y

class Bubble(Item):
    def __init__(self, x=0, y=0, size=1.0, move_down=False):
        super().__init__(x, y, size, move_down)
        self.collider = ItemCollider(self.x, self.y, 0.05, self.size)

    def draw(self):
        glPushMatrix()
        radius = 0.05 * self.size
        glTranslatef(self.x, self.y, 0)
        circle(0, 0, radius, 180, 180, 180, 200, 0.3)
        circle(-radius * 0.3, radius * 0.3, radius * 0.3, 180, 180, 180, 200, 0.6)
        circle(0, 0, radius, 180, 180, 180, 200, fill=False)
        glPopMatrix()

class ExtraLife(Item):
    def __init__(self, x=0, y=0, size=1.0, move_down=False):
        super().__init__(x, y, size, move_down)
        self.collider = ItemCollider(self.x, self.y, 0.08, self.size)

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

    def __init__(self, x=0, y=0, size=1.0, move_down = False):
        super().__init__(x, y, size, move_down)
        self.angle = 0
        self.collider = ItemCollider(self.x, self.y, 0.09, self.size)
    
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