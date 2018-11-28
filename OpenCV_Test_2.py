import cv2
import numpy as np # matrix calc

cap = cv2.VideoCapture(0) # identify the camera

while (1): # loop runs forever
    _, frame = cap.read() # read current frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert image BGR to HSV

    lower_green = np.array([30, 20, 50]) # create a matrix with the three values
    upper_green = np.array([60, 255, 100])
    lower_red = np.array([30, 150, 100])
    upper_red = np.array([255, 255, 200])

    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    green_red = np.add(mask_green, mask_red) # binary array
    #res_green = cv2.bitwise_and(frame, frame, mask=mask_green)
    #res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    res_green_red = cv2.bitwise_and(frame, frame, mask=green_red)

    cv2.imshow('Green & Red', res_green_red)
    #cv2.imshow('res_green', res_green)
    #cv2.imshow('res_red', res_red)

    pmc_green = np.count_nonzero(mask_green)
    pmc_red = np.count_nonzero(mask_red)

    print "pmc_green: ", pmc_green
    print "pmc_red: ", pmc_red

    if pmc_green > 1000 :
        print "I found a brocolli"

    if pmc_red > 1000 :
        print "I found a tomato"

    if pmc_green > 1000 and pmc_red > 1000 :
        print "I made a salad"



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
