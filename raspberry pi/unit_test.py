import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = 640
height = 480
angle = 180
fps = 29

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, fps)

region_of_interest_vertices = [(3, height), (3, height-20), (width / 2, height / 2 + 30), (width, height-20), (width, height),]

#rotate picture
def rotate(img, ang, center=None, scale=None): 
    (h, w) = img.shape[:2] 
    if center == None:
        center = (w // 2, h // 2)
    if scale == None:
        scale = 1.0

    M = cv2.getRotationMatrix2D(center, ang, scale) 

    rot = cv2.warpAffine(img, M, (w, h)) 
    return rot


#对图片进行灰度和颜色处理
def transfer_image(image_roied):
    # GRAY处理，HSV处理
    gray_image = cv2.cvtColor(image_roied, cv2.COLOR_BGR2GRAY)
#    hsv_image = cv2.cvtColor(image_roied, cv2.COLOR_BGR2HSV)
    '''
    # black lines
    lower_range = np.array([0, 0, 0], dtype='uint8')
    upper_range = np.array([180, 255, 46], dtype='uint8')
    mask_black = cv2.inRange(hsv_image, lower_range, upper_range)
    '''    
    mask_white = cv2.inRange(gray_image, 200, 255)
    
#    mask_bw = cv2.bitwise_or(mask_white, mask_black)
#    mask_bw_image = cv2.bitwise_and(gray_image, mask_bw)

    # 高斯降噪
    gauss_image1 = cv2.GaussianBlur(mask_white, (5, 5), 15)
#    gauss_image = cv2.GaussianBlur(mask_bw_image, (5, 5), 0)
    return gauss_image1


#改变探测区域
def region_of_interest(imgs, vertices):
    roi_mask = np.zeros_like(imgs)
    channel_count = 2
    match_maks_color = (255,) * channel_count
    cv2.fillPoly(roi_mask, vertices, match_maks_color)
    #cv2.fillPoly(roi_mask, vertices, 1)
    masked_image = cv2.bitwise_and(imgs, roi_mask)
    return masked_image


#检测边缘及线段
def find_edg_lines(img):
    # 检测边缘
    low_threshold = 100
    high_threshold = 200
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
    return lines, cannyed_edges


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


while True:
    #帧读取为图片
    ret, frame = cap.read()
    img = rotate(frame, angle)
    #图片处理
    image_color_gray = transfer_image(img)
    #得到线段
    lines, img_canny = find_edg_lines(image_color_gray)
    #改变探测区域
    image_roied = region_of_interest(img_canny, np.array([region_of_interest_vertices], np.int32))
    #绘制直线
    line_image = draw_lines(img, lines)
    #显示图像
    if line_image is not None:
        cv2.imshow("capture", image_roied)
    else:
        cv2.imshow("capture", img)
    
    if cv2.waitKey(1) & 0xFF == ord('`'):
        break
    
cap.release()
cv2.destroyAllWindows()

