import cv2

image_path = "1000s.jpg"
image = cv2.imread(image_path)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) == 0:
    print("No face found in the photo")
else:
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 4)

    output_image_path = "output.png"
    cv2.imwrite(output_image_path, image)

    print("Face on the photo successfuly outline. Result saved to", output_image_path)