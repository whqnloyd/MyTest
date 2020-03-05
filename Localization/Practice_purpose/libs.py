import numpy as np
import math

class GPS_Data:
    def __init__(self, data):
        self.t = data[0]
        self.x = data[1]
        self.y = data[2]
        self.gps_mode = data[3]
        self.sat_number = data[4]

class Enc_Data:
    def __init__(self, data):
        self.t = data[0]
        self.v1 = data[1]
        self.v2 = data[2]
        self.v3 = data[3]
        self.v4 = data[4]

class Robot_Pose:
    def __init__(self):
        self.x = 0.
        self.y = 0.
        self.theta = 0.

class Pose_Estimation:
    def __init__(self):
        self.INITIAL_POSE_ERROR = 0.
        self.INITIAL_ANGLE_ERROR = 0.
        self.ENCODER_THSH = 50000
        self.W_L = 6.5140e-6
        self.W_R = -6.5511e-6
        self.WB = 1.2
        self.SIGMA_RHO = 0.05
        self.SIGMA_OMEGA = 0.08
        self.SIGMA_GPS_MODE_5 = 0.05
        self.SIGMA_GPS_MODE_1 = 10.0
        self.GPS_OFFSET_X = 203841
        self.GPS_OFFSET_Y = 455456
        self.SIGMA_HEADING = 2

        self.x = np.array([0., 0., 0.])
        self.p = np.array([[pow(self.INITIAL_POSE_ERROR, 2), 0., 0.],
                           [0, pow(self.INITIAL_POSE_ERROR, 2), 0],
                           [0, 0, pow(self.INITIAL_ANGLE_ERROR, 2)]])

        self.previous_z = np.array([0, 0])

        self.previous_e1 = 0
        self.previous_e2 = 0
        self.previous_e3 = 0
        self.previous_e4 = 0

        self.previous_v1 = 0
        self.previous_v2 = 0
        self.previous_v3 = 0
        self.previous_v4 = 0

        self.rho = 0

        self.IsItFirstStep_Enc = True
        self.IsItFirstStep_GPS = True

    def Prediction_by_Odometry(self, enc_data):
        if self.IsItFirstStep_Enc:
            e1 = 0
            e2 = 0
            e3 = 0
            e4 = 0
            self.IsItFirstStep_Enc = False
        else:
            e1 = enc_data.v1 - self.previous_v1
            e2 = enc_data.v2 - self.previous_v2
            e3 = enc_data.v3 - self.previous_v3
            e4 = enc_data.v4 - self.previous_v4

        if abs(e1) > self.ENCODER_THSH:
            e1 = self.previous_e1
        if abs(e2) > self.ENCODER_THSH:
            e2 = self.previous_e2
        if abs(e3) > self.ENCODER_THSH:
            e3 = self.previous_e3
        if abs(e4) > self.ENCODER_THSH:
            e4 = self.previous_e1

        re = e3
        le = e1

        self.rho = (self.W_R * re + self.W_L * le) * 0.5
        omega = (self.W_R * re - self.W_L * le) / self.WB
        Phi = self.x[2] + 0.5*omega

        self.x[0] = self.x[0] + self.rho * math.cos(Phi)
        self.x[1] = self.x[1] + self.rho * math.sin(Phi)
        self.x[2] = self.x[2] + omega

        a = np.array([[1, 0, -self.rho * math.sin(Phi)],
                      [0, 1, self.rho * math.cos(Phi)],
                      [0, 0, 1]])
        b = np.array([[math.cos(Phi), -0.5 * self.rho * math.sin(Phi)],
                      [math.sin(Phi), 0.5 * self.rho * math.cos(Phi)],
                      [0, 1]])
        q = np.array([[pow(self.rho * self.SIGMA_RHO, 2), 0],
                      [0, pow(omega * self.SIGMA_OMEGA, 2)]])

        self.p = np.dot(np.dot(a, self.p), a.transpose()) + np.dot(np.dot(b, q), b.transpose())

        self.previous_e1 = e1
        self.previous_e2 = e2
        self.previous_e3 = e3
        self.previous_e4 = e4
        self.previous_v1 = enc_data.v1
        self.previous_v2 = enc_data.v2
        self.previous_v3 = enc_data.v3
        self.previous_v4 = enc_data.v4

    def Update_by_GPS(self, gps_data):
        if gps_data.gps_mode == 5:
            sigma_gps = self.SIGMA_GPS_MODE_5
        else:
            sigma_gps = self.SIGMA_GPS_MODE_1

        z_x = gps_data.x - self.GPS_OFFSET_X
        z_y = gps_data.y - self.GPS_OFFSET_Y

        if self.IsItFirstStep_GPS:
            delta_x = 0
            delta_y = 0
            self.IsItFirstStep_GPS = False
        else:
            delta_x = z_x - self.previous_z[0]
            delta_y = z_y - self.previous_z[1]

        z_theta = math.atan2(delta_y, delta_x)

        if self.rho < 0:
            z_theta = -z_theta

        z = np.array([z_x, z_y, z_theta])
        z_hat = self.x

        h = np.array([[1., 0, 0],
                      [0, 1., 0],
                      [0, 0, 1.]])

        r = np.array([[pow(sigma_gps, 2), 0, 0],
                      [0, pow(sigma_gps, 2), 0],
                      [0, 0, pow(self.SIGMA_HEADING, 2)]])

        psi = np.dot(np.dot(h, self.p), h.transpose()) + r

        k = np.dot(np.dot(self.p, h.transpose()), np.linalg.inv(psi))

        delta_z = z - z_hat
        delta_z[2] = math.fmod(delta_z[2], 2 * math.pi)

        if delta_z[2] > math.pi:
            delta_z[2] = delta_z[2] - 2 * math.pi

        self.x = self.x + np.dot(k, delta_z)

        eye3 = np.array([[1., 0, 0],
                         [0, 1., 0],
                         [0, 0, 1.]])

        self.p = np.dot((eye3 - np.dot(k, h)), self.p)

        self.previous_z[0] = z_x
        self.previous_z[1] = z_y

    def Get_Robot_Pose(self, robot_pose):
        robot_pose.x = self.x[0]
        robot_pose.y = self.x[1]
        robot_pose.theta = self.x[2]

    def Get_Robot_Covariance(self, p):
        p = np.copy(self.p)
