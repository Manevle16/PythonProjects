
import numpy as np
import cv2 as cv
import os

os.chdir("C:/Users/Manev/github/Manevle16/PythonProjects/MachineImageProcessing")
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

if not os.path.exists("negative_images/"):
    os.makedirs("negative_images/")

for file in os.listdir("NegativeImages"):
    img = cv.imread("NegativeImages/" + file, cv.IMREAD_GRAYSCALE)
    img = cv.resize(img, (50, 50))
    cv.imwrite("negative_images/"+file, img)
