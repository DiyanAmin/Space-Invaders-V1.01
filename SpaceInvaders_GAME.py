import pygame as g
import math,random

#IMP Vars
ScreenWidth=800
ScreenHeight=500
PlayerStart_X=370
PlayerStart_Y=380
EnemyStart_Ymin=50
EnemyStart_Ymax=150
EnemySpeed_X=4
EnemySpeed_Y=40
BulletSpeed_Y=10
CollisionDistance=27

# Setup
g.init()
Screen=g.display.set_mode((ScreenWidth,ScreenHeight))
backround=g.image.load('Space_BG.jpeg')
g.display.set_caption('Space Invaders V1.01')
icon=g.image.load('UFO.png')
g.display.set_icon(icon)

#Player
playerImg=g.image.load('PLAYER.png')
playerX=PlayerStart_X
playerY=PlayerStart_Y

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
EnemyNum=6   #--> How many enemies

for i in range(EnemyNum):
    enemyImg.append(g.image.load('ENEMY.png'))
    enemyX.append(random.randint(0,ScreenWidth-64))
    enemyY.append(random.randint(EnemyStart_Ymin,EnemyStart_Ymax))
    enemyX_change.append(EnemySpeed_X)
    enemyY_change.append(EnemySpeed_Y)

#Bullet