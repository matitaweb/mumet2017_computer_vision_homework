import cv2          # import the OpenCV module
import numpy as np  # import the numpy module using the name 'np'.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#HOMEWORK 2

#aggiunge un fattore alla luminosita e poi esegue la normalizzazione
def manageLuminance(img, outputFileName, luninanceAdd):
    
    # cambio in YUV per poter maneggiare la luminosita'
    yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

    t = 0 # per prendere in considerazione la luninosita'
    yuv = yuv.astype(float) #trasformo gli elementi della matrice da uint8 a float per poter aggiungere il valore di aumento
  
    # aggiungo la luminosita'
    yuv[..., t] = yuv[..., t] + luninanceAdd
   
    # faccio la normalizzazione
    m = np.amax(yuv[..., t])
    yuv[..., t] = yuv[..., t] * 255 / m
    
    #ritrasformo in unit8
    yuv = yuv.astype(np.uint8)

    #ritrasformo in BRG poiche' e' l'unico modo di salvare correttamente le immagini
    bgr = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
    cv2.imwrite(outputFileName,bgr)
    
# aumenta la luminosita moltiplicando il pixel per un fattore e poi tagliando a 255
def manageLuminanceCap(img, outputFileName, luninancePerc):
    
    # cambio in YUV per poter maneggiare la luminosita'
    yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

    t = 0 # per prendere in considerazione la luninosita'
    yuv = yuv.astype(float) #trasformo gli elementi della matrice da uint8 a float per poter aggiungere il valore di aumento
  
    # aggiungo la luminosita'
    yuv[..., t] = yuv[..., t] *luninancePerc
   
    # taglio quelli maggiori di 255 mettendoli a 1
    yuv[..., t][yuv[..., t]>255] = 255
 
    
    #ritrasformo in unit8
    yuv = yuv.astype(np.uint8)

    #ritrasformo in BRG poiche' e' l'unico modo di salvare correttamente le immagini
    bgr = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
    cv2.imwrite(outputFileName,bgr)    
    
def manageNegative(img, outputFileName):
    
    #bitwise not
    img = 255 - img;
    
    # the same with opencv
    #img = cv2.bitwise_not(img)

    cv2.imwrite(outputFileName,img)

if __name__ == '__main__':
    #01 for image create illuminance variation a dn negative
    img = cv2.imread('img/messi.jpg',1)
    manageLuminance(img, 'result/01-messi-luminance.jpg', 400)
    manageLuminanceCap(img, 'result/01-messi-luminance-cap.jpg', 3)
    manageNegative(img, 'result/01-messi-negative.jpg')

