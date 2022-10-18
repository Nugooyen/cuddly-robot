import cv2 as cv

#stock image
img = cv.imread('Pictures/Cat.jpg')

#image effects

# grayscale
grayimg= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cat image', grayimg)

#simple blur

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blurred img', blur)

# edge cascade ( lots of edges)

canny = cv.Canny(img,125,175)
cv.imshow("edges", canny)

canny2 = cv.Canny(blur,125,175)
cv.imshow("edges after blurred", canny2)


cv.waitKey(0)
