import cv2
import numpy as np
import math

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
    if image_roied is None:
        return
    
    # GRAY处理，HSV处理
    gray_image = cv2.cvtColor(image_roied, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(image_roied, cv2.COLOR_BGR2HSV)

    #hsv
    lower_black = np.array([0, 0, 0], dtype='uint8')
    upper_black = np.array([180, 60, 130], dtype='uint8')
    hsv_black = cv2.inRange(hsv_image, lower_black, upper_black)
    
    #gray
    gray_black = cv2.inRange(gray_image, 15, 125)
    
    mask_image = cv2.bitwise_and(hsv_black, gray_black)

    # 高斯降噪
    gauss_image = cv2.GaussianBlur(mask_image, (5, 5), 3)

    return gauss_image


#改变探测区域
def region_of_interest(imgs, vertices):
    
    roi_mask = np.zeros_like(imgs)
    channel_count = 2
    match_maks_color = (255,) * channel_count
    
    cv2.fillPoly(roi_mask, vertices, match_maks_color)
    
    masked_image = cv2.bitwise_and(imgs, roi_mask)
    return masked_image


#检测边缘
def find_edg(img):
    if img is None:
        return
    
    # 检测边缘
    low_threshold = 100
    high_threshold = 200
    cannyed_edges = cv2.Canny(img, low_threshold, high_threshold)
    
    return cannyed_edges

#find the lines
def find_lines(img):
    if img is None:
        return
    
    # 霍夫变换，找到边缘对应的直线段
    lines = cv2.HoughLinesP(
        img,
        rho=6,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25
    )
    
    return lines

#fine line
def lines_fine(image, lines_):
        if lines_ is None:
            return
    
        left_line_x = []
        left_line_y = []
        right_line_x = []
        right_line_y = []
        
        for line in lines_:
            for x1, y1, x2, y2 in line:
                if ((x2-x1) != 0):
                    slope = (y2 - y1) / (x2 - x1)
                    if math.fabs(slope) < 0.5:
                        continue
                    elif slope < 0:
                        left_line_x.extend([x1, x2])
                        left_line_y.extend([y1, y2])
                    elif slope > 0:
                        right_line_x.extend([x1, x2])
                        right_line_y.extend([y1, y2])
                else: continue
        
        if (left_line_y is None) or (right_line_y is None):
            return
        
        #y position
        min_y = int(image.shape[0] * (65/100))
        max_y = int(image.shape[0] * (100/100))
        
        #x position
        poly_left = np.poly1d(np.polyfit(
                left_line_y,
                left_line_x,
                deg = 1
            ))
        
        left_x_start = int(poly_left(max_y))
        left_x_end = int(poly_left(min_y))
        
        poly_right = np.poly1d(np.polyfit(
                right_line_y,
                right_line_x,
                deg = 1
            ))
        
        right_x_start = int(poly_right(max_y))
        right_x_end = int(poly_right(min_y))
        
        #mid line
        mid_line_start_x = int((left_x_start + right_x_start)/2)
        mid_line_start_y = max_y - 20
        mid_line_end_x = int((left_x_end + right_x_end)/2)
        mid_line_end_y = min_y + 20
        
        mid_line = [[mid_line_start_x,
                     mid_line_start_y,
                     mid_line_end_x,
                     mid_line_end_y]]
        
        fix_line = [[int(image.shape[1]/2),
                     mid_line_end_y+20,
                     int(image.shape[1]/2),
                     mid_line_start_y-20]]
        
        edge_line = [
                [left_x_start, max_y, left_x_end, min_y],
                [right_x_start, max_y, right_x_end, min_y],
            ]
        
        return fix_line, edge_line, mid_line
      
def mid_line_anal(line_):
    if line_ is None:
        return
    
    #for x1, y1, x2, y2 in line_:
        
#绘制直线
def draw_lines(images, lines_, color=[255, 0, 0], thickness=3):
    if lines_ is None:
        return
    
    img = np.copy(images)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8, )
    for x1, y1, x2, y2 in lines_:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    return img


while True:
    #帧读取为图片
    ret, frame = cap.read()
    img = rotate(frame, angle)
    #图片处理
    image_color_gray = transfer_image(img)
    #得到线段value
    img_canny = find_edg(image_color_gray)
    #改变探测区域
    image_roied = region_of_interest(img_canny, np.array([region_of_interest_vertices], np.int32))
    #find lines
    lines = find_lines(image_roied)
    #find two lines
    fix_line, edge_lines, mid_line = lines_fine(img, lines)
    #find instruction line
    #instruction_line = intruct_line()
    #
    edge_image = draw_lines(img, edge_lines)
    mid_image = draw_lines(edge_image, mid_line, [0, 255, 0])
    fix_image = draw_lines(mid_image, fix_line, [0, 0, 255])
    #显示图像
    if fix_image is not None:
        cv2.imshow("capture", fix_image)
    else:
        cv2.imshow("capture", img)
    
    if cv2.waitKey(1) & 0xFF == ord('`'):
        break
    
cap.release()
cv2.destroyAllWindows()

