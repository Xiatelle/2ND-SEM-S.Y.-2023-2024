import cv2

# Load the pre-trained face, eye, and smile cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Open the webcam
video = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not video.isOpened():
    print("Error: Unable to open webcam.")
    exit()


# Function to detect eyes status (open or closed)
def detect_eyes_status(eye_region_gray):
    _, eye_threshold = cv2.threshold(eye_region_gray, 30, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(eye_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return "closed"

    iris_contour = max(contours, key=cv2.contourArea)
    iris_x, iris_y, iris_w, iris_h = cv2.boundingRect(iris_contour)
    aspect_ratio = iris_w / iris_h
    aspect_ratio_threshold = 0.5

    if aspect_ratio < aspect_ratio_threshold:
        return "closed"
    else:
        return "open"


# Function to detect faces, eyes, and smiles in the frame
def detection(gray, frame):
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # For each detected face, detect eyes and smiles
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Region of interest (ROI) for the detected face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Detect smiles within the ROI
        smiles = smile_cascade.detectMultiScale(roi_gray)

        # For each detected eye, draw a rectangle and determine the eye status
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the detected eye
            cv2.rectangle(roi_color, (ex, ey), ((ex + ew), (ey + eh)), (0, 255, 0), 2)

            # Extract the eye region from the grayscale image
            eye_region_gray = roi_gray[ey:ey + eh, ex:ex + ew]

            # Determine the status of the eye (open or closed)
            eye_status = detect_eyes_status(eye_region_gray)

            # Print the status of the detected eye
            print("Right eye:", eye_status)

            # Determine the eye side (right or left) based on the position of the eye within the face
            eye_side = "right" if ex > w // 2 else "left"

            # Print the eye side along with the eye status
            print(eye_side.capitalize() + " eye:", eye_status)

    return frame


# Main loop for reading frames from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = video.read()

    # Check if the frame is successfully read
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Process the frame to detect faces, eyes, and smiles
    canvas = detection(gray, frame)

    # Display the processed frame
    cv2.imshow('Video', canvas)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video.release()
cv2.destroyAllWindows()
