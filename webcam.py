import cv2

framewidth = 640
frameheight = 360
stream_url = "http://100.102.40.253:8080/video"
cap = cv2.VideoCapture(stream_url)

while True:
    success, img = cap.read()
    cv2.imshow('test', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break