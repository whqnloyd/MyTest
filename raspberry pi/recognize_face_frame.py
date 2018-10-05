import cv2

cam = cv2.VideoCapture(0)
face_haar = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")
eye_haar = cv2.CascadeClassifier("data/haarcascades/haarcascade_eye.xml")

width = 640
height = 480
angle = 180
fps = 29

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, fps)


def rotate(img, ang, center=None, scale=None): 
    (h, w) = img.shape[:2] 
    if center == None:
        center = (w // 2, h // 2)
    if scale == None:
        scale = 1.0

    M = cv2.getRotationMatrix2D(center, ang, scale) 

    rot = cv2.warpAffine(img, M, (w, h)) 
    return rot

while True:
    ret,frame = cam.read()
    img = rotate(frame, angle)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_haar.detectMultiScale(gray_img, 1.3, 5)
    
    for face_x, face_y, face_w, face_h in faces:
        cv2.rectangle(img, (face_x, face_y), (face_x + face_w, face_y + face_h), (0, 255, 0), 2)
        roi_gray_img = gray_img[face_y:face_y + face_h, face_x:face_x + face_w]
        roi_img = img[face_y:face_y + face_h, face_x:face_x + face_w]
        eyes = eye_haar.detectMultiScale(roi_gray_img, 1.3, 5)
        
        for eye_x, eye_y, eye_w, eye_h in eyes:
            cv2.rectangle(roi_img, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('`'):
        break
    
cam.release()
cv2.destroyAllWindows()