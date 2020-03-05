from libs import *
# from matplotlib import pyplot as plt
import cv2

file_gps = "D:\\MyTest\Localization\\Practice_purpose\\Data_Encoder\\20120229_180327_GPS.txt"
file_encoder = "D:\\MyTest\\Localization\\Practice_purpose\\Data_Encoder\\20120229_180327_Wheel.txt"

gps_d = []
with open(file_gps, 'r') as f:
    for line in f.readlines():
        temp = line.split()
        temp_n = list(map(float, temp))
        a = GPS_Data(temp_n)
        gps_d.append(a)

enc_d = []
with open(file_encoder, 'r') as f:
    element = []
    for line in f.readlines():
        temp = line.split()
        temp_n = list(map(float, temp))
        a = Enc_Data(temp_n)
        enc_d.append(a)

index = 0
while gps_d[index].t < enc_d[0].t:
    index += 1

pe = Pose_Estimation()
rp = Robot_Pose()
p = np.zeros((3, 3))

path = []
couter = 0
for i in enc_d:
    couter += 1
    pe.Get_Robot_Covariance(p)
    pe.Prediction_by_Odometry(i)

    if gps_d[index].t < i.t:
        pe.Update_by_GPS(gps_d[index])
        index += 1

    pe.Get_Robot_Pose(rp)
    pe.Get_Robot_Covariance(p)

    if couter == 20:
        couter = 0
        path.append([rp.x, rp.y, rp.theta])
        # print(rp.x, rp.y, rp.theta)
path = np.transpose(path)

map = np.ones((int(max(abs(path[1]*20))+200), int(max(abs(path[0]*20))+200)))*255
print(map.shape)
path = np.transpose(path)
for i in path:
    cv2.circle(map, (int(i[0]*20 + 100), int(-i[1]*20 + 100)), 3, 0)
    next_point = (int(i[0]*20 + 100 + math.cos(i[2])*50), int(-i[1]*20 + 100 - math.sin(i[2])*50))
    cv2.arrowedLine(map, (int(i[0]*20 + 100), int(-i[1]*20 + 100)), next_point, 0.8)
    cv2.imshow('map', map)
    cv2.waitKey(100)
cv2.waitKey(0)
# plt.figure(1)
# plt.plot(path[0], path[1])
# plt.show()
