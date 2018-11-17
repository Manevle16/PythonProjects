import numpy as np
import cv2 as cv
import os

os.chdir("C:/Users/Manev/github/Manevle16/PythonProjects/MachineImageProcessing")


cascade = cv.CascadeClassifier('anime_face_cascade_test2.xml')
cascade2 = cv.CascadeClassifier('anime_face_fail1_cascade.xml')
#cascade = cv.CascadeClassifier('lbpcascade_animeface(Not Mine).xml')

for file in os.listdir("TestImages"):
    img = cv.imread("TestImages/"+file)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray, 8, 8)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#    faces2 = cascade2.detectMultiScale(gray, 1.5, 5)
#    for (x, y, w, h) in faces2:
#        cv.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

    img = cv.resize(img, (300, 300))
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
