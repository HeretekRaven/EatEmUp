import pygame
import random

W = 1500
H = 800

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
off_white_f = (220, 0, 200)
off_white_w = (200, 0, 100)

pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("NomNom Demo")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame1 = pygame.image.load("sprite_0.png")
        self.frame2 = pygame.image.load("sprite_1.png")
        self.frame3 = pygame.image.load("sprite_2.png")
        self.frame4 = pygame.image.load("sprite_3.png")
        self.frame1b = pygame.image.load("sprite_0b.png")
        self.frame2b = pygame.image.load("sprite_1b.png")
        self.frame3b = pygame.image.load("sprite_2b.png")
        self.frame4b = pygame.image.load("sprite_3b.png")
        self.frame1c = pygame.image.load("sprite_1c.png")
        self.frame2c = pygame.image.load("sprite_3c.png")
        self.frame3c = pygame.image.load("sprite_5c.png")
        self.frame4c = pygame.image.load("sprite_7c.png")
        self.frame1d = pygame.image.load("sprite_1d.png")
        self.frame2d = pygame.image.load("sprite_3d.png")
        self.frame3d = pygame.image.load("sprite_5d.png")
        self.frame4d = pygame.image.load("sprite_7d.png")
        self.framehd1 = pygame.image.load("spritehd_0.png")
        self.framehd1b = pygame.image.load("spritehd_0b.png")
        self.framehd2 = pygame.image.load("spritehd_1.png")
        self.framehd2b = pygame.image.load("spritehd_1b.png")
        self.framehd3 = pygame.image.load("spritehd_2.png")
        self.framehd3b = pygame.image.load("spritehd_2b.png")
        self.framehd4 = pygame.image.load("spritehd_3.png")
        self.framehd4b = pygame.image.load("spritehd_3b.png")
        self.image = self.frame1
        #self.image = pygame.Surface((30,30))
        #self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400
        self.change_x = 0
        self.change_y = 0
        self.frame = 1
        self.dir = 1
        self.tick = 0
        self.bite = False
        self.bitenum = 0
        self.hidden = False
        self.feet = 90
        self.Ltimer = 0
        self.lunge = False
        #Use speed for collision checks

        self.speed = 10
        self.attack = 10
        self.stealth = 10
    def update(self):
        #floored = pygame.sprite.spritecollide(self, all_sprites, False)
        self.change_x = 0
        self.change_y = 0
        self.walking = False
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.change_y += -1 * self.speed
            self.walking = True
        if key[pygame.K_a]:
            self.change_x += -1 * self.speed
            self.walking = True
            self.dir = 0
        if key[pygame.K_s]:
            self.change_y += self.speed
            self.walking = True
        if key[pygame.K_d]:
            self.change_x += self.speed
            self.walking = True
            self.dir = 1

        if self.tick < 2:
            self.tick += 1
        else:
            self.tick = 0
            if self.walking == True and self.frame < 4:
                self.frame += 1
            else:
                self.frame = 2
            if self.walking == False:
                self.frame = 1

        grass = pygame.sprite.spritecollide(self, cover_inst, False)
        if grass:
            self.hidden = True
        else:
            self.hidden = False
        
            
        if self.frame == 1 and self.bite == False:
            self.image = self.frame1
        if self.frame == 2 and self.bite == False:
            self.image = self.frame2
        if self.frame == 3 and self.bite == False:
            self.image = self.frame3
        if self.frame == 4 and self.bite == False:
            self.image = self.frame4

        if self.frame == 1 and self.dir == 1 and self.bite == False:
            self.image = self.frame1
        if self.frame == 2 and self.dir == 1 and self.bite == False:
            self.image = self.frame2
        if self.frame == 3 and self.dir == 1 and self.bite == False:
            self.image = self.frame3
        if self.frame == 4 and self.dir == 1 and self.bite == False:
            self.image = self.frame4

        if self.frame == 1 and self.dir == 0 and self.bite == False:
            self.image = self.frame1b
        if self.frame == 2 and self.dir == 0 and self.bite == False:
            self.image = self.frame2b
        if self.frame == 3 and self.dir == 0 and self.bite == False:
            self.image = self.frame3b
        if self.frame == 4 and self.dir == 0 and self.bite == False:
            self.image = self.frame4b

        if self.frame == 1 and self.dir == 0 and self.bite == True:
            self.image = self.frame1d
        if self.frame == 2 and self.dir == 0 and self.bite == True:
            self.image = self.frame2d
        if self.frame == 3 and self.dir == 0 and self.bite == True:
            self.image = self.frame3d
        if self.frame == 4 and self.dir == 0 and self.bite == True:
            self.image = self.frame4d

        if self.frame == 1 and self.dir == 1 and self.bite == True:
            self.image = self.frame1c
        if self.frame == 2 and self.dir == 1 and self.bite == True:
            self.image = self.frame2c
        if self.frame == 3 and self.dir == 1 and self.bite == True:
            self.image = self.frame3c
        if self.frame == 4 and self.dir == 1 and self.bite == True:
            self.image = self.frame4c

        if self.frame == 1 and self.dir == 1 and self.bite == False and self.hidden == True:
            self.image = self.framehd1
        if self.frame == 2 and self.dir == 1 and self.bite == False and self.hidden == True:
            self.image = self.framehd3
            a = Particle(self.rect.x, self.rect.y + 50, 1)
            thing.add(a)
        if self.frame == 3 and self.dir == 1 and self.bite == False and self.hidden == True:
            self.image = self.framehd1
        if self.frame == 4 and self.dir == 1 and self.bite == False and self.hidden == True:
            self.image = self.framehd3

        if self.frame == 1 and self.dir == 0 and self.bite == False and self.hidden == True:
            self.image = self.framehd1b
        if self.frame == 2 and self.dir == 0 and self.bite == False and self.hidden == True:
            self.image = self.framehd3b
            a = Particle(self.rect.x, self.rect.y + 50, 1)
            thing.add(a)
        if self.frame == 3 and self.dir == 0 and self.bite == False and self.hidden == True:
            self.image = self.framehd1b
        if self.frame == 4 and self.dir == 0 and self.bite == False and self.hidden == True:
            self.image = self.framehd3b
           

        if self.frame == 1 and self.dir == 1 and self.bite == True and self.hidden == True:
            self.image = self.framehd2
        if self.frame == 2 and self.dir == 1 and self.bite == True and self.hidden == True:
            self.image = self.framehd4
            a = Particle(self.rect.x, self.rect.y + 50, 1)
            thing.add(a)
        if self.frame == 3 and self.dir == 1 and self.bite == True and self.hidden == True:
            self.image = self.framehd2
        if self.frame == 4 and self.dir == 1 and self.bite == True and self.hidden == True:
            self.image = self.framehd4
          

        if self.frame == 1 and self.dir == 0 and self.bite == True and self.hidden == True:
            self.image = self.framehd2b
        if self.frame == 2 and self.dir == 0 and self.bite == True and self.hidden == True:
            self.image = self.framehd4b
            a = Particle(self.rect.x, self.rect.y + 50, 1)
            thing.add(a)
        if self.frame == 3 and self.dir == 0 and self.bite == True and self.hidden == True:
            self.image = self.framehd2b
        if self.frame == 4 and self.dir == 0 and self.bite == True and self.hidden == True:
            self.image = self.framehd4b
           
            


        if self.bite == True and self.bitenum < 3:
            self.bitenum += 1
            

        else:
            self.bite = False
            self.bitenum = 0

        if self.lunge == True:
            if self.dir == 1:
                if self.Ltimer >= 15:
                    self.change_x += 30
                if self.Ltimer < 15 and self.Ltimer > 5:
                    self.change_x += 30
                if self.Ltimer <= 5:
                    self.change_x += 30
                if self.Ltimer <= 0:
                    self.lunge = False
                    self.Ltimer = 0
            if self.dir == 0:
                if self.Ltimer >= 15:
                    self.change_x += -30
                if self.Ltimer < 15 and self.Ltimer > 5:
                    self.change_x += -30
                if self.Ltimer < 5:
                    self.change_x += -30
                if self.Ltimer <= 0:
                    self.lunge = False
                    self.Ltimer = 0
            

        if self.Ltimer > 0:
            self.Ltimer += -1
            
            




        
        if self.rect.y - self.speed <= floor.top:
            if self.change_y < 0:
                self.change_y = 0
        if self.rect.y + self.speed >= floor.bottom:
            if self.change_y > 0:
                self.change_y = 0
        
        
        #grass = pygame.sprite.spritecollide(self, cover_inst, False)
        #if grass:
            #self.hidden = True
        #else:
            #self.hidden = False
            
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
    def moveX(self, value = 0):
        self.change_x = value
    def moveY(self, value = 0):
        self.change_y = value
    def placeX(self):
        return self.rect.x
    def placeY(self):
        return self.rect.y
    def level_up(self, speed = 1):
        self.speed += speed
    def chomp(self):
        self.bite = True
    def Lunge(self):
        if self.lunge == False:
            self.Ltimer = 20
        self.lunge = True
    def hide(self):
        hide = self.hidden
        return hide
        

