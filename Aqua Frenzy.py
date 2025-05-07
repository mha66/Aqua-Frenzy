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
        self.collider = None    #collider defined in child classes

    def update_position(self):
        if(self.reverse):
            self.x -= self.speed
        else:
            self.x += self.speed

        self.collider.update_position(self.x, self.y)


class BasicFish(Fish):
    #(fin_color, body_color)
    color_schemes = [((183, 52, 34), (255, 111, 28)),
                     ((86, 112, 181), (252, 218, 0))]
    
    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.fin_color = self.color_schemes[selected_color][0]
        self.body_color = self.color_schemes[selected_color][1]
        self.collider = FishCollider(self.x + self.size*0.05, self.y + self.size*-0.038, 0.333, 0.16, self.size)

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
    color_schemes = [((151, 156, 168), (180, 186, 191))]

    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.upper_color = self.color_schemes[selected_color][0]
        self.lower_color = self.color_schemes[selected_color][1]
        self.collider = FishCollider(self.x, self.y, 0.5, 0.13, self.size)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        #size is scaled to match the sizes of other fish
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
    color_schemes = [((252, 218, 0), (86, 112, 181), (67, 98, 154))]

    def __init__(self, x=0, y=0, size=1.0, reverse=False, selected_color=0):
        super().__init__(x, y, size, reverse)
        self.fin_color = self.color_schemes[selected_color][0]
        self.body_color = self.color_schemes[selected_color][1]
        self.gradient_color = self.color_schemes[selected_color][2]
        self.collider = FishCollider(self.x, self.y, 0.2, 0.1, self.size)

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        #size is scaled to match the sizes of other fish
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
        #ellipse(0, 0, 0.2, 0.1, 180, 0, 0, 0, False)
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
        #size is scaled to match the sizes of other fish
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

        #ellipse(-0.1, 0, 0.3, 0.12, 180, 0, 0, 0, False)
        # ellipse(-0.1+0.04, 0, 0.26, 0.13, 180, 0, 0, 0, False)
        glPopMatrix()

class Player:
    def __init__(self, fish_object, lives = 3, score = 0):
        self.fish = fish_object
        self.lives = lives
        self.score = score
        self.is_immune = False
        
    def update_position(self, x, y):
        self.fish.reverse = x-self.fish.x < 0
        self.fish.x += 0.1*(x-self.fish.x)
        self.fish.y += 0.1*(y-self.fish.y)
        self.fish.collider.update_position(self.fish.x, self.fish.y)
    
    def draw(self):
        self.fish.draw()
    


class Item:
    def __init__(self, x=0, y=0, size=1.0, move_down = False):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random.uniform(0.005, 0.01)
        if move_down:
            self.speed *= -1
        self.collider = None

    def update_position(self):
        self.y += self.speed
        self.collider.update_position(self.x, self.y)

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


FISH_CLASSES = [BasicFish, Shark, TropicalFish, ClownFish]
def spawn_fish():
    fish_class = FISH_CLASSES[random.randint(0, 3)]
    x = -1.9
    y = random.uniform(-0.95, 0.95)
    reverse = random.randint(0, 1) == 1
    if reverse:
        x = 1.9
    size = random.uniform(0.3, 1)
    selected_color = random.randint(0, len(fish_class.color_schemes) - 1)
    return fish_class(x, y, size, reverse, selected_color)

ITEM_CLASSES = [Bubble, Star, ExtraLife]
def spawn_item():
    item_class = ITEM_CLASSES[random.randint(0,2)]
    x = random.uniform(-1.5, 1.5)
    y = -1.1
    move_down = random.randint(0, 1) == 1
    if move_down:
        y = 1.1
    return item_class(x, y, 1, move_down)


class FishCollider:
    def __init__(self, x, y, rx, ry, scale=1.0):
        self.x = x
        self.y = y
        self.rx = scale*rx
        self.ry = scale*ry

    def update_position(self, x, y):
        self.x = x
        self.y = y

class ItemCollider:
    def __init__(self, x, y, r, scale=1.0):
        self.x = x
        self.y = y
        self.r = scale*r

    def update_position(self, x, y):
        self.x = x
        self.y = y


def check_ellipse_collision(fish1_collider: FishCollider, fish2_collider: FishCollider):
    dx = (fish1_collider.x - fish2_collider.x) / (fish1_collider.rx + fish2_collider.rx)
    dy = (fish1_collider.y - fish2_collider.y) / (fish1_collider.ry + fish2_collider.ry)
    return dx*dx + dy*dy < 1

def check_ellipse_circle_collision(fish_collider: FishCollider, item_collider: ItemCollider):
    # Normalize the circle's position relative to the ellipse
    dx = (item_collider.x - fish_collider.x) / fish_collider.rx
    dy = (item_collider.y - fish_collider.y) / fish_collider.ry

    # Distance from ellipse center to circle center in normalized space
    distance = mm.sqrt(dx*dx + dy*dy)

    # Circle's radius also needs to be scaled (average of x/y scale)
    avg_scale = (1/fish_collider.rx + 1/fish_collider.ry) / 2
    scaled_r = item_collider.r * avg_scale

    return distance < (1 + scaled_r)


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

    player = Player(BasicFish(0, 0, 0.6))
    #fishList = [TropicalFish(0, 0.8), ClownFish(0, 0.2), Shark(0, -0.5)] 
    fishList = []
    items = []

    fish_spawn_timer = pg.USEREVENT + 1
    pg.time.set_timer(fish_spawn_timer, 4000)
    item_spawn_timer = pg.USEREVENT + 2
    pg.time.set_timer(item_spawn_timer, 7000)
    immunity_timer = pg.USEREVENT + 3

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == fish_spawn_timer:
                fishList.append(spawn_fish())
            elif event.type == item_spawn_timer:
                items.append(spawn_item())
            elif event.type == immunity_timer:
                player.is_immune = False
                


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #background
        draw_image(background, -1.6, -1)
        
        for fish in fishList.copy():
            if fish.x < -2 or fish.x > 2:
                fishList.remove(fish)
                continue
            fish.update_position()
            fish.draw()
            if check_ellipse_collision(player.fish.collider, fish.collider):
                if player.fish.size >= fish.size:
                    player.fish.size += 0.04*fish.size
                    player.score += 10*fish.size
                    fishList.remove(fish)
                elif(not player.is_immune):
                    player.lives -= 1
                    player.is_immune = True
                    pg.time.set_timer(immunity_timer, 5000, 1)

            
        x_mouse, y_mouse = pg.mouse.get_pos()
        x_mouse = x_mouse*3.2/display[0] - 1.6    #x is normalized from [0, 1600] to [-1.6, 1.6] 
        y_mouse = 1 - y_mouse*2/display[1]        #y is normalized from [1000, 0] to [-1, 1]
        player.update_position(x_mouse, y_mouse)
        player.draw()
        
        for item in items.copy():
            if item.y < -1.2 or item.y > 1.2:
                items.remove(item)
                continue
            item.update_position()
            item.draw()
            if check_ellipse_circle_collision(player.fish.collider, item.collider):
                if(type(item) == Bubble):
                    player.score += 1
                elif(type(item) == Star):
                    player.score += 10
                elif(type(item) == ExtraLife):
                    player.lives += 1
                items.remove(item)

        

        draw_text(f"Score: {int(player.score)}", -1.55, 0.87, 50)
        draw_text(f"Lives: {player.lives}", 1.25, 0.87, 50)

        pg.display.flip()
        pg.time.wait(10)

main()
