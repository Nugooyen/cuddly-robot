import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Pictures/Cat.jpg')
newimg = rescaleFrame(img)

cv.imshow('Cat', img)
cv.imshow('smolCat', newimg)
cv.waitKey(0)