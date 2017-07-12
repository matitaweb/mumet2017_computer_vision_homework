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

def translation(img, x, y):
    rows, cols, channels = img.shape
    M_trans = np.float32([[1, 0, x], [0, 1, y]])
    dst_trans = cv2.warpAffine(img, M_trans, (cols, rows))
    return dst_trans


# ROTATION
# Rotate the image by 45 degrees
# params are center of rotation, angle and scale
def rotation(img, degree):
    rows, cols, channels = img.shape
    M_rot = cv2.getRotationMatrix2D((cols/2, rows/2), degree, 1)
    dst_rot = cv2.warpAffine(img, M_rot, (cols, rows))
    return dst_rot


if __name__ == '__main__':
    
     #04 correct prospective 
    img_mumet = cv2.imread('img/mumet.jpg', 1)
    x = 50
    y= 100
    img_t = translation(img_mumet, x,y)
    show_wait(img_mumet, img_t, "result/01_mumet_translated.jpg")
    
    d= 60
    img_r = rotation(img_mumet, -d)
    show_wait(img_mumet, img_r, "result/01_mumet_rotated.jpg")
    
    

    
    
    
    
    
    
    
    """
    manageLuminance(img, 'result/01-messi-luminance.jpg', 400)
    manageLuminanceCap(img, 'result/01-messi-luminance-cap.jpg', 3)
    manageNegative(img, 'result/01-messi-negative.jpg')
    """

