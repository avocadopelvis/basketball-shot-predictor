import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

#initialize the videO
cap = cv2.VideoCapture('Videos/vid (1).mp4')

#create the color finder object
myColorFinder = ColorFinder(False) #change to false after you find the hsv values of the ball
hsvVals = {'hmin': 0, 'smin': 101, 'vmin': 87, 'hmax': 17, 'smax': 255, 'vmax': 255}

while True:
    #GRAB THE IMAGE
    #try image with video
    success, img = cap.read()
    # img =  cv2.imread('Ball.png')
    #crop the image 
    img = img[0:900, :] #only cropping height

    #FIND THE COLOR OF THE BALL
    imgColor, mask = myColorFinder.update(img, hsvVals)

    #FIND THE LOCATION OF THE BALL #19:42

    #DISPLAY
    #resize the image
    imgColor = cv2.resize(imgColor, (0, 0), None, 0.7, 0.7)
    #show the image
    # cv2.imshow('Image', img)
    cv2.imshow('ImageColor', imgColor)
    #delay time
    cv2.waitKey(50) #50 milisecond 