import cv2
cap = cv2.VideoCapture("udpsrc port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! appsink sync=false")
while True:
    f, frame = cap.read()
    cv2.imshow('cap', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()