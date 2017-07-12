import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#HOMEWORK 2

# Utility functions
def show_wait(original, transformed, filename):
    double = np.hstack((original,transformed)) #stacking images side-by-side
    cv2.imwrite(filename, double)
    
def drawrectange(img, x,y,h,w):
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,'rectangle',(x+w+10,y+h),0,0.3,(0,255,0))
    return img
    
if __name__ == '__main__':
    img1 = cv2.imread('img/1.jpg',1)
    imgcopy = img1.copy()
    x= 100
    y=100
    h=50
    w=60
    img1 = drawrectange(img1, x,y,h,w)
    show_wait(imgcopy, img1, "result/rectangle.jpg")
    
    img1 = cv2.imread('img/1.jpg',1)
    x1 = 300
    y1 = 300
    x2 = 160
    y2 = 150
    h=y2-y1
    w=x2-x1
    img1 = drawrectange(img1, x1,y1,h,w)
    show_wait(imgcopy, img1, "result/rectangle_2.jpg")