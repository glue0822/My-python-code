from tkinter import *
from time import sleep,time
from random import randint
from math import sqrt
from PIL import ImageTk,Image
feeling_brave=True
#导入模块
ship_speed=5
score=0
window=Tk()
window.title('Bubble Blaster')
window.attributes('-topmost',1)
sea=Canvas(window,width=800,height=500,bg='darkblue')
sea.pack()
#设置窗口
img=Image.open('ship.jpg')
img=img.resize((40,20))
photo=ImageTk.PhotoImage(img)
ship_1=sea.create_image(15,15,image=photo)
sea.coords(ship_1,15,15)
ship_2=sea.create_oval(0,0,30,30,outline='red',state=HIDDEN)
sea.create_polygon(180,500,300,500,300,440,fill='blue',outline='blue')
sea.create_polygon(500,500,620,500,500,440,fill='blue',outline='blue')
sea.create_rectangle(300,500,500,440,fill='blue',outline='blue')
speed_out=sea.create_rectangle(310,480,490,460,outline='green')
speed_1=sea.create_rectangle(310,480,355,460,fill='green',outline='green')
speed_2=sea.create_rectangle(354,480,355,440,fill='green',outline='green')
speed_3=sea.create_text(400,470,text='x100px/s',fill='white')
sea.create_text(310,490,text='0',fill='white')
for n in range(1,4):
    sea.create_text(310+(n*45),490,text=str(n),fill='green')
sea.create_text(490,490,text='4',fill='red')
sea.move(ship_1,400,250)
sea.move(ship_2,400,250)
#创建主体
def move_ship_up(self):
    place=sea.coords(ship_2)
    corner=place[1]
    if corner > 0 and feeling_brave:
        sea.move(ship_1,0,-(ship_speed/2))
        sea.move(ship_2,0,-(ship_speed/2))
    window.update()
sea.bind_all('<KeyPress-w>',move_ship_up)
def move_ship_down(self):
    place=sea.coords(ship_2)
    corner=place[1]
    if corner < 470 and  feeling_brave:
        sea.move(ship_1,0,ship_speed/2)
        sea.move(ship_2,0,ship_speed/2)
    window.update()
sea.bind_all('<KeyPress-s>',move_ship_down)
def move_ship_left(self):
    place=sea.coords(ship_2)
    corner=place[0]
    if corner > 0 and  feeling_brave:
        sea.move(ship_1,-ship_speed,0)
        sea.move(ship_2,-ship_speed,0)
    window.update()
sea.bind_all('<KeyPress-a>',move_ship_left)
def move_ship_right(self):
    place=sea.coords(ship_2)
    corner=place[0]
    if corner < 770 and feeling_brave:
        sea.move(ship_1,ship_speed,0)
        sea.move(ship_2,ship_speed,0)
    window.update()
sea.bind_all('<KeyPress-d>',move_ship_right)
def speed_add_minus(event):
    global ship_speed
    if ship_speed < 20  and feeling_brave and event.delta > 0:
        ship_speed+=1
        sea.move(speed_2,9,0)
    elif ship_speed > 0 > event.delta and feeling_brave:
        ship_speed-=1
        sea.move(speed_2,-9,0)
sea.bind_all('<MouseWheel>',speed_add_minus)
#移动主体
bub_id=list()
bub_r=list()
bub_speed=list()
def create_bub():
    r=randint(10,30)
    y=randint(0,500)
    id1=sea.create_oval(r,y-r,-r,y+r,outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1,10))
def move_bub():
    for serial_number in range(len(bub_id)):
        sea.move(bub_id[serial_number],bub_speed[serial_number],0)
        sea.tag_raise(bub_id[serial_number])
def get_coords(id_num):
    pos=sea.coords(id_num)
    x=(pos[0]+pos[2])/2
    y=(pos[1]+pos[3])/2
    return x,y
def del_bub(number):
    del bub_r[number]
    del bub_speed[number]
    sea.delete(bub_id[number])
    del bub_id[number]
def clean_up_bubs():
    for number in range(len(bub_id)-1,-1,-1):
        x,y=get_coords(bub_id[number])
        if x < -100:
            del_bub(number)
def distance(id1,id2):
    x1,y1=get_coords(id1)
    x2,y2=get_coords(id2)
    return sqrt ((x1-x2)**2+(y1-y2)**2)
def collision():
    points=0
    for bub_num in range(len(bub_id)-1,-1,-1):
        if distance(ship_2,bub_id[bub_num]) < (15+bub_r[bub_num]):
            points+=(bub_r[bub_num]+bub_speed[bub_num])
            del_bub(bub_num)
    return points
#泡泡创建等功能
sea.create_text(50,30,text='TIME',fill='white')
sea.create_text(150,30,text='SCORE',fill='white')
time_text=sea.create_text(50,50,fill='white')
score_text=sea.create_text(150,50,fill='white')
speed_text=sea.create_text(400,450,fill='white')
def show_score(score_int):
    sea.itemconfig(score_text,text=str(score_int))
def show_time(time_left):
    sea.itemconfig(time_text,text=str(time_left))
def show_speed(speed):
    sea.itemconfig(speed_text,text='SPEED:'+str(speed))
#时间和分数显示
bonus=0
end=time()+60
raise_list=[speed_text,speed_out,speed_1,speed_2,speed_3,ship_1,ship_2]
#置顶列表，越往后图层越靠上
color_list=[speed_1,speed_2]
def raise_things():
    global raise_list
    for i in raise_list:
        sea.tag_raise(i)
def color_things(do):
    global color_list
    for x in color_list:
        sea.itemconfig(x,fill=do,outline=do)
    sea.itemconfig(speed_out,outline=do)
while time() <end:
    try:
        if randint(1,10) == 1:
            create_bub()
        if ship_speed > 18:
            color_things('red')
        elif ship_speed < 2:
            color_things('white')
        else:
            color_things('green')
        sea.coords(speed_1,310,480,310+ship_speed*9,460)
        raise_things()
        move_bub()
        clean_up_bubs()
        score+=collision()
        if (int(score/1000)) > bonus:
            bonus+=1
            end+=10
        show_score(score)
        show_time(int(end-time()))
        show_speed(ship_speed*20)
        window.update()
    except TclError:
        raise SystemExit(0)    #这行代码会导致Windows Defender将此文件打包后的exe识别成病毒(T_T),但不加会报错
    finally:
        sleep(0.01)
#主循环
sea.create_text(400,250,text='GAME OVER',fill='white',font=('Helvetica',30))
sea.create_text(400,280,text='Bonus time:'+str(bonus*10)+'s',fill='white')
sea.create_text(400,295,text='Score:'+str(score),fill='white')
def close_window():
    window.destroy()
window.protocol('WM_DELETE_WINDOW',close_window)
quit_button=Button(window,text='Close',command=close_window,width=120)
quit_button.pack()
feeling_brave=False
window.mainloop()
#结束后的等待关闭
