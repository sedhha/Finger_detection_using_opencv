import numpy as np
import cv2
import time

cam=cv2.VideoCapture(1)
a=[]
i2=0
isel=0
print("Calibrated for distance of 20cm, approx avoid skin color backgrounds... \ntry to put all fingers within camera feed for best results")
time.sleep(5)
while True:
    #try:
    ret,frame=cam.read()
    if ret==False:
        print("Please change cv2.VideoCapture(1) to cv2.VideoCapture(0)")
    frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img_gray=cv2.fastNlMeansDenoising(img_gray,None)
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    
    image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #x=index(max(cv2.contourArea(contours)))
     
    img = cv2.drawContours(thresh, contours, -1, (120,220,0), 2)
    im=np.zeros_like(img)
    cv2.drawContours(im,contours,-1,(150,10,220),2)
    cv2.imshow('i',im)
    print(np.std(img))
    if np.std(img)<=112:
        print("Number of fingers = 1")
    elif np.std(img)<=116:
        print("Number of fingers = 2")
    elif np.std(img)<=118:
        print("Number of fingers = 3")
    elif np.std(img)<=120:
        print("Number of fingers = 4")
    elif np.std(img)>120:
        print("Number of fingers = 5")

    cv2.imshow('Actual frame',frame)
    a=[]
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Terminating")
        break
    '''except:
        print('Shit!')
        pass'''
cam.release()
cv2.destroyAllWindows()


    
