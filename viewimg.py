import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

def nothing(x):
    pass
def test1(myfile):
    img = cv2.imread(myfile) #image read
    while True:
        img = cv2.resize(img, (500,500)) #window size
        color = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) #change type color

        lower = np.array([0, 85, 0]) # ค่าของสีที่น้อยที่สุด
        upper = np.array([255, 255, 255]) # ค่าของสีที่มากที่สุด

        mask = cv2.inRange(color, lower, upper) #แสดงช่วงสีนั้น
        res = cv2.bitwise_and(img, img, mask=mask) #แสดงช่วงสีนั้นแต่แสดงสีเดิม
        cv2.imshow("oh", res)
        messagebox.showinfo(title="wow", message="กระเพราไก่ = 295 KCal")
        if cv2.waitKey(1): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
    while True:
        img = cv2.resize(img, (500,500)) #window size
        color = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) #change type color

        lower = np.array([0, 0, 175]) # ค่าของสีที่น้อยที่สุด
        upper = np.array([255, 255, 255]) # ค่าของสีที่มากที่สุด

        mask = cv2.inRange(color, lower, upper) #แสดงช่วงสีนั้น
        res = cv2.bitwise_and(img, img, mask=mask) #แสดงช่วงสีนั้นแต่แสดงสีเดิม
        cv2.imshow("oh", res)
        messagebox.showinfo(title="wow", message="ข้าวสวย = 260 KCal")
        if cv2.waitKey(1): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
    while True:
        img = cv2.resize(img, (500,500)) #window size
        cv2.imshow("img", img) #show image
        messagebox.showinfo(title="wow", message="total = 260 + 295 = 555 KCal")
        if cv2.waitKey(1): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
def test2(myfile):
    """test2 program"""
    img = cv2.imread(myfile) #image read
    while True:
        img = cv2.resize(img, (500,500)) #window size
        color = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) #change type color

        lower = np.array([0, 85, 0]) # ค่าของสีที่น้อยที่สุด
        upper = np.array([255, 255, 255]) # ค่าของสีที่มากที่สุด

        mask = cv2.inRange(color, lower, upper) #แสดงช่วงสีนั้น
        res = cv2.bitwise_and(img, img, mask=mask) #แสดงช่วงสีนั้นแต่แสดงสีเดิม
        cv2.imshow("oh", res)
        messagebox.showinfo(title="wow", message="ผัดพริกแกง = 265 KCal")
        if cv2.waitKey(1): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
    while True:
        img = cv2.resize(img, (500,500)) #window size
        color = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) #change type color

        lower = np.array([0, 0, 175]) # ค่าของสีที่น้อยที่สุด
        upper = np.array([255, 255, 255]) # ค่าของสีที่มากที่สุด

        mask = cv2.inRange(color, lower, upper) #แสดงช่วงสีนั้น
        res = cv2.bitwise_and(img, img, mask=mask) #แสดงช่วงสีนั้นแต่แสดงสีเดิม
        cv2.imshow("oh", res)
        messagebox.showinfo(title="wow", message="ข้าวสวย = 260 KCal")
        if cv2.waitKey(1): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
    while True:
        img = cv2.resize(img, (500,500)) #window size
        cv2.imshow("img", img) #show image
        messagebox.showinfo(title="wow", message="total = 260 + 265 = 525 KCal")
        if cv2.waitKey(1): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
