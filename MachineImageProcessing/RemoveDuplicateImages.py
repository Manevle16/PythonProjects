
import numpy as np
import cv2
from PIL import Image
import os
from PIL import ImageChops

method = cv2.TM_SQDIFF_NORMED


def equal(im1, im2):
    #    print(im1)
    #    print(im2)
    #    print(ImageChops.difference(im1, im2).getbbox() is None)
    return ImageChops.difference(im1, im2).getbbox() is None


os.chdir("C:/Users/Manev/Downloads/Google Images")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# if not os.path.exists("positive_images/"):
#    os.makedirs("positive_images/")

address = "images"
print(os.listdir(address))
i = 1
files = os.listdir(address)
for file in files:
    for file2 in files:
        if(file == file2):
            continue
    #    img1 = Image.open(address + "/" + file)
    #    img2 = Image.open(address + "/" + file2)

        # Read the images from the file
        small_image = cv2.imread(address + "/" + file)
        large_image = cv2.imread(address + "/" + file2)
        graySmall = cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)
        grayLarge = cv2.cvtColor(large_image, cv2.COLOR_BGR2GRAY)

        if(small_image.shape[0] > large_image.shape[0] or small_image.shape[1] > large_image.shape[1]):
            continue

        result = cv2.matchTemplate(graySmall, grayLarge, method)
        if(np.min(result) > .01):
            continue
        else:
            print(file + " is same as " + file2)
            files.remove(file)
            os.remove(address + "/" + file)
            break
#        print(file + " > " + file2 + " :" + str(np.min(result)))
        # We want the minimum squared difference
#        mn, _, mnLoc, _ = cv2.minMaxLoc(result)

        # Draw the rectangle:
        # Extract the coordinates of our best match
#        MPx, MPy = mnLoc

        # Step 2: Get the size of the template. This is the same size as the match.
#        trows, tcols = small_image.shape[:2]

        # Step 3: Draw the rectangle on large_image
#        cv2.rectangle(large_image, (MPx, MPy), (MPx+tcols, MPy+trows), (0, 0, 255), 2)

        # Display the original image with the rectangle around the match.
#        cv2.imshow('output', large_image)

        # The image is only displayed if we call this
#        cv2.waitKey(0)


'''faces = face_cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
