import pygame
from pygame.locals import *
import sys
import time
import math
screensize=[640,480]
screen = pygame.display.set_mode((screensize[0], screensize[1]))                # 大きさ600*500の画面を生成
pygame.display.set_caption("疑似3Dの勉強")
#color:[r,g,b]
cd=0
cm=1
ct=0#0-2
def draw_f(pos):
    global ct
    global cm
    global cd
    if ct==0:
        pygame.draw.polygon(screen, (cd,255-cd,255),[pos[0],pos[1],pos[2]], 0)
    if ct==1:
        pygame.draw.polygon(screen, (255,cd,255-cd),[pos[0],pos[1],pos[2]], 0)
    if ct==2:
        pygame.draw.polygon(screen, (255-cd,255,cd),[pos[0],pos[1],pos[2]], 0)
    cd+=1
    if cd==256:
        cd=0
        ct+=1
        if ct==3:
            ct=0
def draw(pos,c):
    pygame.draw.polygon(screen, [255, 255, 0],[pos[0],pos[1],pos[2]], 1)
    
def ft(A,x,y,z):
    output=[]
    for i in A:
        print(i)
        output.append([i[0]+x,i[1]+y,i[2]+z])
    return output

def fs(A,x,y,z):
    output=[]
    for i in A:
        output.append([i[0]*x,i[1]*y,i[2]*z])
    return output
    
def l_max(A):
    output=sorted(A,key=lambda x:x[2])
    return output

def fp(A):
    #output=l_max(A)
    output=A
    output2=[]
    for a in output:
        output2.append([a[0]/a[2], a[1]/a[2]])
    return output2
    
def fc(A,w,h):
    output=[]
    for a in A:
        output.append([w*a[0]/2+w/2, h*a[1]/2+h/2])
    return output

def fr_y(A,r):#Y回転
    output=[]
    for a in A:
        output.append([a[0]*math.cos(r) + a[2]*math.sin(r),a[1],-a[0]*math.sin(r) + a[2]*math.cos(r)])
    return output

def fr_z(A,r):#Z回転
    output=[]
    for a in A:
        output.append([a[0]*math.cos(r) + a[1]*math.sin(r),-a[0]*math.sin(r) + a[1]*math.cos(r),a[2]])
    return output
def center(A):
    return [(A[0][0] + A[1][0] + A[2][0]) / 3,(A[0][1] + A[1][1] + A[2][1]) / 3]


pos_d=[[0, 0, 0],[1, 0, 0],[0, 0, 1],[0, -1, 0]]#x,y,z,c
face=[[0, 2, 1,0],[0, 1, 3,1],[1, 2, 3,2],[0, 3, 2,3]]
face_c=[[255, 255, 0],[255, 0, 0],[255, 0, 255],[255, 255, 255]]
start_time=0
ob_pos=[screensize[0]/2,0,screensize[1]/2]
ob_ang=[0,0]
while True:
    pos_s=pos_d
    time.sleep(0.01)
    start_time+=0.01
    screen.fill((0,0,0)) 
    pygame.event.pump() #おまじない
    pressed = pygame.key.get_pressed()
    
    if pressed[K_UP]:
        ob_ang[1]-=0.1
    if pressed[K_DOWN]:
        ob_ang[1]+=0.1
    if pressed[K_RIGHT]:
        ob_ang[0]-=0.1
    if pressed[K_LEFT]:
        ob_ang[0]+=0.1
    if pressed[K_w]:
        ob_pos[2]-=5
    if pressed[K_s]:
        ob_pos[2]+=5
    if pressed[K_a]:
        ob_pos[0]-=5
    if pressed[K_d]:
        ob_pos[0]+=5
    if pressed[K_LSHIFT]:
        ob_pos[1]+=0.1
    if pressed[K_SPACE]:
        ob_pos[1]-=0.1
    pos_s = fr_z(pos_s, ob_ang[1])
    pos_s = fr_y(pos_s, ob_ang[0])
    pos_s = ft(pos_s, ob_pos[0]/120-3, ob_pos[1], -ob_pos[2]/240+4)
    C = pos_s
    pos_s = fp(pos_s);
    pos_s = fc(pos_s, screensize[0], screensize[1])
  
    C = fs(C, 1, 0, 1)
    C = ft(C, 0, 1.5, 0)
    C = fp(C)
    C = fc(C, screensize[0], screensize[1])
    
    for i in range(len(face)):
        print(face_c[face[i][3]])
        draw([pos_s[face[i][0]],pos_s[face[i][1]],pos_s[face[i][2]]],face_c[i])
        draw_f([C[face[i][0]],C[face[i][1]],C[face[i][2]]])

    pygame.display.update()

        # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:                              # 閉じるボタンが押されたら終了
            pygame.quit()                                   # Pygameの終了(画面閉じられる)
            sys.exit()
