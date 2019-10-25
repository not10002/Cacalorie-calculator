import cv2
import numpy as np
def nothing(x):
    pass
img = cv2.imread("2.jpg")
while True:
    cv2.imshow("img", img)
    color = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    lower = np.array([50, 225, 220])
    upper = np.array([255, 255, 255])

    mask = cv2.inRange(color, lower, upper)
    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("color", color)
    cv2.imshow("oh", res)
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()
