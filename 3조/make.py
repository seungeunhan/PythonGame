import turtle as t
import math as m

xy=[]

def makePan():
    global xy
    # 창 설정
    t.ht()
    t.speed(0)
    t.setup(1100,700)
    t.title("윷놀이 게임")


    # 윷놀이 만들기 시작

    t.penup()
    t.goto(200,-200)
    t.setheading(90) 
    t.pendown()

    ## 윷 판 만들기

    for i in range(4):
        t.forward(400)
        t.left(90)
        
    t.left(45)  ## 제 4 사분면 -> 제 2 사분면으로 이동하는 대각선
    t.goto(-200,200)

    t.penup()   ## 제 3 사분면 -> 제 1 사분면으로 이동하는 대각선
    t.goto(-200,-200)
    t.pendown()
    t.right(90)
    t.goto(200,200)


    ## 모서리 원 만들기
    t.setheading(0) ## start 반지름만큼 이동
    t.penup()
    t.forward(30)
    t.pendown()

    t.setheading(90)   ## 제 1 사분면
    t.begin_fill()
    t.circle(30)
    t.fillcolor('violet')
    t.end_fill()

    t.penup()
    t.goto(-170,200)  ## 제 2 사분면
    t.pendown()

    t.setheading(90)
    t.begin_fill()
    t.circle(30)
    t.fillcolor('violet')
    t.end_fill()

    t.penup()
    t.goto(-170,-200)  ## 제 3 사분면
    t.pendown()

    t.setheading(90)
    t.begin_fill()
    t.circle(30)
    t.fillcolor('violet')
    t.end_fill()

    t.penup()
    t.goto(230,-200)   ## 제 4 사분면
    t.pendown()

    t.setheading(90)
    t.begin_fill()
    t.circle(30)
    t.fillcolor('blue')
    t.end_fill()

    t.penup()
    t.goto(-30,0)  ## 0.0 (중앙)
    t.pendown()

    t.setheading(270)
    t.begin_fill()
    t.circle(30)
    t.fillcolor('violet')
    t.end_fill()


    # 중간 원 만들기

    t.penup()       # 제 1 사분면으로 이동
    t.goto(230,200)
    t.pendown()
    t.setheading(90)

    for k in range(5):
        t.circle(30)
        t.left(90)
        t.penup()
        t.forward(80)
        t.pendown()
        t.right(90)

    t.penup()       # 제 2 사분면으로 이동
    t.goto(-170,200)
    t.pendown()
    t.setheading(90)

    for k in range(5):
        t.circle(30)
        t.left(180)
        t.penup()
        t.forward(80)
        t.pendown()
        t.right(180)

    t.penup()       # 제 3 사분면으로 이동
    t.goto(-170,-200)
    t.pendown()
    t.setheading(90)

    for k in range(5):
        t.circle(30)
        t.right(90)
        t.penup()
        t.forward(80)
        t.pendown()
        t.left(90)

    t.penup()       # 제 4 사분면으로 이동
    t.goto(230,-200)
    t.pendown()
    t.setheading(90)


    for k in range(5):
        t.circle(30)
        t.penup()
        t.forward(80)
        t.pendown()


    # 대각선 원 만들기

    t.penup()           ## 제 1 사분면 -> 제 3 사분면
    t.goto(180,220)
    t.pendown()
    t.setheading(0)
    t.right(135)
    t.penup()
    t.pendown()

    for i in range(6):
        t.circle(30)
        t.penup()
        t.forward(m.sqrt(320000)/6)
        xy.append(t.pos())
        t.pendown()

    t.penup()           ## 제 2 사분면 -> 제 4 사분면
    t.goto(-220,180)
    t.pendown()
    t.setheading(0)
    t.right(45)
    t.penup()
    t.pendown()

    for i in range(6):
        t.circle(30)
        t.penup()
        t.forward(m.sqrt(320000)/6)
        xy.append(t.position())
        t.pendown()

    return xy
