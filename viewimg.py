import cv2
import numpy as np
def nothing(x):
    pass
def main(myfile):
    img = cv2.imread(myfile) #image read
    while True:
        img = cv2.resize(img, (500,500)) #window size
        cv2.imshow("img", img) #show image
        color = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) #change type color

        lower = np.array([0, 85, 0]) # ค่าของสีที่น้อยที่สุด
        upper = np.array([255, 255, 255]) # ค่าของสีที่มากที่สุด

        mask = cv2.inRange(color, lower, upper) #แสดงช่วงสีนั้น
        res = cv2.bitwise_and(img, img, mask=mask) #แสดงช่วงสีนั้นแต่แสดงสีเดิม
        cv2.imshow("color", color)
        cv2.imshow("oh", res)
        if cv2.waitKey(0): #จะปิดเมื่อกดคียบอร์ด
            break
        cv2.destroyAllWindows() #show all window
