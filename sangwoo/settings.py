import pygame as pg
vec = pg.math.Vector2

#컬러 정하기
WHITE=(255,255,255)
BLACK=(0,0,0)
DARKGREY=(40,40,40)
LIGHTGREY=(100,100,100)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)
BROWN=(100,55,5)
CYAN = (0, 255, 255)

#게임 세팅
WIDTH=640
HEIGHT=480
FPS=60
TITLE="Tilemap Demo"
BGCOLOR=BROWN

TILESIZE=16
GRIDWIDTH=WIDTH/TILESIZE
GRIDHEIGHT=HEIGHT/TILESIZE


WALL_IMG='tileGreen_39.png'

# Player settings
PLAYER_HEALTH=100
PLAYER_SPEED = 230
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'wizzard_f_idle_anim_f0.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET=vec(30,10)

#Gun settings
BULLET_IMG='weapon_katana.png'
BULLET_SPEED=500
BULLET_LIFETIME=1000
BULLET_RATE=150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE=10

# Mob settings
MOB_IMG = 'ogre_idle_anim_f1.png'
MOB_SPEEDS = [150,100,75,125]
MOB_HEALTH=100
MOB_HIT_RECT = pg.Rect(0,0,30,30)
MOB_DAMAGE=10
MOB_KNOCKBACK=20
AVOID_RADIUS=50