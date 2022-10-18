import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame1 = capture.read()
    frame2 = rescaleFrame(frame1)
    cv.imshow('smol jerky boi', frame2)
    cv.imshow('JerkMate', frame1)
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()