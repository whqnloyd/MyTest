import cv2

# Step1. 读入图像
image = cv2.imread('image/06bf0e5e92987c3d92e028dc16089d3b_b.jpg', 0)

# Step2. 二值化
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Step3. 轮廓提取
image, contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step4. 轮廓绘制
color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst = cv2.drawContours(color, contour, -1, (0,255,0), 2)

cv2.imshow("dst", dst)

cv2.waitKey(0)