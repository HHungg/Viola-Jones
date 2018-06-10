import numpy as np
import cv2
#face_cascade = cv2.CascadeClassifier('C:/Users/kaise/Anaconda3/pkgs/opencv-3.3.0-py36_201/Library/etc/haarcascades/haarcascade_frontalface_alt2.xml')
face_cascade = cv2.CascadeClassifier('E:\Program Files\Results\classifier\cascade.xml')
img = cv2.imread('Linkin Park.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.085, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()