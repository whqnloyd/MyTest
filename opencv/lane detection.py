import cv2
import numpy as np

cap = cv2.VideoCapture('video/example.mp4')

#改变探测区域
def region_of_interest(imgs, vertices):
    roi_mask = np.zeros_like(imgs)
    channel_count = imgs.shape[2]
    match_maks_color = (255,) * channel_count
    cv2.fillPoly(roi_mask, vertices, match_maks_color)
    masked_image = cv2.bitwise_and(imgs, roi_mask)
    return masked_image


#绘制直线
def draw_lines(images, lines_, color=[255, 0, 0], thickness=3):
    if lines_ is None:
        return
    img = np.copy(images)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8, )
    for line in lines_:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    return img


#对图片进行灰度和颜色处理
def transfer_image(image_roied):
    # GRAY处理，HSV处理
    gray_image = cv2.cvtColor(image_roied, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(image_roied, cv2.COLOR_BGR2HSV)

    # 设置白色及黄色
    lower_yellow = np.array([20, 100, 100], dtype='uint8')
    upper_yellow = np.array([30, 255, 255], dtype='uint8')
    mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(gray_image, 200, 255)
    mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
    mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)

    # 高斯降噪
    gauss_image = cv2.GaussianBlur(mask_yw_image, (5, 5), 0)
    return gauss_image
#    return mask_yw_image


#检测边缘及线段
def find_edg_lines(img):
    # 检测边缘
    low_threshold = 50
    high_threshold = 150
    cannyed_edges = cv2.Canny(img, low_threshold, high_threshold)

    # 霍夫变换，找到边缘对应的直线段
    lines = cv2.HoughLinesP(
        cannyed_edges,
        rho=6,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25
    )
    return lines


while True:
    #帧读取为图片
    ret, image = cap.read()
#    cv2.imshow('test', image)
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [(0, height), (width / 2, height / 2), (width, height), ]
    #改变探测区域
    image_roied = region_of_interest(image, np.array([region_of_interest_vertices], np.int32))
#    plt.figure()
#    plt.imshow(image_roied)

    #图片处理
    image_color_gray = transfer_image(image_roied)

    #得到线段
    lines = find_edg_lines(image_color_gray)

    #绘制直线
    line_image = draw_lines(image, lines)

    #显示图像
    if line_image is not None:
        cv2.imshow("capture", line_image)
    else:
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
