import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#HOMEWORK 5

# Utility functions
def show_wait(original, transformed, filename):
    double = np.hstack((original,transformed)) #stacking images side-by-side
    cv2.imwrite(filename, double)


def ex01():
    #01 Mosaiking: take more images with some overlap and construct a long mosaics of the scene
    img422 = cv2.imread('img/Foto422.jpg',1)
    img423 = cv2.imread('img/Foto423.jpg',1)
    
    
    img422pts = np.float32([[186, 39], [269, 21], [189, 159], [266, 156]])
    img423pts = np.float32([[16, 59], [120, 51], [14, 219], [112, 209]])
    

    mat_perspective = cv2.getPerspectiveTransform(img423pts, img422pts)
    
    # compute the homography between the two sets of points
    #(H, status) = cv2.findHomography(img1pts, img2pts, cv2.RANSAC, 1)
    
    
    #warping seconda immagine
    #img2rows, img2cols = img2.shape
    I = -np.identity(3)
    img1WarpedBack = cv2.warpPerspective(img422, I, (1500, 1500))
    img2WarpedFront = cv2.warpPerspective(img423, mat_perspective, (1500, 1500))
    
    img1WarpedBack[img2WarpedFront>0]=0
    img422_423 = img1WarpedBack+img2WarpedFront
    
    
    cv2.imwrite("result/01_img1Warped.jpg", img1WarpedBack)
    cv2.imwrite("result/01_img2Warped.jpg", img2WarpedFront)
    cv2.imwrite("result/01_img422_423.jpg", img422_423)
    

def ex02():
    img424 = cv2.imread('img/Foto424.jpg',1)
    imgPlanpts = np.float32([[0, 111], [191, 44], [24, 216], [299, 122]])
    imgZ0pts = np.float32([[0, 0], [200, 0], [0, 110], [200, 110]])
    
    mat_perspective_z0 = cv2.getPerspectiveTransform(imgPlanpts, imgZ0pts)
    imgZ0Warped = cv2.warpPerspective(img424, mat_perspective_z0, (210, 120))
    cv2.imwrite("result/02_img424_z0.jpg", imgZ0Warped)
    
   
def ex03():
    imgvvf = cv2.imread('img/vvf.jpg',1)
    imgskyscraper= cv2.imread('img/skyscraper.jpg',1)
    imgvvfPts = np.float32([[0, 0], [600, 0], [0,400], [600, 400]])
    imgSkyscraperPts = np.float32([[232, 55], [377, 208], [232, 208], [420, 383]])
    mat_perspective_vvf = cv2.getPerspectiveTransform(imgvvfPts, imgSkyscraperPts)
    I = -np.identity(3)
    imgvvf = cv2.warpPerspective(imgvvf, mat_perspective_vvf, (542, 440))
    cv2.imwrite("result/03_imgvvf.jpg", imgvvf)
    
    imgskyscraper[imgvvf>0]=0
    imgMerge = imgskyscraper+imgvvf
    cv2.imwrite("result/03_merge_face_skyscraper.jpg", imgMerge)

def ex04():
    #04 correct prospective 
    img_sudoku = cv2.imread('img/04_sudoku.jpg', cv2.IMREAD_GRAYSCALE)

    rows, cols = img_sudoku.shape
    print img_sudoku.shape

    dimSquare = 500
    pts1 = np.float32([[74, 87], [36, 515], [520, 520], [470, 70]])
    pts2 = np.float32([[0, 0], [0, dimSquare], [dimSquare, dimSquare], [dimSquare, 0]])

    mat_perspective = cv2.getPerspectiveTransform(pts1, pts2)
    img_sudoku_trasf = cv2.warpPerspective(img_sudoku, mat_perspective, (dimSquare, dimSquare))
    cv2.imwrite('result/04_sudoku-mosaiking.jpg', img_sudoku_trasf)


if __name__ == '__main__':
    
    
    ex01()
    ex02()
    ex03()
    ex04()
    
    
    
    
    
    
    
    """
    manageLuminance(img, 'result/01-messi-luminance.jpg', 400)
    manageLuminanceCap(img, 'result/01-messi-luminance-cap.jpg', 3)
    manageNegative(img, 'result/01-messi-negative.jpg')
    """

