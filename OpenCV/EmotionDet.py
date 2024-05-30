import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.imread('happy.jpg, cv2.IMREAD_COLOR')


if not cam.isOpened():
    raise IOError("Camera not opened")

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        try:
            analyze = DeepFace.analyze(face_roi, actions=['emotion'])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 2)
            cv2.putText(frame, analyze['dominant_emotion'], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(analyze['dominant_emotion'])
        except:
            print("No Face Detected")

    cv2.imshow('cam', frame)
    if cv2.waitKey(1) == ord('v'):
        break

cv2.imshow('cam', cam)
cv2.waitKey(0)

cv2.destroyAllWindows()
