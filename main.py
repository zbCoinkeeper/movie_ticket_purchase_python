import turtle
from tkinter import *
import tkinter.messagebox
import csv
import turtle


#全局数据
frame=[]
canvas=[]
seatList=[]
root = Tk()

#定义座位类,0代表没有人选择，1代表当前选中，2代表已经被人选走了
class Seat():
    def __init__(self,canvas,state,id):
        self.id=id
        self.canvas=canvas
        self.state=state
        self.draw()
        self.canvas.bind("<Button-1>", self.toggle())
    
    def draw(self):
        color=""
        if self.state=="0":
            color = "white";
        elif self.state=="1":
            color = "#9bb67b";
        else:
            color = "red";
        self.canvas.create_rectangle(10,10,20,20,fill=color)
        

    def toggle(self):
        def func(e):
            if self.state=="0":
                self.state="1"
                #重新绘制座位
                self.draw()
                #更新seatList数据
                seatList[0][self.id]="1"
            elif self.state=="1":
                self.state="0"
                self.draw()
                seatList[0][self.id]="0"
            else:
                return
        return func


def initReadCSV(seatList):
    with open('seat.csv', 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            seatList.append(row)



def updateSeatGUI():
    initReadCSV(seatList)
    # 实例化座位数量
    k=0
    for i in range(8):
        frame.append(Frame(root,bg="#ececec",height="50",width="400"))
        canvas.append([])
        for j in range(10):
            canvas[i].append(Canvas(frame[i], width=20, height=20,bg="#ececec"))
            canvas[i][j].pack(side=LEFT)
            #k为作为id，来作为座位的唯一标识
            seat=Seat(canvas[i][j],seatList[0][k],k)
            k=k+1



def buyTickets():
    result = tkinter.messagebox.askokcancel(title = '确认支付',message='确定要购买吗')
    if result:
        with open("seat.csv","w") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(seatList[0])):
                #确认购买之后，那么所有标记为1的位置应该变为2
                if seatList[0][i]=="1":
                    seatList[0][i]="2"
            writer.writerows(seatList)
        #类似于vue的数据驱动视图,先更新数据，再根据数据更新视图
        updateSeatGUI()

def drawDoor(canva_door):
    theScreen = turtle.TurtleScreen(canva_door)
    theScreen.bgcolor("#ececec")
    path = turtle.RawTurtle(theScreen)
    path.hideturtle()
    path.speed(0)
    path.up()
    path.backward(175)
    path.down()
    path.forward(20)
    path.up()
    path.forward(20)
    path.down()
    path.forward(270)
    path.up()
    path.forward(20)
    path.down()
    path.forward(20)

    path.up()
    path.right(90)
    path.forward(20)
    path.right(90)
    path.forward(200)
    path.down()

    path.right(90)
    path.right(90)

    
    for x in range(1, 6):
        path.forward(50)
        path.left(216)  #在这里先向右直行，然后左转216°(左下，正五角星度数180/5=36°)
  
    theScreen.mainloop()
 

def main():
    root.title("电影院")
    #根据数据，画出座位
    updateSeatGUI()
    for i in range(8):
        frame[i].place(x = 100, y = 21+40*i)
        frame[i].pack_propagate(False)
    #画出电影院的入口
    canva_door = Canvas(root, width=350, height=100,bg="#ececec")
    canva_door.place(x=50,y=350)
    #画出按钮
    B = Button(root, text ="购票", command = buyTickets,highlightcolor="white")
    B.pack(side=BOTTOM)
    root.geometry("500x500+500+300")
    drawDoor(canva_door)
    root.mainloop()



if __name__ == "__main__":
    main()