import time
import cv2
import keyboard

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

#get starting position:
_, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
try:
    x0,y0,w0,h0 = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
except:
    raise RuntimeError("No Faces Found")
print(x0, y0, w0, h0)

while True:

    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('You Pressed A Key!')

    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    print(faces)
    cv2.rectangle(img, (x0, y0), (x0 + w0, y0 + h0), (0, 255, 0), 2)

    try:
        x,y,w,h = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        score = abs(x-x0) + abs(y-y0) + abs(h-h0) + abs(w-w0)
        cv2.putText(img=img, text='Garbage Posture Score: ' + str(score), org=(0, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=1)
    except:
        cv2.putText(img=img, text='Garbage Posture Score: NaN', org=(0, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=1)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()