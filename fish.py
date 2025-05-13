import random
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from shapes import *

class Fish:
    speed_multiplier = 1.0     #increases as the player levels up to make the game harder
    def __init__(self, x=0, y=0, size=1.0, reverse=False):
        self.x = x
        self.y = y
        self.size = size
        self.reverse = reverse
        self.speed = self.speed_multiplier * random.uniform(0.005, 0.015)
        self.collider = None    #collider defined in child classes

    #used to move all fish except the player
    def update_position(self):
        if(self.reverse):
            self.x -= self.speed
        else:
            self.x += self.speed

        self.collider.update_position(self.x, self.y)

#ellipse collider
class FishCollider:
    def __init__(self, x, y, rx, ry, scale=1.0):
        self.x = x
        self.y = y
        #size of ellipse depends on size of fish 
        self.rx = scale*rx
        self.ry = scale*ry

    def update_position(self, x, y):
        self.x = x
        self.y = y


class BasicFish(Fish):
    #color_schemes stores all possible color styles for each type of fish
    #(fin_color, body_color)
    color_schemes = [((183, 52, 34), (255, 111, 28)),
                     ((86, 112, 181), (252, 218, 0)),
                     ((255, 171, 88), (220, 220, 200))]
    
    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.fin_color = self.color_schemes[selected_color][0]
        self.body_color = self.color_schemes[selected_color][1]
        self.collider = FishCollider(self.x + self.size*0.05, self.y + self.size*-0.038, 0.333, 0.16, self.size) #an offset is added because the body of BasicFish is not centered around the origin

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
    #(upper_color, lower_color)
    color_schemes = [((151, 156, 168), (180, 186, 191)),
                     ((169, 108, 88), (180, 180, 180))]

    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.upper_color = self.color_schemes[selected_color][0]
        self.lower_color = self.color_schemes[selected_color][1]
        self.collider = FishCollider(self.x, self.y, 0.5, 0.13, self.size)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        #size is scaled to match the sizes of other fish visually
        glScalef(0.95*self.size, 0.95*self.size, 0)
        #reverse is inverted to match direction with the rest of fish
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
    #(fin_color, body_color, gradient_color)
    color_schemes = [((252, 218, 0), (86, 112, 181), (67, 98, 154)),
                     ((234, 104, 28), (15, 32, 48), (125, 68, 38))]

    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.fin_color = self.color_schemes[selected_color][0]
        self.body_color = self.color_schemes[selected_color][1]
        self.gradient_color = self.color_schemes[selected_color][2]
        self.collider = FishCollider(self.x, self.y, 0.2, 0.1, self.size)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        #size is scaled to match the sizes of other fish visually
        glScalef(1.55*self.size, 1.55*self.size, 0)
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
    #(fin_color, body_color)
    color_schemes = [((244, 89, 48), (242, 111, 51))]

    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.fin_color = self.color_schemes[selected_color][0]
        self.body_color = self.color_schemes[selected_color][1]
        self.collider = FishCollider(self.x + self.size*-0.1, self.y, 0.3, 0.12, self.size)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        #size is scaled to match the sizes of other fish visually
        glScalef(1.25*self.size, 1.25*self.size, 0)
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
        quad_bezier_curve(0.07, 0.11, -0.05, 0, 0.07, -0.1, 0, 0, 0, fill=False, loop=True) #outline
        
        #center
        quad_bezier_curve(-0.09, 0.135, -0.19, 0, -0.09, -0.13, 255, 255, 255)
        quad_bezier_curve(-0.09, 0.135, -0.19, 0, -0.09, -0.13, 0, 0, 0, fill=False) #outline
        quad_bezier_curve(-0.09, 0.135, 0.01, 0, -0.095, -0.13, 255, 255, 255)
        quad_bezier_curve(-0.09, 0.135, 0.01, 0, -0.095, -0.13, 0, 0, 0, fill=False) #outline

        #left
        quad_bezier_curve(-0.3, 0.055, -0.35, 0, -0.3, -0.05, 255, 255, 255)
        quad_bezier_curve(-0.3, 0.055, -0.35, 0, -0.3, -0.05, 0, 0, 0, fill=False) #outline
        quad_bezier_curve(-0.3, 0.055, -0.2, 0, -0.305, -0.05, 255, 255, 255)
        quad_bezier_curve(-0.3, 0.055, -0.2, 0, -0.305, -0.05, 0, 0, 0, fill=False) #outline

        glPopMatrix()
