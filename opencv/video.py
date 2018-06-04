import cv2

# Step1. 构造VideoCapture对象
cap = cv2.VideoCapture('video/Arduino Quadruped Robot - YouTube.MP4')

# Step2. 创建一个背景分割器
# createBackgroundSubtractorKNN()函数里，可以指定detectShadows的值
# detectShadows=True，表示检测阴影，反之不检测阴影
knn = cv2.createBackgroundSubtractorKNN(detectShadows=True)

while True :
    ret, frame = cap.read() # 读取视频
    fgmask = knn.apply(frame) # 背景分割
    cv2.imshow('frame', fgmask) # 显示分割结果
    if cv2.waitKey(100) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()