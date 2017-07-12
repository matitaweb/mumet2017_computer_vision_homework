import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def buildCDF(img, outputImageName, cIndex, title):
    hist= cv2.calcHist([img], [cIndex], None, [256], [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    
    fig = plt.figure()
    
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.title(title) # subplot 211 title
    plt.savefig(outputImageName)

if __name__ == "__main__":
    imgGrey = cv2.imread('img/messi.jpg',0) # grey scale
    buildCDF(imgGrey, "result/01-histogram-cfd-messi-grey.png", 0, "grey")
    imgColor = cv2.imread('img/messi.jpg',1) # color BGR scale
    buildCDF(imgColor, "result/01-histogram-cfd-messi-color_b.png", 0, "b-color")
    buildCDF(imgColor, "result/01-histogram-cfd-messi-color_g.png", 1, "g-color")
    buildCDF(imgColor, "result/01-histogram-cfd-messi-color_r.png", 2, "r-color")