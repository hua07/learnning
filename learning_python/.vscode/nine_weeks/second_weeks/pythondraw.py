#pythondraw.py
""" import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done() """

#使用turtle库绘制正方形
""" import turtle
turtle.setup(400,400,200,200)
turtle.penup()
turtle.fd(-50)
turtle.pendown()
turtle.pensize(10)
turtle.pencolor('black')
for i in range(4):
    turtle.fd(100)
    turtle.left(90)
turtle.done() """

#六边形的绘制
""" import turtle
turtle.setup(400,400,200,200)
turtle.penup()
turtle.fd(-50)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor('red')
for i in range(6):
    turtle.fd(50)
    turtle.left(60)
turtle.done()
"""

#叠边形的绘制（9条边）
""" import turtle
turtle.setup(600,400,200,200)
turtle.penup()
turtle.fd(-100)
turtle.pendown()
turtle.pensize(3)
turtle.pencolor('yellow')
for i in range(9):
    turtle.fd(100)
    turtle.left(80)
turtle.done() """
#风轮绘制方法一
""" import turtle

turtle.setup(800,600,200,200)
turtle.pensize(3)
turtle.pencolor('blue')
for i in range(4):
    turtle.left(90)
    turtle.fd(150)
    turtle.right(90)
    turtle.circle(-150,45)
    turtle.goto(0,0)
    turtle.left(135)       
turtle.done() """

#风轮绘制方法二
""" import turtle
turtle.setup(800,600,200,200)
turtle.pensize(3)
turtle.pencolor('blue')
for i in range(4):
    turtle.right(45)
    turtle.fd(150)
    turtle.left(90)
    turtle.circle(150,45)
    turtle.goto(0,0)
           
turtle.done() """

#自己绘制一条蟒蛇
""" 
import turtle
turtle.setup(800,600,200,200)
turtle.penup()
turtle.fd(-200)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor('green')
turtle.seth(30)
for i in range(4):
    turtle.circle(50,60)
    turtle.circle(-50,60)
turtle.left(30)
turtle.fd(50)
turtle.circle(30,220)
turtle.done() """

#绘制一个正方形

""" import turtle as t
t.pensize(2)
for i in range(4):
    t.fd(150)
    t.left(90)
t.done() """
#绘制六边形
""" import turtle as t
t.pensize(2)
for i in range(6):
    t.fd(150)
    t.left(60)
t.done() """

#绘制五角星
""" 
import turtle as t
t.pensize(2)
for i in range(5):
    t.left(72)
    t.fd(100)
    t.right(144)
    t.fd(100)
t.done() """

""" import turtle as t
t.pensize(2)
t.left(36)
for i in range(5):
    t.fd(200)
    t.left(144)
t.done() """

#叠边形效果

""" import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(200)
    t.left(80)
t.done() """

#风车的绘制
""" import turtle as t
t.pensize(2)
for i in range(4):
    t.right(45)
    t.fd(100)
    t.left(90)
    t.circle(100,45)
    t.goto(0,0)
t.done() """
""" 
import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0), """
# 画一个桌面
""" import turtle as t
t.pensize(2)
for i in range(2):
    t.fd(200)
    t.circle(30,90)
    t.fd(150)
    t.circle(30,90)
t.done() """

