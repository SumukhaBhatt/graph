def x_line(ca):
    a=int(scy.get())
    for i in range(78,680,38):
        ca.create_line(40,680-i,1500,680-i,width=0.1)
        ca.create_text(32,680-i,text=str(a),angle=90,fill="red")
        a=a+int(scy.get())
def y_line(ca):
    a=int(scx.get())
    for i in range(78,1500,38):
        ca.create_line(i,0,i,640,width=0.5)
        ca.create_text(i,648,text=str(a),fill="red")
        a=a+int(scx.get())
def x_co(val,xscale):
    return((val/xscale)*38+40)
def x_label(ca):
    try:
        ca.delete(ca.find_closest(700,670)[0])
    except:
        pass
    ca.create_text(700,670,text=lbx.get(),fill="green")
def y_label(ca):
    try:
        ca.delete(ca.find_closest(10,300)[0])
    except:
        pass  
    ca.create_text(10,300,text=lby.get(),angle=90,fill="green")
def y_co(val,yscale):
    return(640-(val/yscale)*38)
def xyscale():
    ca.create_polygon(1108,53,1108,107,1294,107,1294,53,fill="white",outline="black")
    ca.create_text(1200,80,text="SCALE::\n\t X axis: 1cm="+scx.get()+" units\n\tY axis: 1cm="+scy.get()+" units",fill="blue")
def x_event(x):
    return(round((x-40)*int(scx.get())/38,2))
def y_event(y):
     return(round((640-y)*int(scy.get())/38,2))
def ev(event):
    ca.create_text(event.x-20,event.y-20,text="("+str(x_event(event.x))+","+str(y_event(event.y))+")")
    ca.create_line(event.x,event.y,event.x-20,event.y-20)
def sub():
    global ob,ca
    if ca==None:
        ob=Toplevel(gr)
        ca=Canvas(ob,height=680,width=1500,bg="white")
        ca.pack()
    try:
        ca.create_line(40,0,40,680,width=2)
    except:
        ob=Toplevel(gr)
        ca=Canvas(ob,height=680,width=1500,bg="white")
        ca.pack()
        ca.create_line(40,0,40,680,width=2)
    ca.create_line(0,640,1500,640,width=2)
    y_line(ca)
    x_line(ca)
    x_label(ca)
    y_label(ca)
    xyscale()
    a=xx.get().split(":")
    if len(y.get().split(","))==1:
        points=[]
        for x in range(int(a[0]),int(a[1])+1,int(a[2])):
            ca.create_text(x_co(x,int(scx.get())),y_co(round(eval(y.get())),int(scy.get())),text="*")
            points.append(x_co(x,int(scx.get())))
            points.append(y_co(round(eval(y.get())),int(scy.get())))
        if line.get():
            ca.create_line(points,smooth=True,width=1.5)
    else:
        points=[]
        b=y.get().split(",")
        i=0;
        for x in range(int(a[0]),int(a[1]),int(a[2])):
            ca.create_text(x_co(x,int(scx.get())),y_co(int(b[i]),int(scy.get())),text="*")
            points.append((x_co(x,int(scx.get()))))
            points.append(y_co(int(b[i]),int(scy.get())))
            i+=1
        if line.get():
            ca.create_line(points,smooth=True,width=1.5)
    ca.bind("<Double-1>",ev)
from tkinter import *
from math import *
gr=Tk()
gr.title("Graph")
gr.geometry("500x500")
gr=Frame(gr)
gr.pack()
ob=ca=None
Label(gr,text="please enter the x cordinate").pack(anchor="w")
xx=Entry(gr)
xx.pack(anchor="e")
Label(gr,text="Write the expression").pack(anchor="w")
y=Entry(gr)
y.pack(anchor="e")
Label(gr,text="Number of unis for 1Cm in X co-ordinate:").pack(anchor="w")
scx=Entry(gr)
scx.pack(anchor="e")
Label(gr,text="Number of unis for 1Cm in y co-ordinate:").pack(anchor="w")
scy=Entry(gr)
scy.pack(anchor="e")
Label(gr,text="X label").pack(anchor="w")
lbx=Entry(gr)
lbx.pack(anchor="e")
Label(gr,text="Y label").pack(anchor="w")
lby=Entry(gr)
lby.pack(anchor="e")
xx.insert(0,"1:20:1")
y.insert(0,"x")
scx.insert(0,"2")
scy.insert(0,"2")
lbx.insert(0,"in cm")
lby.insert(0,"in cm")
Label(gr,text="Do you want to draw the line").pack(anchor="w")
line=IntVar()
Radiobutton(gr,value=1,text="Yes",variable=line).pack(side=LEFT)
Radiobutton(gr,value=0,text="No",variable=line).pack(side=LEFT)
Button(gr,text="Submit",command=sub).pack(side="bottom")
gr.mainloop()
