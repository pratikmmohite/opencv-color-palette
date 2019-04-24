import numpy as np
import cv2 as cv
def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
while True:
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    img[:] = [b,g,r]
    color=cv.cvtColor(img,cv.COLOR_RGB2HSV)
    font = cv.FONT_HERSHEY_SIMPLEX
    text=str(color[0,0])
    cv.putText(img,'HSV =',(100,222), font, 1,(255,255,255),2,cv.LINE_AA)
    cv.putText(img,text,(220,222), font, 1,(255,255,255),2,cv.LINE_AA)
cv.destroyAllWindows()
