#PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()



'''
1.for i in range(4):
    这个结构一般都是python中for循环的写法；
    range(N)表示生成0,1,2。。。，N-1的列表
    range(M,N)表示的是生成M,M+1,...N-1的列表

2.import turtle是导入该模块
  from turtle import *是导入了该模块的函数，后续就不用模块名.函数名这样调用了
  import turtle as t 是给turtle取了个别名，便于书写调用
'''

