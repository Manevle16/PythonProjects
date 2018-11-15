import numpy as np
import cv2 as cv
import os

os.chdir("C:/Users/Manev/github/Manevle16/PythonProjects/MachineImageProcessing")


cascade = cv.CascadeClassifier('anime_face_fail1_cascade.xml')
img = cv.imread('test7.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
