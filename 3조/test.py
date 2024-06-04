import random as r
import turtle as t
import math as m
import Sound
import cv2 as cv

from make import makePan

def catch():
    result=int(t.textinput("누가이김?","상대방이 이겼으면 1 당신이 이겼으면 0"))
    return result

# 윷
def Dice():
    s0="./image/backk.gif"
    s1="./image/pig.gif"
    s2="./image/dog.gif"
    s3="./image/lem.gif"
    s4="./image/cow.gif"
    s5="./image/horse.gif"

    dice=r.randrange(0,6,1)
    
    if dice == 0:
            s.shape(s0)
    elif dice == 1:
            s.shape(s1)
    elif dice == 2:
            s.shape(s2)
    elif dice == 3:
            s.shape(s3)
    elif dice == 4:
            s.shape(s4)
    elif dice == 5:
            s.shape(s5)
    return dice


# 플레이어 이동
def gogo1(x,y):        #플레이어 1
    global step_total1
    global tot1
    s.st()
    while True:
        dice=Dice()
        Sound.sound()
        
        step=dice * 80
        step_total1+=step
        tot1+=dice

        if dice == 0 : # 백도
            if step_total1==0 and p1.position() != t.position() :
                p1.right(90)
                p1.forward(-80)
                step_total1=320
                tot1-=1
                break;
            elif p1.position() == t.position():
                break;
            else :
                p1.forward(-80)
                step_total1-=80
                tot1-=1
                break
        

        if step_total1 > 400 or tot1==5 or tot1==10 or tot1==15:
            p1.forward(step - (step_total1 % 400))
            p1.left(90)
            p1.forward(step_total1 % 400)
            step_total1%=400

        elif tot1 == 5 or tot1 == 10:  # 대각선 위치
            angle = m.atan2(y - p1.ycor(), x - p1.xcor()) * 180 / m.pi
            p1.setheading(angle)
            p1.forward(step)

        else:
            p1.forward(step)
        
        if tot1 >= 20:
            p1.ht()
            win = cv.imread("family.jpg")
            cv.putText(win,"Winner is player 1",(200,200),fontFace=0,fontScale=3,color=(0,0,0),thickness=3)
            cv.imshow("winner",win)

        print ("p1 현재위치 : %d    p1 step = %d"%(tot1,step_total1))
        if player!=1:
             if(tot1==tot2 or tot1==tot3 or tot1==tot4):
                  result=catch()
                  if(result==1):
                       p1.goto(t.position())
                       p1.setheading(90)
                       tot1=0
                       step_total1=0

        break


def gogo2(x,y):        #플레이어2
    global step_total2
    global tot2
    s.st()
    while True:
        dice=Dice()
        Sound.sound()
        step=dice * 80
        
        step_total2+=step
        tot2+=dice

        if dice == 0 : # 백도
            if step_total2==0 and p2.position() != t2.position() :
                p2.right(90)
                p2.forward(-80)
                step_total2=320
                tot2-=1
                break;
            elif p2.position() == t2.position():
                break;
            else :
                p2.forward(-80)
                step_total2-=80
                tot2-=1
                break
        

        if step_total2 > 400 or tot2==5 or tot2==10 or tot2==15:
            p2.forward(step - (step_total2 % 400))
            p2.left(90)
            p2.forward(step_total2 % 400)
            step_total2%=400
        else:
            p2.forward(step)
        
        if tot2 >= 20:
            p2.ht()
            win = cv.imread("family.jpg")
            cv.putText(win,"Winner is player 2",(200,200),fontFace=0,fontScale=3,color=(0,0,0),thickness=3)
            cv.imshow("winner",win)

        print ("p2 현재위치 : %d    p2 step = %d"%(tot2,step_total2))

        if(tot1==tot2 or tot2==tot3 or tot2==tot4):
            result=catch()
            if(result==1):
                p2.goto(t2.position())
                p2.setheading(90)
                tot2=0
                step_total2=0
        break
        

def gogo3(x,y):        #플레이어3
    global step_total3
    global tot3
    s.st()
    while True:
        dice=Dice()
        Sound.sound()
        step=dice * 80
        
        step_total3+=step
        tot3+=dice

        if dice == 0 : # 백도
            if step_total3==0 and p3.position() != t3.position() :
                p3.right(90)
                p3.forward(-80)
                step_total3=320
                tot3-=1
                break;
            elif p3.position() == t3.position():
                break;
            else :
                p3.forward(-80)
                step_total3-=80
                tot3-=1
                break
            
        if step_total3 > 400 or tot3==5 or tot3==10 or tot3==15:
            p3.forward(step - (step_total3 % 400))
            p3.left(90)
            p3.forward(step_total3 % 400)
            step_total3%=400
        else:
            p3.forward(step)
        
        if tot3 >= 20:
            p3.ht()
            win = cv.imread("family.jpg")
            cv.putText(win,"Winner is player 3",(200,200),fontFace=0,fontScale=3,color=(0,0,0),thickness=3)
            cv.imshow("winner",win)

        print ("p3 현재위치 : %d    p3 step = %d"%(tot3,step_total3))

        if(tot2==tot3 or tot1==tot3 or tot3==tot4):
            result=catch()
            if(result==1):
                p3.goto(t3.position())
                p3.setheading(90)
                tot3=0
                step_total3=0
        break
        
        
