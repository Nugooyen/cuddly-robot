import cv2 as cv

#creates a video capture object which takes video from the webcam
capture = cv.VideoCapture(0)


#iterates frame by frame
while True:
    #creates an image from the current frame of the video feed
    isTrue, frame1 = capture.read()
    

    #converts the frame to gray
    gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

    #creates cascade object from classifier
    haar_cascade = cv.CascadeClassifier('Haar_face.xml')
    
    #increasing minNeigbors decreases the number of false positives
    
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        print(f'{x} {y}')     
    
    #prints number of faces
    print(f'number of faces {len(faces_rect)}')

    # shuts closes window when 'd' is pressed
    cv.imshow('Detected Face', frame1)
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()