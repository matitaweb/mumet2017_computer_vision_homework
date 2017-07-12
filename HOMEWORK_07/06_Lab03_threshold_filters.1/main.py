# Lab3 - Thresholds and filters


import cv2
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Applying a threshold on an image like OTSU
img = cv2.imread('shades.jpg', cv2.IMREAD_GRAYSCALE)
thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
double = np.hstack((img,thresh)) #stacking images side-by-side
cv2.imwrite('result/shades-threshold.jpg', double)


# Gaussian Filter
# info about image filtering: https://goo.gl/T6zED3
img = cv2.imread('2.png', cv2.IMREAD_GRAYSCALE)
filtered = cv2.GaussianBlur(img, (1, 1), 1.0)
double = np.hstack((img,filtered)) #stacking images side-by-side
cv2.imwrite('result/2-gaussian.png', double)


# EXERCISES
# Try the cv2.adaptiveThreshold() on the sudoku.jpg image to see the correct binary image.
# http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Global_Thresholding_Adaptive_Thresholding_Otsus_Binarization_Segmentations.php
img = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,10) 
double = np.hstack((img,th2)) #stacking images side-by-side
cv2.imwrite('result/sudoku-adaptive_meanc.jpg', double)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,10)
double = np.hstack((img,th3)) #stacking images side-by-side
cv2.imwrite('result/sudoku-adaptive_gaussianc.jpg', double)

# Try also the median cv2.medianBlur() 
thMedianBlur = cv2.medianBlur(img,7)
double = np.hstack((img,thMedianBlur)) #stacking images side-by-side
cv2.imwrite('result/sudoku-median-blur.jpg', double)

# Try also the median and bilateral filters  cv2.bilateralFilter()

bilateral = cv2.bilateralFilter(img, 10, 15, 15)
double = np.hstack((img,bilateral)) #stacking images side-by-side
cv2.imwrite('result/sudoku-bilateral.jpg', double)