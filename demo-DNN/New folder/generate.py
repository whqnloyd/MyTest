import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path_pic = 'data/3.jpg'
width = 640
height = 480

raw_pic = cv2.resize(cv2.imread(path_pic, 1), (width, height))
raw_pic_2 = cv2.resize(cv2.imread(path_pic, 1), (width, height))

def transfer_image_HSV(img):
    if img is None:
        return

    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    grass_lower_range = np.array([0, 20, 70], dtype='uint8')
    grass_upper_range = np.array([40, 125, 160], dtype='uint8')
    grass_hsv_range = cv2.bitwise_not(cv2.inRange(hsv_image, grass_lower_range, grass_upper_range))

    road_lower_range = np.array([0, 0, 50], dtype='uint8')
    road_upper_range = np.array([180, 40, 150], dtype='uint8')
    road_hsv_range = cv2.inRange(hsv_image, road_lower_range, road_upper_range)

    hsv_image_mix = cv2.bitwise_and(grass_hsv_range, road_hsv_range)

    and_image_blur = cv2.GaussianBlur(hsv_image_mix, (13, 13), 2.3, 2.3)

    return grass_hsv_range, road_hsv_range, hsv_image_mix, and_image_blur

def find_edg(img):
    if img is None:
        return

    low_threshold = 150
    high_threshold = 450
    cannyed_edges = cv2.Canny(img, low_threshold, high_threshold)

    return cannyed_edges

def get_pos(canny_img):
    if canny_img is None:
        return

    points = []
    y = 1
    for i in canny_img:
        y = y + 1
        x = 1
        for j in i:
            if j != 0:
                points.append((x, y))
            x = x + 1

    return points

grass_image, road_image, mix_image, and_image = transfer_image_HSV(raw_pic)

# plt.figure(1)
# plt.subplot(1, 2, 1)
# plt.title('RGB')
# raw_pic_0 = cv2.cvtColor(raw_pic, cv2.COLOR_BGR2RGB)
# plt.imshow(raw_pic_0)
# plt.axis('off')
#
# plt.subplot(1, 2, 2)
# hsv_image = cv2.cvtColor(raw_pic, cv2.COLOR_BGR2HSV)
# plt.title('HSV')
# plt.imshow(hsv_image)
# plt.axis('off')

plt.subplot(1, 2, 1)
plt.title('Binary map for grass')
grass_hsv_image = cv2.cvtColor(grass_image, cv2.COLOR_GRAY2RGB)
plt.imshow(grass_hsv_image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Binary map for road')
road_hsv_image = cv2.cvtColor(road_image, cv2.COLOR_GRAY2RGB)
plt.imshow(road_hsv_image)
plt.axis('off')

# plt.subplot(1, 1, 1)
# plt.figure(1)
# plt.title('Bit addition')
# hsv_mix_image = cv2.cvtColor(mix_image, cv2.COLOR_GRAY2RGB)
# plt.imshow(hsv_mix_image)
# plt.axis('off')
# # #
# # plt.subplot(1, 1, 1)
# plt.figure(2)
# plt.title('Gaussian blur')
# and_image = cv2.cvtColor(and_image, cv2.COLOR_GRAY2RGB)
# plt.imshow(and_image)
# plt.axis('off')

# plt.subplot(2, 3, 6)
# plt.title('edg_points')
# edg_points = cv2.cvtColor(edg_points, cv2.COLOR_GRAY2RGB)
# plt.imshow(edg_points)
#
plt.show()

while 1:
    grass_image, road_image, mix_image, and_image = transfer_image_HSV(raw_pic)
    edg_points = find_edg(and_image)
    points = get_pos(edg_points)
    m = np.array(points)
    # m1 = m[0::4]
    m1 = m[0::4]

    for n in points:
        cv2.imshow('points', cv2.circle(raw_pic_2, n, 1, (255, 0, 0)))

    # cv2.imshow('raw', raw_pic)
    # #cv2.imshow('gray', gray_image)
    # cv2.imshow('grass', grass_image)
    # cv2.imshow('road', road_image)
    # cv2.imshow('mix_image', mix_image)
    # cv2.imshow('and', and_image)
    cv2.imshow('edg_points', edg_points)

    # plt.figure(1)
    # plt.subplot(1, 2, 1)
    # plt.title('Edge points')
    # edg_points = cv2.cvtColor(edg_points, cv2.COLOR_GRAY2RGB)
    # plt.imshow(edg_points)
    # # plt.gca().invert_yaxis()
    # plt.xlabel('x position')
    # plt.ylabel('y position')
    # plt.subplot(1, 2, 2)
    # plt.title('Raw image with edge points')
    # raw_pic_0 = cv2.cvtColor(raw_pic_2, cv2.COLOR_BGR2RGB)
    # plt.imshow(raw_pic_0)
    # # plt.gca().invert_yaxis()
    # plt.xlabel('x position')
    # plt.show()

    if cv2.waitKey(1) & 0xFF == ord('`'):
        dataframe = pd.DataFrame({'x': m1[0:, 0], 'y': m1[0:, 1]})
        dataframe.to_csv('points_copy.csv', index=False, sep=',')
        print('saved to copy')
        break

cv2.destroyAllWindows()
