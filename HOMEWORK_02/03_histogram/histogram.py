import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#HOMEWORK 2

"""
http://docs.opencv.org/trunk/d0/d86/tutorial_py_image_arithmetics.html

"""
    
    

#TEST
if __name__ == '__main__':
    #01 for image create illuminance variation a dn negative
    img1 = cv2.imread('img/coin.jpg')
    
    img1b = cv2.medianBlur(img1,5)
    img1b = cv2.GaussianBlur(img1b,(5,5),0)
    
    # Apply thresholding on the background and display the resulting mask
    ret, mask = cv2.threshold(img1b, 15, 255, cv2.THRESH_BINARY)

	# Note: The mask is displayed as a RGB image, you can
	# display a grayscale image by converting 'foreGround' to
	# a grayscale before applying the threshold.
	
    cv2.imwrite("result/mask.jpg",mask)
    cv2.imwrite("result/ret.jpg", ret)
    ro, co, ch =  img1.shape
    cut = np.zeros((ro, co, ch))
    #cut[mask]=img1
    cv2.imwrite("result/cut.jpg", cut)
    #a=1
    #img = cv2.addWeighted(img1,a,img2,1-a,0)
    
    """
    img2 = cv2.imread('img/home2.jpeg')
    b1 = manageBlending(img1, img2, 'result/home1-home2-blend-02.jpeg', 0.2)
    b2 = manageBlending(img1, img2, 'result/home1-home2-blend-04.jpeg', 0.4)
    b3 = manageBlending(img1, img2, 'result/home1-home2-blend-06.jpeg', 0.6)
    b4 = manageBlending(img1, img2, 'result/home1-home2-blend-08.jpeg', 0.8)
    double1 = np.hstack((b1,b2)) #stacking images side-by-side
    double2 = np.hstack((b2,b3)) #stacking images side-by-side
    double12 = np.hstack((double1,double2))
    cv2.imwrite("result/all.jpeg",double12)
    """