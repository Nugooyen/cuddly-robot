import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame1 = capture.read()
    blurry = cv.GaussianBlur(frame1, (7,7), cv.BORDER_DEFAULT)
    processedFrame = cv.Canny(blurry,50,55)
    cv.imshow('', blurry)
    cv.imshow('JerkMate', processedFrame)
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()