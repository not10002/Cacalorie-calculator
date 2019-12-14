
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
from viewimg import *

def output():
    """output program"""
    check = var.get()
    if check == 1 :
        myfile = filedialog.askopenfilename() #เลือกไฟล์
        myfile = str(myfile) #แสดงตำแหน่งไฟล์ที่เลือก
        test1(myfile)
    else:
        myfile = filedialog.askopenfilename() #เลือกไฟล์
        myfile = str(myfile) #แสดงตำแหน่งไฟล์ที่เลือก
        test2(myfile)

gui = Tk() #สร้างui
gui.geometry("400x600") #ขนาดเริ่มต้นโปรแกรม
gui.title("Calorie_Calculator") #ชื่อที่แสดงบนหัวโปรแกรม
gui.configure(bg='paleturquoise') #สีพื้นหลัง

load = Image.open("bg.png") #เปิดรูป
render = ImageTk.PhotoImage(load) #Set รูป
img = Label(gui, image=render) #Set เบื้องหลัง
img.place(x=0, y=0) #แสดงพื้นหลัง

label1 = Label().pack() #ข้อความแรกที่แสดง
label1 = Label(text="Calorie_Calculator", fg="#000", font=("Courier", 16), pady=30, bd=8, relief="solid").pack() #ข้อความแรกที่แสดง

myframe=Frame(gui) # สร้างframeขึ้นมาใหม่
myframe.pack() #show frame
scrollbar = Scrollbar(myframe) #เพิ่ม Scrollbar 
scrollbar.pack(side=RIGHT) #แสดงScrollbarไว้ด้านขวา
listbox = Listbox(myframe, yscrollcommand=scrollbar.set, height=8) #เพิ่มlistbox 
listbox.insert(1, "หมู") #แทรกเข้าไปในlistbox
listbox.insert(2, "ไก่") #แทรกเข้าไปในlistbox
listbox.insert(3,   "กุ้ง") #แทรกเข้าไปในlistbox
listbox.pack() #แสดงlistbox
var = IntVar()
var.set(0)
radio1 = Radiobutton(text="ข้าวกระเพรา", padx=20, variable=var, value=1).pack()
radio2 = Radiobutton(text="ข้าวผัดพริกแกง", padx=13, variable=var, value=2).pack()
radio3 = Radiobutton(text="ข้าวผัด", padx=30, variable=var, value=3).pack()

button = Button(text="submit", fg="red", command=output, font=("Courier", 15), bd=8, width=6, relief="raised").pack() #ปุ่มแรกที่แสดง

menubar = Menu(gui)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New") #เพิ่มคำสั่งNew
filemenu.add_command(label="Open") #เพิ่มคำสั่งOpen
filemenu.add_command(label="Close") #เพิ่มคำสั่งClose
menubar.add_cascade(label="File",menu=filemenu) #เพิ่ม menu ชื่อ File
gui.config(menu=menubar)
gui.mainloop() #คำสั่งให้ใช้งานจนกว่าจะออก