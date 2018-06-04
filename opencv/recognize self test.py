import cv2

face_haar = cv2.CascadeClassifier("C:/opencv/build/x64/vc14/bin/nest/cascade.xml")

cam = cv2.VideoCapture(0)

while True:
    ret,img = cam.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_haar.detectMultiScale(gray_img, 1.3, 5)
    for face_x, face_y, face_w, face_h in faces:
        cv2.rectangle(img, (face_x, face_y), (face_x + face_w, face_y + face_h), (0, 255, 0), 2)
        roi_gray_img = gray_img[face_y:face_y + face_h, face_x:face_x + face_w]
        roi_img = img[face_y:face_y + face_h, face_x:face_x + face_w]

    cv2.imshow('img', img)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()