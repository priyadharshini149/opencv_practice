import cv2 as cv
#reading images
image=cv.imread('images/image1.jpeg')
cv.imshow('People',image)
cv.waitKey(0)  #time in ms 


# reading video
capture=cv.VideoCapture('videos/video1.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #press d to stop video
        break
capture.release()
cv.destroyAllWindows()
    
