import cv2
import os

img = cv2.imread("image.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors =5)
for x,y,w,h in faces:
    image = cv2.rectangle(image, (x,y), (x+w, y+h),(25,224,24),)
cv2.imshow('Image', image)
cv2.waitKey(0)