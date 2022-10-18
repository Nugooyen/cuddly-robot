import cv2 as cv
import numpy as np

#create an array filled with zeroes of 500 by 500, with 4 color channels
blank = np.zeros((500,500,3), dtype='uint8')

cv.imshow('blank' , blank)

# paint image a certain color
blank[:] = 200,255,200
cv.imshow('blank 2' , blank)

blank[0:100, 100:300] = 200,100,200
cv.imshow('blank screen' , blank)

cv.rectangle(blank, (100,150), (250,250), (0,0,0), thickness=2)
cv.putText(blank, "hewoo world", (100, 130), cv.FONT_HERSHEY_COMPLEX, 1.0, (10,10,10), thickness=2 )
cv.imshow('Rect and text',blank)
cv.waitKey(0)
