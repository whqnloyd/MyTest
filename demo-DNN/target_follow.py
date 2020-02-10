import cv2
import numpy as np

cap = cv2.VideoCapture(0)
template = cv2.imread('image/test_target.jpg', 0)

w, h = template.shape[::-1]
# first 2 are good for color change, and next 2 are good for distort
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
methods = ['cv2.TM_CCOEFF_NORMED']
method = eval(methods[0])

while True:
    ret1, img_0 = cap.read()
    img_1 = cv2.cvtColor(img_0, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_1, template, method)

    threshold = 0.5
    thresh_loc = np.where(res >= threshold)
    loc_x = np.median(thresh_loc[::-1][0])
    loc_y = np.median(thresh_loc[::-1][1])
    if loc_x > 0 and loc_y > 0:
        cv2.rectangle(img_0, (int(loc_x), int(loc_y)), (int(loc_x + w), int(loc_y + h)), (0, 0, 255), 2)
        print('x: %.2f, y: %.2f' % (loc_x, loc_y))

    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #     top_left = min_loc
    # else:
    #     top_left = max_loc
    # bottom_right = (top_left[0] + w, top_left[1] + h)
    # target_img = img_1[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    # cv2.rectangle(img_0, top_left, bottom_right, 255, 2)

    # for pt in zip(*thresh_loc[::-1]):
    #     cv2.rectangle(img_0, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imshow('result', img_0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
