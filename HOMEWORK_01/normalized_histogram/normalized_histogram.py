import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#01 
img = cv2.imread('img/messi.jpg',0)
print img
plt.hist(img.ravel(),256,[0,256]);
plt.savefig("result/01-histogram-messi.png")

#02
img = cv2.imread('img/messi.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #affianca le immagini prolungando le rige del della matrice img con quelle di equ
cv2.imwrite('result/02-messi-normalized.png',res)
plt.hist(res.ravel(),256,[0,256])
plt.savefig("result/02-histogram-messi-normalized.png")