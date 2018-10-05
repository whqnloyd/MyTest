import cv2

cap = cv2.VideoCapture(0)

width = 640
height = 480
angle = 180
fps = 29

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, fps)


def rotate(img, ang, center=None, scale=None): 
    (h, w) = img.shape[:2] 
    if center == None:
        center = (w // 2, h // 2)
    if scale == None:
        scale = 1.0

    M = cv2.getRotationMatrix2D(center, ang, scale) 

    rot = cv2.warpAffine(img, M, (w, h)) 
    return rot 

while(1):
    ret,frame = cap.read()
    image = rotate(frame, angle)

    cv2.imshow("capture", image)
    if cv2.waitKey(1) & 0xFF == ord('`'):
        break

cap.release()
cv2.destroyAllWindows()
