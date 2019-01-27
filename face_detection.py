# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:20:40 2019

@author: CAPTAIN
"""

import cv2

face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier("haarcascade_eye.xml")

def detect(gray,frame):
    faces=face.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray=gray[y:y+h,x:x+w]
        roi_frame=frame[y:y+h,x:x+w]
        
        eyes=eye.detectMultiScale(roi_gray,1.1,3)
        
        for (k,l,m,n) in eyes:
            cv2.rectangle(roi_frame,(k,l),(k+m,l+n),(0,255,0),2)
            
    return frame

video=cv2.VideoCapture(0)

while True:
    _,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    pic=detect(gray,frame)
    cv2.imshow("hey",pic)
    
    if cv2.waitKey(1) & 0XFF==ord('q'):
        video.release()
        cv2.destroyAllWindows()