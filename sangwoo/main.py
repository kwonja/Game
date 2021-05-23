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
import time

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
        img_folder3=path.join(game_folder,'frames')
        map_folder=path.join(game_folder,'maps2')
        snd_folder = path.join(game_folder, 'snd')#add
        pain_folder = path.join(snd_folder, 'pain')#add
        music_folder = path.join(game_folder, 'music') #add
        self.map=TiledMap(path.join(map_folder,'newmap.tmx'))
        self.map_img=self.map.make_map()
        self.map_rect=self.map_img.get_rect()
        self.player_img=pg.image.load(path.join(img_folder3,PLAYER_IMG)).convert_alpha()
        self.bullet_images={}
        #self.bullet_images['lg'] = pg.image.load(path.join(img_folder3, WEAPONS[game.player.weapon : 'bullet_image'])).convert_alpha()
        #self.bullet_images['sm'] = pg.transform.scale(self.bullet_images['lg'],(10,10))
        self.bullet_image=pg.image.load(path.join(img_folder3,'weapon_rusty_sword.png')).convert_alpha()
        #self.mob_img = pg.image.load(path.join(img_folder3, MOB_IMG)).convert_alpha()#img2폴더 img_folder
        #self.player_img = pg.transform.scale(self.player_img, (64, 64))
        #self.wall_img=pg.image.load(path.join(img_folder2,WALL_IMG)).convert_alpha()#img폴더 img_folder2
        #self.wall_img=pg.transform.scale(self.wall_img,(TILESIZE,TILESIZE))
        self.item_images={}
        for item in ITEM_IMAGES:
            self.item_images[item]=pg.image.load(path.join(img_folder3,ITEM_IMAGES[item])).convert_alpha()
        self.mob_images = {}
        for mob in MOB_IMAGES:
            self.mob_images[mob] =pg.image.load(path.join(img_folder3, MOB_IMAGES[mob])).convert_alpha()
            if mob=='boss':
                self.mob_images[mob]=pg.transform.scale(self.mob_images[mob],(64,64))
        # Sound loading
        pg.mixer.music.load(path.join(music_folder, BG_MUSIC))   #뮤직폴더에서 가져오기 위해 선언
        self.effects_sounds = {} ##힐팩사운드
        for type in EFFECTS_SOUNDS:
            if(type=='level_start'):
                start_music = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
                start_music.set_volume(0.1)
                self.effects_sounds[type] = start_music
            else:
                effect = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
                effect.set_volume(0.2)
                self.effects_sounds[type] = effect
        self.weapon_sounds = {}
        for snd in WEAPON_SOUNDS_GUN:
            s = pg.mixer.Sound(path.join(snd_folder, WEAPON_SOUNDS_GUN[snd]))
            s.set_volume(0.05)
            self.weapon_sounds[snd] = s
        self.player_hit_sounds = []
        for player in PLAYER_HIT_SOUNDS:
            self.player_hit_sounds.append(pg.mixer.Sound(path.join(pain_folder, player)))
        self.zombie_hit_sounds = []
        for mob in ZOMBIE_HIT_SOUNDS:
            self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, mob)))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs=pg.sprite.Group()
        self.bullets=pg.sprite.Group()
        self.items=pg.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            obj_center=vec(tile_object.x+tile_object.width/2,
                           tile_object.y+tile_object.height/2)
            if tile_object.name=='player':
                self.player=Player(self,obj_center.x,obj_center.y,PLAYER_SPEED1)
            if tile_object.name=='ogre':
                Mob(self,obj_center.x,obj_center.y,tile_object.name)
            if tile_object.name=='chort' :
                Mob(self,obj_center.x,obj_center.y,tile_object.name)
            if tile_object.name == in ['boss']:
                Mob(self,obj_center.x,obj_center.y,tile_object.name)
            if tile_object.name in ['zombie']:
                Mob(self,obj_center.x,obj_center.y,tile_object.name)
            if tile_object.name in ['muddy']:
                Mob(self,obj_center.x,obj_center.y,tile_object.name)
            if tile_object.name=='wall' :
                Obstacle(self,tile_object.x,tile_object.y
                         ,tile_object.width,tile_object.height)
            if tile_object.name in ['health1']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['health2']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['speed1']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['mace']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['chest']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['katana']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['rusty_sword']:
                Item(self,obj_center,tile_object.name)
            if tile_object.name in ['golden_sword']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name in ['spear']:
                Item(self, obj_center, tile_object.name)
        self.camera=Camera(self.map.width, self.map.height)
        self.draw_debug=False
        self.effects_sounds['level_start'].play()                   ##시작할때 음악


    def run(self): #동작시키는 함수
        # game loop - set self.playing = False to end the game
        self.playing = True
        pg.mixer.music.play(loops=-1)           #add -1이면 반복재생
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
        hits=pg.sprite.spritecollide(self.player,self.items,False)

        for tile_object in self.map.tmxdata.objects:
            obj_center=vec(tile_object.x+tile_object.width/2,
                           tile_object.y+tile_object.height/2)

        for hit in hits:
            if hit.type=='chest':
                self.effects_sounds['health_up'].play()
                Mob(self, obj_center.x, obj_center.y, 'imp')
                hit.kill()


        for hit in hits:
            if hit.type=='health1' and self.player.health<PLAYER_HEALTH:
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.add_health(HEALTH_PACK_AMOUNT1)
        for hit in hits:
            if hit.type=='health2' and self.player.health<PLAYER_HEALTH:
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.add_health(HEALTH_PACK_AMOUNT2)
        for hit in hits:
            if hit.type=='speed1':
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.speed=PLAYER_SPEED2
                seconds=self.clock.tick()/1000.0



        for hit in hits:
            if hit.type=='mace':
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.weapon='mace'
                game_folder = path.dirname(__file__)  # 현재 main이있는 파일 경로
                img_folder3 = path.join(game_folder, 'frames')
                self.bullet_image = pg.image.load(path.join(img_folder3, ITEM_IMAGES['mace'])).convert_alpha()

        for hit in hits:
            if hit.type=='katana':
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.weapon='katana'
                game_folder = path.dirname(__file__)  # 현재 main이있는 파일 경로
                img_folder3 = path.join(game_folder, 'frames')
                self.bullet_image = pg.image.load(path.join(img_folder3, ITEM_IMAGES['katana'])).convert_alpha()
        for hit in hits:
            if hit.type=='rusty_sword':
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.weapon='rusty_sword'
                game_folder = path.dirname(__file__)  # 현재 main이있는 파일 경로
                img_folder3 = path.join(game_folder, 'frames')
                self.bullet_image = pg.image.load(path.join(img_folder3, ITEM_IMAGES['rusty_sword'])).convert_alpha()
        for hit in hits:
            if hit.type=='spear':
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.weapon='spear'
                game_folder = path.dirname(__file__)  # 현재 main이있는 파일 경로
                img_folder3 = path.join(game_folder, 'frames')
                self.bullet_image = pg.image.load(path.join(img_folder3, ITEM_IMAGES['spear'])).convert_alpha()
        for hit in hits:
            if hit.type=='golden_sword':
                self.effects_sounds['health_up'].play()
                hit.kill()
                self.player.weapon='golden_sword'
                game_folder = path.dirname(__file__)  # 현재 main이있는 파일 경로
                img_folder3 = path.join(game_folder, 'frames')
                self.bullet_image = pg.image.load(path.join(img_folder3, ITEM_IMAGES['golden_sword'])).convert_alpha()
        #mobs hit player
        hits=pg.sprite.spritecollide(self.player,self.mobs,False,collide_hit_rect)
        for hit in hits:
            if random() < 0.7:
                choice(self.player_hit_sounds).play()
            self.player.health-=MOB[hit.type]['mob_damage']
            hit.vel=vec(0,0)
            if self.player.health<=0:
                self.playing=False
            if hits:
                self.player.pos+=vec(MOB[hit.type]['mob_knockback'],0).rotate(-hits[0].rot)
        #bullets hit mobs
        hits=pg.sprite.groupcollide(self.mobs,self.bullets,False,True)
        for hit in hits:
            hit.health-=WEAPONS[self.player.weapon]['damage'] * len(hits[hit])
            hit.vel=vec(0,0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
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

is_paused=False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True


# create the game object
g = Game()
g.show_start_screen()



while True:
    g.new()
    g.run()
    g.show_go_screen()