class Runner(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.frame1 = pygame.image.load("sprite_0r.png")
        self.frame2 = pygame.image.load("sprite_1r.png")
        self.frame3 = pygame.image.load("sprite_2r.png")
        self.frame4 = pygame.image.load("sprite_3r.png")
        self.frame5 = pygame.image.load("sprite_4r.png")
        self.frame10 = pygame.image.load("sprite_0r0.png")
        self.frame20 = pygame.image.load("sprite_1r0.png")
        self.frame30 = pygame.image.load("sprite_2r0.png")
        self.frame40 = pygame.image.load("sprite_3r0.png")
        self.frame50 = pygame.image.load("sprite_4r0.png")
        self.framed = pygame.image.load("sprite_0rk.png")
        self.frame1d = pygame.image.load("sprite_1rk.png")
        self.frame2d = pygame.image.load("sprite_2rk.png")
        self.image = self.frame1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.frame = 1
        self.dir = 1
        self.tick = 0
        self.walking = False
        self.alert = False
        self.timer = 0
        self.movex = 0
        self.movey = 0
        self.viewdist = 80

        self.speed = 20

    def update(self):
        #floored = pygame.sprite.spritecollide(self, all_sprites, False)
        self.change_x = 0
        self.change_y = 0
        rng = 0

        if self.tick < 2:
            self.tick += 1
        else:
            self.tick = 0
            if self.walking == True and self.frame < 5:
                self.frame += 1
            else:
                self.frame = 2
            if self.walking == False:
                self.frame = 1

        
        if self.frame == 1 and self.dir == 1:
            self.image = self.frame1
        if self.frame == 2 and self.dir == 1:
            self.image = self.frame2
        if self.frame == 3 and self.dir == 1:
            self.image = self.frame3
        if self.frame == 4 and self.dir == 1:
            self.image = self.frame4
        if self.frame == 5 and self.dir == 1:
            self.image = self.frame5

        if self.frame == 1 and self.dir == 0:
            self.image = self.frame10
        if self.frame == 2 and self.dir == 0:
            self.image = self.frame20
        if self.frame == 3 and self.dir == 0:
            self.image = self.frame30
        if self.frame == 4 and self.dir == 0:
            self.image = self.frame40
        if self.frame == 5 and self.dir == 0:
            self.image = self.frame50

        if self.walking == False and self.alert == False:
            rng = random.randint(1,30)
        if rng == 9:
            self.walking = True
            self.timer += 10
            self.movey = random.randint(-10,10)
            self.movex = random.randint(-10,10)
            if self.movex > 0:
                self.dir = 1
            else:
                self.dir = 0
        if self.walking == True: 
            self.timer += -1

        if self.timer <= 0:
            self.timer = 0
            self.walking = False
            self.movex = 0
            self.movey = 0
        
        self.change_x += self.movex
        self.change_y += self.movey

        if self.alert == True:
            self.walking = True
            self.timer = 1000

            if self.rundir == 1:
                self.change_x = self.speed
                self.dir = 1
                mark = Mark(self.rect.x + 70, self.rect.y - 70, self.change_x, self.change_y)
                thing.add(mark)
            else:
                self.change_x = -1 * self.speed
                self.dir = 0
                mark = Mark(self.rect.x, self.rect.y - 70, self.change_x, self.change_y)
                thing.add(mark)

        eaten = pygame.sprite.spritecollide(self, player_inst, False)
        if eaten and player.bite == True:
            corpse = CorpseR(self.rect.x,self.rect.y)
            for i in range(10):
                a = Particle(self.rect.x + 25, self.rect.y + 50, 2)
                thing.add(a)
            dead_inst.add(corpse)
            self.kill()
        
        if self.dir == 1:
            self.rect.x += self.viewdist
            close = pygame.sprite.spritecollide(self, player_inst, False)
            if close:
                if player.hide() == False and self.alert == False:
                    self.alert = True
                    rng2 = random.randint(1,2)
                    self.rundir = rng2
                    self.startle()
                self.rect.x -= self.viewdist
            else:
                self.rect.x -= self.viewdist
        if self.dir == 0:
            self.rect.x -= self.viewdist 
            closer = pygame.sprite.spritecollide(self, player_inst, False)
            if closer:
                if player.hide() == False and self.alert == False:
                    self.alert = True
                    rng2 = random.randint(1,2)
                    self.rundir = rng2
                    self.startle()
                self.rect.x += self.viewdist 
            else:
                self.rect.x += self.viewdist

        self.rect.y -= self.viewdist 
        closerish = pygame.sprite.spritecollide(self, player_inst, False)
        if closerish:
            if player.hide() == False and self.alert == False:
                self.alert = True
                rng2 = random.randint(1,2)
                self.rundir = rng2
                self.startle()
            self.rect.y += self.viewdist 
        else:
            self.rect.y += self.viewdist
        self.rect.y += self.viewdist 
        closerestish = pygame.sprite.spritecollide(self, player_inst, False)
        if closerestish:
            if player.hide() == False and self.alert == False:
                self.alert = True
                rng2 = random.randint(1,2)
                self.rundir = rng2
                self.startle()
            self.rect.y -= self.viewdist 
        else:
            self.rect.y -= self.viewdist
        
        closest = pygame.sprite.spritecollide(self, player_inst, False)
        if closest:
            if player.hide() == False and self.alert == False:
                self.alert = True
                rng2 = random.randint(1,2)
                self.rundir = rng2
                self.startle()


        if self.change_y + self.rect.y >= floor.bottom - 100:
            if self.change_y > 0:
                self.change_y = 0
        if self.change_y + self.rect.y <= floor.top - 50:
            if self.change_y < 0:
                self.change_y = 0
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
    def startle(self):
        if self.rundir == 1:
            a = self.speed
        else:
            a = -1 * self.speed
        
        #all_sprites.add(mark)
        #thing.add(mark)

        
#Utility and prop classes        

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500,500))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = H - 600
        self.top = 150
        self.bottom = 600
    def update(self):
        self.pop = 0
        
