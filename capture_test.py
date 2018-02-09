import cv2
import dlib
from imutils import face_utils

detector = dlib.get_frontal_face_detector()
cap = cv2.VideoCapture("udpsrc port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! appsink sync=false")
while True:
    f, frame = cap.read()
    dets = detector(frame, 1)
    for (i, face) in enumerate(dets):
        (x,y,w,h) = face_utils.rect_to_bb(face)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

    cv2.imshow('cap', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()