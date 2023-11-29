import dlib
import cv2

# Load face recognition model from dlib
detector = dlib.get_frontal_face_detector()

# Start capturing video from the default camera (you can change the parameter to use a different camera obscura)
cap = cv2.VideoCapture(0)

while True:
    # Capturing one frame-by- another frame
    ret, frame = cap.read()

    # Face detection converting  the frame to grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #  It Detects faces in grayscale frames
    faces = detector(gray)

    # Draw rectangluar boxes around the face
    for face in faces:
        i, j, wt, ht = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (i, j), (i + wt, j + ht), (0, 255, 0), 2)

    # print the result frame
    cv2.imshow('Face Recognition', frame)

    #  At last Break the loop when 'q' key is clicked
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Discharge the video captured object and shut the window
cap.release()
cv2.destroyAllWindows()
