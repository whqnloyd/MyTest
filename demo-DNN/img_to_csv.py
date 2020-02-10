import cv2
import pandas as pd
import numpy as np

path_pic = 'image/road.jpg'
width = 64*2
height = 48*2
raw_pic = cv2.resize(cv2.imread(path_pic, 1), (width, height))

def transfer_image_binary(img):
    w_b_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(w_b_image, (5, 5), 5)

    return image_blur

def region_of_interest(img):
    return img[int(height/3*1.5):int(height), :]

data3 = transfer_image_binary(raw_pic)
data3 = region_of_interest(data3)
data3 = np.array(data3) #change format to narray
print(data3)

while 1:
    cv2.imshow('pic', data3)

    if cv2.waitKey(1) & 0xFF == ord('`'):
        data3 = data3.reshape(1, -1)
        dataframe = pd.DataFrame(data3)
        print(dataframe)
        dataframe.to_csv('points_copy.csv', index=False, sep=',')
        print('saved to copy')
        break
cv2.destroyAllWindows()
