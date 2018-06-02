#!/usr/bin/python3
import cv2

cap = cv2.VideoCapture(0)

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('camera0',frame)  
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('camera1',gray)
    cv2.imshow('camera3',frame)
    cv2.imshow('camera4',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
