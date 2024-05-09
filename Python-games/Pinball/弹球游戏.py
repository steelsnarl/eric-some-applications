# 完整代码
# 导入模块
from tkinter import *

# 制作窗口
win = Tk()
cv = Canvas(win,width=640,height=480)
cv.pack()

# 初始化游戏
ball_weizhi_x = 300
ball_weizhi_y = 150
ball_yidong_x = 30
ball_yidong_y = -30
ball_size = 10

# 绘制画面
def draw_screen():
    # 清空画面
    cv.delete('all')
    # 制作画布 (画面)
    cv.create_rectangle(0,0,640,480,fill='white',width=0)

def draw_ball():
    # 绘制小球
    cv.create_oval(ball_weizhi_x - ball_size,ball_weizhi_y - ball_size,
                   ball_weizhi_x + ball_size,ball_weizhi_y + ball_size,fill='red')
# 移动小球
def move_ball():
    global ball_weizhi_x,ball_weizhi_y,ball_yidong_x,ball_yidong_y

    # 判断是否撞到左右的墙壁
    if ball_weizhi_x + ball_yidong_x < 0 or ball_weizhi_x + ball_yidong_x > 640:
        ball_yidong_x *= -1
    
