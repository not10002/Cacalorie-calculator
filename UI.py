
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

def user():
    """User Interface program"""
    gui = Tk() #สร้างui
    gui.geometry("450x550") #ขนาดเริ่มต้นโปรแกรม
    gui.title("Calorie_Calculator") #ชื่อที่แสดงบนหัวโปรแกรม
    gui.configure(bg='paleturquoise') #สีพื้นหลัง

    load = Image.open("bg.png") #เปิดรูป
    render = ImageTk.PhotoImage(load) #Set รูป
    img = Label(gui, image=render) #Set เบื้องหลัง
    img.place(x=0, y=0) #แสดงพื้นหลัง

    label1 = Label(text="Calorie_Calculator", fg="#000").pack() #ข้อความแรกที่แสดง
    button1 = Button(text="submit", fg="red", command=output).pack() #ปุ่มแรกที่แสดง
    button2 = Button(text="first") #ปุ่มที่สองที่แสดง
    button2.bind('<Button-1>',box) #สั้งใช้งานbox function
    button2.pack()
    button3 = Button(text="Select") #ปุ่มที่สามที่แสดง
    button3.bind('<Button-1>',wantfile) #สั้งใช้งานwant function
    button3.pack()

    textbox = Entry().pack()
    gui.mainloop() #คำสั่งให้ใช้งานจนกว่าจะออก

def output():
    """output program"""
    print("test") #แสดง output
def box(event):
    """box program"""
    status = messagebox.askyesno(title="showcase", message="calorie calculator") #แสดงหน้าต่าง
    if status == 0: #ถ้ากดno
        print("กด No")
    else: #ถ้ากดyes
        print("กด Yes")
def wantfile(event):
    """want program"""
    myfile = filedialog.askopenfile() #เลือกไฟล์
    label2 = Label(text=myfile).pack() #แสดงตำแหน่งไฟล์ที่เลือก
user()
