import pygame as pg

vec = pg.math.Vector2

# 컬러 정하기
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (100, 55, 5)
CYAN = (0, 255, 255)

# 게임 세팅
WIDTH = 640
HEIGHT = 480
FPS = 60
TITLE = "Cave Escape"
BGCOLOR = BROWN

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

SPEED_TIME_LIMIT1 = 5
SPEED_TIME_LIMIT2 = 8
INVINCIBLE_TIME_LIMIT1=10
INVINCIBLE_TIME_LIMIT2=15
POWER_UP_TIME1=5
POWER_UP_TIME2=8


# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED1 = 230
PLAYER_SPEED2 = 500
PLAYER_SPEED3=510
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'wizzard_f_idle_anim_f0.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings
BULLET_IMG = 'weapon_katana.png'
WEAPONS = {}
WEAPONS['katana'] = {'bullet_speed': 500,
                     'bullet_lifetime': 4000,
                     'rate': 230,
                     'kickback': 200,
                     'spread': 0,
                     'damage': 17,
                     'bullet_size': 'lg',
                     'bullet_count': 1,
                     'bullet_image': 'weapon_katana.png'}

WEAPONS['mace'] = {'bullet_speed': 150,
                   'bullet_lifetime': 3500,
                   'rate': 400,
                   'kickback': 250,
                   'spread': 3,
                   'damage': 25,
                   'bullet_size': 'lg',
                   'bullet_count': 1,
                   'bullet_image': 'weapon_mace.png'}

WEAPONS['rusty_sword'] = {'bullet_speed': 300,
                          'bullet_lifetime': 3000,
                          'rate': 200,
                          'kickback': 50,
                          'spread': 10,
                          'damage': 1,
                          'bullet_size': 'lg',
                          'bullet_count': 5,
                          'bullet_image': 'weapon_rusty_sword.png'
                          }

WEAPONS['spear'] = {'bullet_speed': 700,
                    'bullet_lifetime': 8000,
                    'rate': 600,
                    'kickback': 500,
                    'spread': 1,
                    'damage': 95,
                    'bullet_size': 'lg',
                    'bullet_count': 1,
                    'bullet_image': 'weapon_rusty_sword.png'
                    }

WEAPONS['golden_sword'] = {'bullet_speed': 700,
                           'bullet_lifetime': 8000,
                           'rate': 20,
                           'kickback': 1,
                           'spread': 50,
                           'damage': 0.5,
                           'bullet_size': 'lg',
                           'bullet_count': 10,
                           'bullet_image': 'weapon_golden_sword.png'
                           }

# Mob settings
MOB = {}
MOB['ogre'] = {
    'mob_speeds': 100,
    'mob_health': 100,
    'hit_rect': pg.Rect(0, 0, 30, 30),
    'mob_damage': 10,
    'mob_knockback': 15,
    'avoid_radius': 50
}
MOB['chort'] = {
    'mob_speeds': 200,
    'mob_health': 75,
    'hit_rect': pg.Rect(0, 0, 30, 30),
    'mob_damage': 5,
    'mob_knockback': 10,
    'avoid_radius': 200
}
MOB['imp'] = {
    'mob_speeds': 300,
    'mob_health': 30,
    'hit_rect': pg.Rect(0, 0, 30, 30),
    'mob_damage': 1,
    'mob_knockback': 2,
    'avoid_radius': 50
}

MOB['zombie'] = {
    'mob_speeds': 50,
    'mob_health': 120,
    'hit_rect': pg.Rect(0, 0, 30, 30),
    'mob_damage': 60,
    'mob_knockback': 100,
    'avoid_radius': 50
}

MOB['boss'] = {
    'mob_speeds': 100,
    'mob_health': 1000,
    'hit_rect': pg.Rect(0, 0, 30, 30),
    'mob_damage': 34,
    'mob_knockback': 100,
    'avoid_radius': 50
}

MOB['muddy'] = {
    'mob_speeds': 10,
    'mob_health': 300,
    'hit_rect': pg.Rect(0, 0, 30, 30),
    'mob_damage': 20,
    'mob_knockback': 100,
    'avoid_radius': 200
}

MOB_IMAGES = {'ogre': 'ogre_idle_anim_f1.png',
              'chort': 'chort_idle_anim_f0.png',
              'imp': 'imp_idle_anim_f0.png',
              'zombie': 'big_zombie_idle_anim_f0.png',
              'boss': 'big_demon_idle_anim_f0.png',
              'muddy': 'muddy_idle_anim_f0.png'
              }

# Items
ITEM_IMAGES = {'health1': 'flask_red.png',
               'health2': 'flask_big_red.png',
               'mace': 'weapon_mace.png',
               'katana': 'weapon_katana.png',
               'rusty_sword': 'weapon_rusty_sword.png',
               'spear': 'weapon_spear.png',
               'golden_sword': 'weapon_golden_sword.png',
               'chest': 'chest_mimic_open_anim_f0.png',
               'speed1': 'flask_blue.png',
               'speed2':'flask_big_blue.png',
               'invincible1':'flask_green.png',
               'invincible2':'flask_big_green.png',
               'power_up1':'flask_yellow.png',
               'power_up2':'flask_big_yellow.png'
               }
HEALTH_PACK_AMOUNT1 = 20
HEALTH_PACK_AMOUNT2 = 40

# Sounds #add ogg,wav 파일을 선호
BG_MUSIC = 'backgroundmusic.ogg'
PLAYER_HIT_SOUNDS = ['pain8.wav', 'pain9.wav', 'pain10.wav', 'pain11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS_GUN = {'gun': 'sfx_weapon_singleshot2.wav', 'attack': 'shout_effect.mp3'}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav'}