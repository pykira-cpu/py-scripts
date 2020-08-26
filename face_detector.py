import cv2 

# Cascade classifier for face detection(to be used later)
face_detector = cv2.CascadeClassifier(r'C:\Users\user\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml')

# Grab webcam feed
webcam = cv2.VideoCapture(0)

# Process to capture and show the current frame
while True:

    # read the cuurent frame from the webcam Video Stream
    successfull_frame_read, frame = webcam.read()

    if not successfull_frame_read:
        break

    
    # change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces first
    faces = face_detector.detectMultiScale(frame_grayscale)
    print(faces)

    # Run smile detection within each of those faces
    for (x, y, w, h) in faces:

        # Draw rectangle
        cv2.rectangle(frame, (x,y), (x+w, y+h), (100, 200, 50), 4) # you can choose whichever RGB you want to

    # show the current frame
    cv2.imshow('Smile detector', frame)

    # Display
    cv2.waitKey(1)


# cleanup
webcam.release()
cv2.destroyAllWindows()

