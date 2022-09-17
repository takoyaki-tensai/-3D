# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import time
#壁と視点の線の交点の座標を算出
def calc_cross_point(pointA, pointB, pointC, pointD):
    cross_points = (0,0)
    bunbo = (pointB[0] - pointA[0]) * (pointD[1] - pointC[1]) - (pointB[1] - pointA[1]) * (pointD[0] - pointC[0])

    # 直線が平行な場合
    if (bunbo == 0):
        return False, cross_points

    vectorAC = ((pointC[0] - pointA[0]), (pointC[1] - pointA[1]))
    r = ((pointD[1] - pointC[1]) * vectorAC[0] - (pointD[0] - pointC[0]) * vectorAC[1]) / bunbo
    s = ((pointB[1] - pointA[1]) * vectorAC[0] - (pointB[0] - pointA[0]) * vectorAC[1]) / bunbo

    # 線分AB、線分AC上に存在しない場合
    if (r <= 0) or (1 <= r) or (s <= 0) or (1 <= s):
        return False, cross_points

    # rを使った計算の場合
    distance = ((pointB[0] - pointA[0]) * r, (pointB[1] - pointA[1]) * r)
    cross_points = (int(pointA[0] + distance[0]), int(pointA[1] + distance[1]))

    # sを使った計算の場合
    # distance = ((pointD[0] - pointC[0]) * s, (pointD[1] - pointC[1]) * s)
    # cross_points = (int(pointC[0] + distance[0]), int(pointC[1] + distance[1]))

    return True, cross_points
#壁と視点の線の交点とプレーヤーの距離を算出
def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

#メイン
def main():
    pygame.init()                                               # Pygameの初期化
    screensize=[640,480]
    screen = pygame.display.set_mode((screensize[0], screensize[1]))                # 大きさ600*500の画面を生成
    pygame.display.set_caption("疑似3Dの勉強")
    pos=[0.0,0.0]
    angle=0
    #視点線の本数増やせば細かくなるが重くなる
    seido=32
    mode=0# タイトルバーに表示する文字

    #Mapdata
    map1=[[0,0,0,0,0,0,0,0,0,0,0],
                  [0,1,1,1,1,0,0,0,0,1,0],
                  [0,0,1,0,0,0,1,1,0,0,0],
                  [0,1,1,1,1,0,0,1,1,0,0],
                  [0,0,0,0,1,0,0,1,0,0,0],
                  [0,0,0,1,0,1,0,1,0,1,0],
                  [0,1,0,0,0,0,0,1,0,0,0],
                  [0,0,0,0,1,0,1,1,1,0,0],
                  [0,0,1,0,0,0,0,0,0,0,0],
                  [1,0,0,0,1,1,0,1,0,1,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  ]
    while (1):
        time.sleep(0.001)
        screen.fill((0,0,0)) 
        # (0,0)から(80,80)まで線幅5pxで緑色(R=0, G=95, B=0)の直線を描く
           # 直線の描画
        #[mode=0・・・2dモード][1・・・3dモード]
        if mode==0:
            for h in range(11):
                for w in range(11):
                    if map1[w][h]==1:
                        for r in range(seido):
                            if map1[w-1][h]==0:
                                pygame.draw.circle(screen, (255,0,0), (calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))[1][1]), 3)
                            if map1[w][h-1]==0:
                                pygame.draw.circle(screen, (255,0,0), (calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[1][1]), 3)
                            if map1[w+1][h]==0:
                                pygame.draw.circle(screen, (255,0,0), (calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[1][1]), 3)
                            if map1[w][h+1]==0:
                                pygame.draw.circle(screen, (255,0,0), (calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[1][1]), 3)
    
                        calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))
                        pygame.draw.line(screen, (255,255,255), (h*64,w*64), (h*64+64,w*64), 1)
                        pygame.draw.line(screen, (255,255,255), (h*64,w*64), (h*64,w*64+64), 1)
                        pygame.draw.line(screen, (255,255,255), (h*64+64,w*64), (h*64+64,w*64+64), 1)
                        pygame.draw.line(screen, (255,255,255), (h*64,w*64+64), (h*64+64,w*64+64), 1)
            for r in range(seido):
                pygame.draw.line(screen, (255,255,255), (pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), 1)
        if mode==1:
            #hit・・・壁と自分の距離をすべてリストとして格納　-1.0=壁に触れていない 1.3=壁と自分に1.3の距離がある
            hit=[]
            for r in range(seido):
                hit.append(-1.0)
            for h in range(11):
                for w in range(11):
                    if map1[w][h]==1:
                        for r in range(seido):
                            
                            if map1[w-1][h]==0 and calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))[0]:
                                if hit[r]==-1.0 or hit[r]>get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64,w*64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))[1][1]):
                                    hit[r] = get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64+64,w*64))[1][1])
                            if map1[w][h-1]==0 and calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[0]:
                                if hit[r]==-1.0 or hit[r]>get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[1][1]):
                                    hit[r]=get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64), (h*64,w*64+64))[1][1])
                            if map1[w][h+1]==0 and calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[0]:
                                if hit[r]==-1.0 or hit[r]>get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[1][1]):
                                    hit[r]=get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64+64,w*64), (h*64+64,w*64+64))[1][1])
                            if map1[w+1][h]==0 and calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[0]:
                                if hit[r]==-1.0 or hit[r]>get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[1][1]):
                                    hit[r]=get_distance(pos[0],pos[1],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[1][0],calc_cross_point((pos[0],pos[1]), (pos[0]+math.cos(math.radians(angle+r*(90/seido)))*150,pos[1]+math.sin(math.radians(angle+r*(90/seido)))*150), (h*64,w*64+64), (h*64+64,w*64+64))[1][1])
            #壁を絵画
            for r in range(seido-1):
                if hit[r]!=-1.0 and hit[r+1]!=-1.0:
                    pygame.draw.polygon(screen, (255/max(hit[r]/64,1),255/max(hit[r]/64,1),255/(max(hit[r]/64,1))), [(screensize[0]/seido*r,320+(20/hit[r])*300),(screensize[0]/seido*(r+1),320+(20/hit[r+1])*300),(screensize[0]/seido*(r+1),320-(20/hit[r+1])*300),(screensize[0]/seido*r,320-(20/hit[r])*300)])
            if pressed_key[K_p]:
                print(hit)
        pygame.display.update()                                 # 画面を更新
        #Key操作
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            angle-=2
        if pressed_key[K_RIGHT]:
            angle+=2
        if pressed_key[K_UP]:
            pos[0]+=math.cos(math.radians(angle+45))*1.0
            pos[1]+=math.sin(math.radians(angle+45))*1.0
        if pressed_key[K_DOWN]:
            pos[0]-=math.cos(math.radians(angle+45))*1.0
            pos[1]-=math.sin(math.radians(angle+45))*1.0
        # イベント処理
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_e:
                    if mode==0:
                        mode=1
                    elif mode==1:
                        mode=0
            if event.type == QUIT:                              # 閉じるボタンが押されたら終了
                pygame.quit()                                   # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()
