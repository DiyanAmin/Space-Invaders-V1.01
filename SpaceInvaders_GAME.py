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
backround=g.image.load('BG.png')
g.display.set_caption('Space Invaders V1.01')
icon=g.image.load('UFO.png')
g.display.set_icon(icon)

#Player
playerImg=g.image.load('PLAYER.png')
playerX=PlayerStart_X
playerY=PlayerStart_Y
playerX_change=0

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
bulletImg=g.image.load('Bullet.png')
bulletX=0
bulletY=PlayerStart_Y
bulletXchange=0
bulletYchange=BulletSpeed_Y
bulletState='ready'

#Score
scoreVal=0
font=g.font.Font('freesansbold.ttf',64)
textX=10
textY=10

#Important functions
overFont=g.font.Font('freesansbold.ttf',64)
def showScore(x,y):
    #Display the current score on screen
    score=font.render('Score:'+str(scoreVal),True,(255,255,255))
    Screen.blit(score,(x,y))

def GameOverText():
    #Display the game over text
    OverText=overFont.render('GAME OVER',True,(255,255,255))
    Screen.blit(OverText,(200,250))

def player(x,y):
    Screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    Screen.blit(enemyImg[i],(x,y))

def FireBullet(x,y):
    global bulletState
    bulletState='fire'
    Screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    #If bullet hit enemy --> enemy die
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance<CollisionDistance

#Game Loop
running=True
while running:
    Screen.fill((0,0,0))
    Screen.blit(backround,(0,0))
    for event in g.event.get():
        if event.type==g.QUIT:
            running=False
        if event.type==g.KEYDOWN:
            if event.key==g.K_LEFT:
                playerX_change=-5
            if event.key==g.K_RIGHT:
                playerX_change=5
            if event.key==g.K_SPACE and bulletState=='ready':
                bulletX=playerX
                FireBullet(bulletX,bulletY)
        if event.type==g.KEYUP and event.key in [g.K_LEFT,g.K_RIGHT]:
            playerX_change=0
    #Player Movement
    playerX+=playerX_change
    playerX=max(0,min(playerX,ScreenWidth-64))#64 is player size

    #Enemy Movement
    for i in range(EnemyNum):
       if enemyY[i]>340: #--> if true, game over
            for j in range(EnemyNum):
                enemyY[j]=2000
            GameOverText()
            break
       enemyX[i]+=enemyX_change[i]
       if enemyX[i]<=0 or enemyX[i]>=ScreenWidth-64:
           enemyX_change[i]*=-1
           enemyY[i]+=enemyY_change[i]
        #Collision Check
       if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
           bulletY=PlayerStart_Y
           bulletState='ready'
           scoreVal+=1
           enemyX[i]=random.randint(0,ScreenWidth-64)
           enemyY[i]=random.randint(EnemyStart_Ymin,EnemyStart_Ymax)
       enemy(enemyX[i],enemyY[i],i)
    #Bullet Movement
    if bulletY<=0:
        bulletY=PlayerStart_Y
        bulletState='ready'
    elif bulletState=='fire':
        FireBullet(bulletX,bulletY)
    player(playerX,playerY)
    showScore(textX,textY)
    g.display.update()