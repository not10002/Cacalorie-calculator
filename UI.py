
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def user():
    """User Interface program"""
    gui = Tk() #สร้างui
    gui.configure(bg='paleturquoise') #ตั้งสีเบื้องหลัง
    gui.geometry("900x900") #ขนาดเริ่มต้นโปรแกรม
    gui.title("Calorie_Calculator") #ชื่อที่แสดงบนหัวโปรแกรม
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
    print("test")
def box(event):
    """box program"""
    status = messagebox.askyesno(title="showcase", message="calorie calculator")
    if status == 0:
        print("กด No")
    else:
        print("กด Yes")
def wantfile(event):
    """want program"""
    filedialog.askopenfile()
user()
