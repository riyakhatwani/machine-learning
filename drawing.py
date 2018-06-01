
import cv2
img=cv2.imread('/home/riya/Downloads/iimages.jpeg',1)
print (img.shape)
cv2.line(img,(0,0),(80,80),(0,0,255),2)
cv2.rectangle(img,(80,80),(160,160),(0,255,0))
cv2.imshow('myimage',img)
cv2.waitKey(0)

