## 递归地绘制茂密的分形树 金黄色系随机颜色树叶和落叶

import turtle
import random

rate= 0.8  #树枝递归时减小的比例
leaf_length_low=10  #最短的叶子长度下界
leaf_length_high=50 #最长的叶子长度上界  再长就是褐色的主干
def draw_brach(brach_length,ratating=0):
    #产生随机颜色的list 可以补充其他颜色 这里想绘制秋天的叶子，所以为黄色和金色
    color=['yellow','yellow2','yellow3','yellow4','gold','gold2','gold3','gold4']
    temp_color=color[int(random.random()*7)]
    if brach_length > leaf_length_low:
        if brach_length < leaf_length_high:
            turtle.color(temp_color)
        else:
            turtle.color('brown')
        # 递归地画右侧的树枝
        #向前一段长度
        turtle.forward(brach_length)
        #右转度数
        turtle.right(25)
        #递归地绘制
        draw_brach(brach_length*rate)
        # 递归地画左侧的树枝
        #左转度数
        turtle.left(50)
        #递归地绘制
        draw_brach(brach_length*rate)
        if brach_length < leaf_length_high:
            turtle.color(temp_color)
        else:
            turtle.color('brown')
        # 返回之前的树枝上
        #右转度数
        turtle.right(25)
        #向后一段长度
        turtle.backward(brach_length)
def draw_leaf(x,y):
    # 抬起画笔 避免移动时划线
    turtle.up()
    turtle.goto(x,y)
    # 按下画笔 继续绘制
    turtle.down()
    #绘制落叶 所以随机旋转一下画笔的角度更真实
    turtle.right(random.randrange(-90,90,1))
    #调用一下画树的函数 传入一个正好够画一个树杈的长度
    draw_brach(leaf_length_low/0.8+1)
if __name__ == '__main__':
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.speed(100000000000000)
    draw_brach(100)
    for i in range(100):
        draw_leaf(random.randrange(-250,250,1),random.randrange(-180,-50,1))
    turtle.exitonclick()