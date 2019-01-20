#!/usr/bin/python36
import cv2
import math
import numpy as np
xv = cv2.VideoCapture(0)#Pointer to camera
front_face = cv2.CascadeClassifier("haarcasde_frontalface_default.xml")
while True:#Video Capture
        r,photo = xv.read()
        photo=cv2.imread("/root/Desktop/1.jpg")
        faces = front_face.detectMultiScale(photo,1.3,5)
        for i in faces:
            x,y,h,w=i
            cv2.rectangle(photo,(x,y),(x+w,y+w),(255,0,0),5)
        if len(faces) >= 2 :
            i,j = faces
            x1,y1,h1,w1 = i
            x,y,h,w = j
            f1 = np.copy(photo[y1:y1+min(w1,w),x1:x1+min(h1,h)])
            f2 = np.copy(photo[y:y+min(w1,w),x:x+min(h1,h)])
            photo[y1:y1+min(w1,w),x1:x1+min(h1,h)],photo[y:y+min(w1,w),x:x+min(h1,h)]=f2,f1
        cv2.imshow('hi',photo)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
xv.release()
cv2.destroyAllWindows()
