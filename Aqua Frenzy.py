import pygame as pg
import math as mm
import random
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from shapes import *
from fish import *
from items import *

class Player:
    initial_size = 0.6
    def __init__(self, lives = 3, score = 0):
        fish_class = random.choice(FISH_CLASSES) 
        self.fish = fish_class(0, 0, self.initial_size)
        self.lives = lives
        self.score = score
        self.is_immune = False
        self.lost = False
        
    def update_position(self, x, y):
        #x and y are the cursor cooridnates
        if self.lost:
            return
        self.fish.reverse = x-self.fish.x < 0
        #increment the player position by a fraction of the distance between the player and the cursor
        #this makes the player fish move faster when it's further away from the cursor, and slows down as it approaches the cursor
        self.fish.x += 0.1*(x-self.fish.x)
        self.fish.y += 0.1*(y-self.fish.y)
        self.fish.collider.update_position(self.fish.x, self.fish.y)
    
    def draw(self):
        if self.lost:
            return
        self.fish.draw()
    
    def check_loss(self):
        if self.lost:
            rectangle(-1.6, -1, 1.6, 1, 0, 0, 0, 0.5)     #semi transparent black overlay
            draw_text("GAME OVER", -0.4, 0.1, 70, (255, 0, 0))
            draw_text(f"FINAL SCORE: {int(self.score)}", -0.5, -0.1, 70, (255, 0, 0))
            draw_text("Press any key to restart", -0.5, -0.6, 50, (255, 0, 0))
    

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


FISH_CLASSES = (BasicFish, Shark, TropicalFish, ClownFish)
def spawn_fish():
    fish_class = random.choice(FISH_CLASSES)
    x = -1.9
    y = random.uniform(-0.95, 0.95)
    reverse = random.randint(0, 1) == 1
    if reverse:
        x = 1.9
    size = random.uniform(0.3, 1)
    selected_color = random.randint(0, len(fish_class.color_schemes) - 1)
    return fish_class(x, y, size, reverse, selected_color)

ITEM_CLASSES = (Bubble, Star, ExtraLife)
def spawn_item():
    item_class = None
    #25% chance of spawning an extra life
    if random.random() < 0.25:
        item_class = ExtraLife
    else:
        item_class = ITEM_CLASSES[random.randint(0,1)]
        
    x = random.uniform(-1.5, 1.5)
    y = -1.1
    move_down = random.randint(0, 1) == 1
    if move_down:
        y = 1.1
    return item_class(x, y, 1, move_down)


def check_fish_collision(fish1_collider: FishCollider, fish2_collider: FishCollider):
    #scale the distance between centers relative to the ellipses' combined size (scale the ellipses to circles)
    dx = (fish1_collider.x - fish2_collider.x) / (fish1_collider.rx + fish2_collider.rx)
    dy = (fish1_collider.y - fish2_collider.y) / (fish1_collider.ry + fish2_collider.ry)
    #dx and dy represent the normalized distance between the ellipses' centers
    #if dx and dy are inside a unit circle, this means the normalized distance is less than 1 and the ellipses are colliding
    return dx*dx + dy*dy < 1

def check_fish_item_collision(fish_collider: FishCollider, item_collider: ItemCollider):
    # normalize the circle's position relative to the ellipse
    dx = (item_collider.x - fish_collider.x) / fish_collider.rx
    dy = (item_collider.y - fish_collider.y) / fish_collider.ry

    # distance from ellipse center to circle center in normalized space
    distance = mm.sqrt(dx*dx + dy*dy)

    # circle's radius also needs to be scaled (average of x/y scale)
    avg_scale = (1/fish_collider.rx + 1/fish_collider.ry) / 2
    scaled_r = item_collider.r * avg_scale

    return distance < (1 + scaled_r)


