# -*- coding: utf-8 -*-
import cv2
 
 
cam = cv2.VideoCapture('/home/tensorflow/jupyter/object_detection/POSCO_PCM_Movie.avi')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/tensorflow/data/DEMO_DATA/POSCO_test.avi',fourcc, 10.0, (640,480))
        
while True:
    ret_val, frame = cam.read()
            
    if ret_val:
        out.write(frame)
        cv2.imshow('My Movie', frame)
                
        if cv2.waitKey(1) == 27: 
            break  # esc to quit

out.release()
cam.release()
        
cv2.destroyAllWindows()


