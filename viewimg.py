import cv2
import numpy as np

img = cv2.imread("1.jpg", -1)
while True:
    color = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("image", img)
    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])
    mask = cv2.inRange(color, l_b, u_b)
    cv2.imshow("mask", mask)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        break
    cv2.destroyAllWindows()