class Tall_grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.frame1 = pygame.image.load("sprite_0g.png")
        self.frame2 = pygame.image.load("sprite_1g.png")
        self.image = self.frame1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        stepped = pygame.sprite.spritecollide(self, player_inst, False)
        if stepped:
            self.image = self.frame2
        else:
            self.image = self.frame1

class Mark(pygame.sprite.Sprite):
    def __init__(self, X, Y, movex, movey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("stealthalt.png")
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.change_x = movex
        self.change_y = movey
        self.timer = 2
    def update(self):
        self.timer += -1
        if self.timer <= 0:
            self.kill()
        self.rect.x += self.change_x
        self.rect.y += self.change_y

class CorpseR(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frame1 = pygame.image.load("sprite_1rk.png")
        self.frame2 = pygame.image.load("sprite_2rk.png")
        self.image = pygame.image.load("sprite_0rk.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.eaten = False
        self.tick = 0
        self.bleh = 1
        self.timer = 200
    def update(self):
        eaten = pygame.sprite.spritecollide(self, player_inst, False)
        if eaten and player.bite == True and self.tick == 3 and self.eaten != True:
            self.eaten = True
            global Hun
            if Hun < 10:
                Hun += 1
        if self.tick < 3:
            self.tick += 1
        if self.tick == 3:
            self.image = pygame.image.load("sprite_1rk.png")
        if self.eaten == True:
            self.image = pygame.image.load("sprite_2rk.png")
            if self.bleh == 1:
                for i in range(10):
                    a = Particle(self.rect.x + 25, self.rect.y + 60, 2)
                    thing.add(a)
                self.bleh = 0
        if self.timer <= 0:
            self.kill()
        if self.timer > 0:
            self.timer += -1

            

class Spookzone(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 1
    def update(self):
        if self.timer <= 0:
            self.kill()
        self.timer += -1

class IconHP(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprite_health.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class IconHu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprite_bar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        if a == 1:
            self.image = pygame.image.load("spritesingle_0.png")
        if a == 2:
            rng3 = random.randint(0,3)
            if rng3 == 0:
                self.image = pygame.image.load("spritegore_0.png")
            if rng3 == 1:
                self.image = pygame.image.load("spritegore_1.png")
            if rng3 == 2:
                self.image = pygame.image.load("spritegore_2.png")
            if rng3 == 3:
                self.image = pygame.image.load("spritegore_3.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 20
        self.rng1 = random.randint(-10,10)
        self.rng2 = random.randint(-20,-5)
        self.done = False
        self.change_x = self.rng1
        self.change_y = self.rng2
        self.y = self.rng2
    def update(self):
        if self.timer <= 0:
            self.kill()
        if self.done == True:
            self.timer += -1
        else:
            self.change_y += 1
            if self.change_y >= -1 * self.y:
                self.change_y = 0
                self.change_x = 0
                self.done = True
        
        
            
        
        
        

        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        
    
        

gen = 0        
class Game():
    def __init__(self):
        self.lvl = 1
    def gen_1(self):
        global gen
        gen = 1
    #def clear(self):
        

Hp = 5
Hun = 6
Hp_space = 60
Hun_timer = 0
new = 0
    


font = pygame.font.SysFont("Times New Roman", 20)   
all_sprites = pygame.sprite.Group()
player_inst = pygame.sprite.Group()
prey_inst = pygame.sprite.Group()
cover_inst = pygame.sprite.Group()
thing = pygame.sprite.Group()
floor_inst = pygame.sprite.Group()
bar = pygame.sprite.Group()
dead_inst = pygame.sprite.Group()


 
console = Game()
console.gen_1()



if gen == 1:
        floor = Floor()
        floor_inst.add(floor)
        
        grass = Tall_grass(600,400)
        cover_inst.add(grass)
        i = 7
        for i in range(0,7):
            rngx = random.randint(0, 1500)
            rngy = random.randint(floor.top,floor.bottom)
            runner = Runner(rngx, rngy)
            all_sprites.add(runner)
            prey_inst.add(runner)
            i += -1
        for i in range(0,7):
            rngx = random.randint(0, 1500)
            rngy = random.randint(floor.top,floor.bottom)
            g = Tall_grass(rngx, rngy)
            cover_inst.add(g)
            i += -1


        player = Player()
        all_sprites.add(player)
        player_inst.add(player)



Quit = False
while not Quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.chomp()
            #if event.key == pygame.K_q:
                #player.Lunge()
    if Hun_timer < 200:
        Hun_timer += 1
    if Hun_timer >= 200:
        Hun_timer = 0
        Hun += -1
        new = 1
        if Hun <= 0:
            Hun = 0
            Hp += -1
        if Hp <= 0:
            Quit = True
    bar.empty()
    for i in range(Hp):
        a = IconHP(Hp_space * i, 5)
        bar.add(a)
        i += -1
    for i in range(Hun):
        b = IconHu(Hp_space * i, 60)
        bar.add(b)
        i += -1

    if new == 1:
        rngx = random.randint(0, 1500)
        rngy = random.randint(floor.top,floor.bottom)
        runner = Runner(rngx, rngy)
        all_sprites.add(runner)
        prey_inst.add(runner)
        new += -1
    
    


                
        

            
    all_sprites.update()
    cover_inst.update()
    floor_inst.update()
    dead_inst.update()
    thing.update()
    pygame.display.flip()
    win.fill(black)
    floor_inst.draw(win)
    cover_inst.draw(win)
    dead_inst.draw(win)
    all_sprites.draw(win)
    thing.draw(win)
    bar.draw(win)
    #board = font.render("Shield: " + player.s * " [X] ", True, white)
    clock.tick(30)








pygame.quit()
quit()