def gogo4(x,y):        #플레이어4
   global step_total4
   global tot4
   s.st()
   while True:
        dice=Dice()
        Sound.sound()
        step=dice * 80
        
        step_total4+=step
        tot4+=dice

        if dice == 0 : # 백도
            if step_total4==0 and p4.position() != t4.position() :
                p4.right(90)
                p4.forward(-80)
                step_total4=320
                tot4-=1
                break;
            elif p4.position() == t4.position():
                break;
            else :
                p4.forward(-80)
                step_total4-=80
                tot4-=1
                break

        if step_total4 > 400 or tot4==5 or tot4==10 or tot4==15:
            p4.forward(step - (step_total4 % 400))
            p4.left(90)
            p4.forward(step_total4 % 400)
            step_total4%=400
        else:
            p4.forward(step)
        
        if tot4 >= 20:
            p4.ht()
            win = cv.imread("family.jpg")
            cv.putText(win,"Winner is player 4",(200,200),fontFace=0,fontScale=3,color=(0,0,0),thickness=3)
            cv.imshow("winner",win)

        print ("p4 현재위치 : %d    p4 step = %d"%(tot4,step_total4))
        if(tot4==tot2 or tot1==tot4 or tot3==tot4):
            result=catch()
            if(result==1):
                p4.goto(t4.position())
                p4.setheading(90)
                tot4=0
                step_total4=0
        break


def godiagonal(x, y):
    pass

# 윷 판 만들기
Sound.BGM()
point_lst = makePan()
print(point_lst)

# 플레이어 수 만들기

player=0

player=int(t.textinput("","플레이어 수를 입력해주세요"))
t.penup()
t.goto(200,-200)

if player == 1:          #1명
    p1=t.Turtle()
    
    p1.shape('turtle')
    p1.color('pink')
    
    p1.penup()
    
    p1.setheading(90)
    
    p1.goto(200,-200)
    
    p1.onclick(gogo1,1,True)

elif player == 2:       #2명
    p1=t.Turtle()
    p2=t.Turtle()
    t2=t.Turtle()
    t2.ht()
    
    p1.shape('turtle')
    p1.color('pink')
    
    p2.shape('turtle')
    p2.color('yellow')
    
    p1.penup()
    p2.penup()
    t2.penup()
    
    p1.setheading(90)
    p2.setheading(90)
    
    p1.goto(200,-200)
    p2.goto(220,-200)
    t2.goto(220,-200)
    
    p1.onclick(gogo1,1,True)
    p2.onclick(gogo2,1,True)

elif player == 3:      # 3명
    p1=t.Turtle()
    p2=t.Turtle()
    p3=t.Turtle()
    t2=t.Turtle()
    t3=t.Turtle()
    t2.ht()
    t3.ht()
    
    p1.shape('turtle')
    p1.color('pink')
    
    p2.shape('turtle')
    p2.color('yellow')
    
    p3.shape('turtle')
    p3.color('lightblue')
    
    p1.penup()
    p2.penup()
    p3.penup()
    t2.penup()
    t3.penup()
    
    p1.setheading(90)
    p2.setheading(90)
    p3.setheading(90)
    
    p1.goto(200,-200)
    p2.goto(220,-200)
    t2.goto(220,-220)
    p3.goto(200,-220)
    t3.goto(200,-220)
    
    p1.onclick(gogo1,1,True)
    p2.onclick(gogo2,1,True)
    p3.onclick(gogo3,1,True)
    
elif player == 4:       # 4명
    p1=t.Turtle()
    p2=t.Turtle()
    p3=t.Turtle()
    p4=t.Turtle()
    t2=t.Turtle()
    t3=t.Turtle()
    t4=t.Turtle()
    t2.ht()
    t3.ht()
    t4.ht()
    
    p1.shape('turtle')
    p1.color('pink')
    
    p2.shape('turtle')
    p2.color('yellow')
    
    p3.shape('turtle')
    p3.color('lightblue')
    
    p4.shape('turtle')
    p4.color('green')
    
    p1.penup()
    p2.penup()
    p3.penup()
    p4.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    
    p1.setheading(90)
    p2.setheading(90)
    p3.setheading(90)
    p4.setheading(90)
    
    p1.goto(200,-200)
    p2.goto(220,-200)
    t2.goto(220,-200)
    p3.goto(200,-220)
    t3.goto(200,-220)
    p4.goto(220,-220)
    t4.goto(220,-220)
    
    p1.onclick(gogo1,1,True)
    p2.onclick(gogo2,1,True)
    p3.onclick(gogo3,1,True)
    p4.onclick(gogo4,1,True)

else:
    t.penup()
    t.goto(0,250)
    t.pendown()
    t.write("최대 4명까지 가능합니다. 다시 실행시켜주세요.","휴면옛체",20,move=True)
    t.penup()
    
step_total1=0
step_total2=0
step_total3=0
step_total4=0

tot1=0
tot2=0
tot3=0
tot4=0


## 윷 구현

s=t.Turtle()
s.penup()
s.goto(-400,0)

s.ht()

s0="./image/backk.gif"
s1="./image/pig.gif"
s2="./image/dog.gif"
s3="./image/lem.gif"
s4="./image/cow.gif"
s5="./image/horse.gif"


for i in range(0,6):
    t.addshape(globals()['s'+str(i)])


t.mainloop()

