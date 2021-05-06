# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
#      import CYAN as CYAN
import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

# HUD functions
def draw_player_health(surf,x,y,pct):
    if pct<0:
        pct=0
    BAR_LENGTH=100
    BAR_HEIGHT=20
    fill=pct*BAR_LENGTH
    outline_rect=pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pg.Rect(x,y,fill,BAR_HEIGHT)
    if pct > 0.6:
        col=GREEN
    elif pct>0.3:
        col=YELLOW
    else:
        col=RED
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect,2)
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) #꾹누르면 움직이게 하는 코드 (500밀리초동안기다리고,100밀리초동안 반복)
        self.load_data()

    def load_data(self):
        game_folder=path.dirname(__file__) #현재 main이있는 파일 경로
        img_folder=path.join(game_folder,'img2')
        img_folder2=path.join(game_folder,'img')
        img_folder3=path.join(game_folder,'frames')
        map_folder=path.join(game_folder,'maps')
        self.map=TiledMap(path.join(map_folder,'4155.tmx'))
        self.map_img=self.map.make_map()
        self.map_rect=self.map_img.get_rect()
        self.player_img=pg.image.load(path.join(img_folder,PLAYER_IMG)).convert_alpha()#
        self.bullet_img=pg.image.load(path.join(img_folder3,BULLET_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder3, MOB_IMG)).convert_alpha()#img2폴더 img_folder
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        self.wall_img=pg.image.load(path.join(img_folder2,WALL_IMG)).convert_alpha()#img폴더 img_folder2
        self.wall_img=pg.transform.scale(self.wall_img,(TILESIZE,TILESIZE))


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs=pg.sprite.Group()
        self.bullets=pg.sprite.Group()
        #for row,tiles in enumerate(self.map.data): #row=index tiles=value
            #for col, tile in enumerate(tiles): #col=index tile=value
               # if tile=='1':
                   # Wall(self,col,row)
               # if tile=='M':
                    #Mob(self,col,row)
                #if tile=='P':
                    #self.player=Player(self,col,row)
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name=='player':
                self.player=Player(self,tile_object.x,tile_object.y)
            if tile_object.name=='monster':
                Mob(self,tile_object.x,tile_object.y)
            if tile_object.name=='wall' :
                Obstacle(self,tile_object.x,tile_object.y
                         ,tile_object.width,tile_object.height)
        self.camera=Camera(self.map.width, self.map.height)
        self.draw_debug=False

    def run(self): #동작시키는 함수
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()   #event
            self.update()   #update
            self.draw()     #draw

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        #mobs hit player
        hits=pg.sprite.spritecollide(self.player,self.mobs,False,collide_hit_rect)
        for hit in hits:
            self.player.health-=MOB_DAMAGE
            hit.vel=vec(0,0)
            if self.player.health<=0:
                self.playing=False
            if hits:
                self.player.pos+=vec(MOB_KNOCKBACK,0).rotate(-hits[0].rot)
        #bullets hit mobs
        hits=pg.sprite.groupcollide(self.mobs,self.bullets,False,True)
        for hit in hits:
            hit.health-=BULLET_DAMAGE
            hit.vel=vec(0,0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()



    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key==pg.K_h:
                    self.draw_debug=not self.draw_debug


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()