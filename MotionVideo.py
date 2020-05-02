import cv2

video = cv2.VideoCapture(0)

a = 1

while True:
    a = a + 1
    check, frame = video.read()
    # print(frame)
    
    # Font type to be used
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # To display text on video
    cv2.putText(frame,
                'Press \'q\' to quit',
                (50, 50),
                font, 1,
                (0, 255, 255),
                2)
    # For Color video
    cv2.imshow('My_Color_Video', frame)
    
    # For Black and White / Gray  video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('My_Video', gray)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

# print(a)
video.release()
cv2.destroyAllWindows()
