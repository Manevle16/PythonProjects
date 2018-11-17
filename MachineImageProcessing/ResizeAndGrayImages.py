
import numpy as np
import cv2 as cv
import os

os.chdir("C:/Users/Manev/github/Manevle16/PythonProjects/MachineImageProcessing")
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')


for file in os.listdir("NegativeImages"):
    img = cv.imread("NegativeImages/" + file, cv.IMREAD_GRAYSCALE)
    img = cv.resize(img, (100, 100))
    cv.imwrite("NegativeImages/"+file, img)

for file in os.listdir("PositiveImages"):
    img = cv.imread("PositiveImages/" + file, cv.IMREAD_GRAYSCALE)
    img = cv.resize(img, (100, 100))
    cv.imwrite("PositiveImages/"+file, img)