def main():
    pg.init()
  
    display = (1600,1000)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    glOrtho(-1.6, 1.6, -1, 1, -1, 1)

    #enable transparency
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #enable depth
    glEnable(GL_DEPTH_TEST)  
    glDepthFunc(GL_LEQUAL)
    
    assets_path = "assets/"
    background = pg.image.load(assets_path + "background.jpeg")

    bubble_sound = pg.mixer.Sound(assets_path + "bubble-pop.mp3")
    eat_sound = pg.mixer.Sound(assets_path + "eat.mp3")
    lose_life_sound = pg.mixer.Sound(assets_path + "eaten.mp3")
    extra_life_sound = pg.mixer.Sound(assets_path + "extra-life.mp3")
    game_over_sound = pg.mixer.Sound(assets_path + "game-over.mp3")
    level_up_sound = pg.mixer.Sound(assets_path + "level-up.mp3")
    music = pg.mixer.Sound(assets_path + "music.mp3")
    star_sound = pg.mixer.Sound(assets_path + "star-pickup.mp3")

    player = Player()
    fish_list = []
    items = []

    fish_spawn_rate = 4000   #decreases as the player levels up
    fish_spawn_timer = pg.USEREVENT + 1
    pg.time.set_timer(fish_spawn_timer, fish_spawn_rate)
    item_spawn_timer = pg.USEREVENT + 2
    pg.time.set_timer(item_spawn_timer, 7000)
    immunity_timer = pg.USEREVENT + 3

    music.play(-1)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == fish_spawn_timer:
                fish_list.append(spawn_fish())
            elif event.type == item_spawn_timer:
                items.append(spawn_item())
            elif event.type == immunity_timer:
                player.is_immune = False
            elif player.lost and (event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN):
                #reset game
                player = Player()
                fish_list.clear()
                items.clear()
                Fish.speed_multiplier = 1.0
                fish_spawn_rate = 4000
                pg.time.set_timer(fish_spawn_timer, fish_spawn_rate)
                pg.time.set_timer(item_spawn_timer, 7000)
                music.play(-1)

                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #background
        draw_image(background, -1.6, -1)
        
        for fish in fish_list.copy():
            #remove off-screen fish
            if fish.x < -2 or fish.x > 2:
                fish_list.remove(fish)
                continue
            fish.update_position()
            fish.draw()
            if check_fish_collision(player.fish.collider, fish.collider) and not player.lost:
                #player fish eats the other fish
                if player.fish.size >= fish.size:
                    player.fish.size += 0.04*fish.size
                    player.score += 10*fish.size
                    fish_list.remove(fish)
                    #if player fish gets too big, reset its size, level up, and make the game harder
                    if player.fish.size >= 1.1:
                        level_up_sound.play()
                        player.score += 100
                        player.fish.size = Player.initial_size
                        Fish.speed_multiplier *= 1.1    #increase the speed of all other fish by 10%
                        if Fish.speed_multiplier > 5:
                            Fish.speed_multiplier = 5   #speed limit
                        fish_spawn_rate = int(0.8*fish_spawn_rate)   #decrease spawn time by 20%
                        if fish_spawn_rate < 1000:
                            fish_spawn_rate = 1000      #spawn rate limit
                        pg.time.set_timer(fish_spawn_timer, fish_spawn_rate)
                    #no level up happens
                    else:
                        eat_sound.play()
                #player fish gets eaten
                elif(not player.is_immune and not player.lost):
                    player.lives -= 1
                    lose_life_sound.play()
                    player.lost = player.lives == 0
                    if player.lost:
                        music.stop()
                        game_over_sound.play()
                    player.is_immune = True
                    pg.time.set_timer(immunity_timer, 3000, 1)

            
        x_mouse, y_mouse = pg.mouse.get_pos()
        x_mouse = x_mouse*3.2/display[0] - 1.6    #x is normalized from [0, 1600] to [-1.6, 1.6] 
        y_mouse = 1 - y_mouse*2/display[1]        #y is normalized from [1000, 0] to [-1, 1]
        player.update_position(x_mouse, y_mouse)
        player.draw()
        
        for item in items.copy():
            #remove off-screen items
            if item.y < -1.2 or item.y > 1.2:
                items.remove(item)
                continue
            item.update_position()
            item.draw()
            if check_fish_item_collision(player.fish.collider, item.collider) and not player.lost:
                if(type(item) == Bubble):
                    player.score += 1
                    bubble_sound.play()
                elif(type(item) == Star):
                    player.score += 10
                    star_sound.play() 
                elif(type(item) == ExtraLife):
                    player.lives += 1
                    extra_life_sound.play()
                items.remove(item)

        
        
        draw_text(f"Score: {int(player.score)}", -1.55, 0.87, 50)
        lives_color = (255, 255, 255)
        if player.is_immune:
            lives_color = (255, 0, 0)   #immunity indicator
        draw_text(f"Lives: {player.lives}", 1.25, 0.87, 50, lives_color)

        player.check_loss()

        pg.display.flip()
        pg.time.wait(10)

main()
