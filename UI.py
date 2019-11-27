
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

    label1 = Label(text="Calorie_Calculator", fg="#000", font=("Courier", 24), bd=8, relief="solid").pack() #ข้อความแรกที่แสดง
    button1 = Button(text="submit", fg="red", command=output, font=("Courier", 15), bd=8, width=6, relief="raised").pack() #ปุ่มแรกที่แสดง
    button2 = Button(text="first", font=("Courier", 15), bd=8, width=6, relief="raised") #ปุ่มที่สองที่แสดง
    button2.bind('<Button-1>',box) #สั้งใช้งานbox function
    button2.pack()
    button3 = Button(text="Select", font=("Courier", 15), bd=8, width=6, relief="raised") #ปุ่มที่สามที่แสดง
    button3.bind('<Button-1>',wantfile) #สั้งใช้งานwant function
    button3.pack()

    myframe=Frame(gui) # สร้างframeขึ้นมาใหม่
    myframe.pack() #show frame
    scrollbar = Scrollbar(myframe) #เพิ่ม Scrollbar 
    scrollbar.pack(side=RIGHT) #แสดงScrollbarไว้ด้านขวา
    listbox = Listbox(myframe, yscrollcommand=scrollbar.set, height=2) #เพิ่มlistbox 
    listbox.insert(1, "ข้าวกระเพรา") #แทรกเข้าไปในlistbox
    listbox.insert(2, "บะหมี่") #แทรกเข้าไปในlistbox
    listbox.insert(3, "ข้าวผัด") #แทรกเข้าไปในlistbox
    listbox.pack() #แสดงlistbox
    radio1 = Radiobutton(text="หมู", value=1).pack()
    radio2 = Radiobutton(text="ไก่", value=2).pack()
    radio3 = Radiobutton(text="กุ้ง", value=3).pack()

    textbox = Entry().pack() # เพิ่มและแสดง textbox

    menubar = Menu(gui)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New") #เพิ่มคำสั่งNew
    filemenu.add_command(label="Open") #เพิ่มคำสั่งOpen
    filemenu.add_command(label="Close") #เพิ่มคำสั่งClose
    menubar.add_cascade(label="File",menu=filemenu) #เพิ่ม menu ชื่อ File
    gui.config(menu=menubar)
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
