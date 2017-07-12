import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#HOMEWORK 2


def manageBlending(img1, img2, outputFileName, a):
    img = cv2.addWeighted(img1,a,img2,1-a,0)
    cv2.imwrite(outputFileName,img)
    return img

if __name__ == '__main__':
    #01 for image create illuminance variation a dn negative
    img1 = cv2.imread('img/home1.jpeg')
    img2 = cv2.imread('img/home2.jpeg')
    
    b1 = manageBlending(img1, img2, 'result/home1-home2-blend-02.jpeg', 0.2)
    b2 = manageBlending(img1, img2, 'result/home1-home2-blend-04.jpeg', 0.4)
    b3 = manageBlending(img1, img2, 'result/home1-home2-blend-06.jpeg', 0.6)
    b4 = manageBlending(img1, img2, 'result/home1-home2-blend-08.jpeg', 0.8)
    double1 = np.hstack((b1,b2)) #stacking images side-by-side
    double2 = np.hstack((b2,b3)) #stacking images side-by-side
    double12 = np.hstack((double1,double2))
    cv2.imwrite("result/all.jpeg",double12)