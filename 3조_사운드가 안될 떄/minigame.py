import turtle as t
import winsound
import time
import random


def minigame():

    #기본설정
    t.bgcolor('#F6DB90')
    scr = t.Screen()
    scr.setup(1000, 1000)
    scr.bgpic("lyard.gif")
    scr.update()
    t.up()
    t.speed(0)
    t.goto(0,220)
    t.write("거북이 레이스", False, "center", ('맑은 고딕',40))


    #레이스 경기장
    t.goto(-400,140)
    t.down()
    t.color("#C0A55A")
    t.begin_fill()
    for i in range(2):
        t.forward(800)
        t.right(90)
        t.forward(400)
        t.right(90)
    t.end_fill()


    #터틀 선수 생성
    start_ycor=[10,-140]
    color_list = ["#191970","#FF00FF"]
    turtles=[]


    for i in range(2) :
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.shape("turtle")
        new_turtle.color(color_list[i])
        new_turtle.goto(-390, start_ycor[i])
        new_turtle.write(f"{i+1}번")
        new_turtle.goto(-350, start_ycor[i]) #출발선
        turtles.append(new_turtle)


    #레이스 라인 생성
    t.up()
    t.goto(-400,start_ycor[i] +80)
    t.color("white")
    t.pensize(3)
    t.down()
    t.goto(400,start_ycor[i] +80)


    #결승선 그리기
    t.color("black")
    t.pensize(5)
    t.up()
    t.goto(330,170)
    t.down()
    t.goto(330,-290)


    # 배팅하기
    #user1_name = t.textinput("거북이 레이스", "user1님의 이름 입력 : ")
    #user2_name = t.textinput("거북이 레이스", "user2님의 이름 입력 : ")

    user1_choice = int(t.textinput("거북이 레이스", "상대방이 선택한 우승 거북이 번호는?"))
    user2_choice = int(t.textinput("거북이 레이스", "본인이 선택한 우승 거북이 번호는?"))
    t.up()
    t.goto(0,-320)
    t.color("black")
    t.write(f"상대방 : {user1_choice}번 터틀, 본인 : {user2_choice}번 터틀 배팅 완료", False, "center", ("맑은 고딕",18))
    t.ht()


    #경기 시작 알림
    winsound.Beep(523,300)
    time.sleep(0.5)


    #경기 시작
    game_over = False
    while not game_over :
        for i in turtles:
            rand_speed = random.randint(1,10)
            i.forward(rand_speed)
            if i.xcor() > 330:
                game_over = True

    # 1등 찾기
    max_xcor = 0
    winner = 0
    for i in range(len(turtles)):
        if turtles[i].xcor() > max_xcor:
            max_xcor=turtles[i].xcor()
            winner = i+1

    #배팅 결과
    t.goto(0,-380)
    if user1_choice == winner:
        t.write(f"상대방님이 선택한 {user1_choice}번 거북이가 우승하였습니다!",False,"center", ("맑은 고딕",25))
        return 1
    else :
        t.write(f"본인님이 배팅한 {user2_choice}번 거북이가 우승하였습니다!",False,"center", ("맑은 고딕",25))
        return 0

    #비주얼 스튜디오 코드에서 터틀이 닫히지 않게 하는 용도
    #t.exitonclick()
    

minigame()
