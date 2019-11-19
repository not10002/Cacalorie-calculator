
from tkinter import * 
def user():
    """User Interface program"""
    gui = Tk() #สร้างui
    gui.geometry("900x900") #ขนาดเริ่มต้นโปรแกรม
    gui.title("Calorie_Calculator") #ชื่อที่แสดงบนหัวโปรแกรม
    label1 = Label(text="Calorie_Calculator", fg="#000").pack() #ข้อความแรกที่แสดง
    button1 = Button(text="submit", fg="red", command=output).pack() #ปุ่มแรกที่แสดง
    gui.mainloop() #คำสั่งให้ใช้งานจนกว่าจะออก

def output():
    """output program"""
    print("test")
user()
