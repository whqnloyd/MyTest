#pragma once
#include <Eigen/Dense>
#include "Tools.h"

#define PI 3.14159265358979323846
#define ENCODER_THSH 50000	// 
#define W_L 6.5140e-6	    // encoder_value * alpha_r = right_wheel_movement(m)
#define W_R -6.5511e-6	    // encoder_value * alpha_l = left_wheel_movement(m)
#define WB 1.20		        // kinematic model parameter for rotation 
#define SIGMA_RHO 0.05		// Update process convariance
#define SIGMA_OMEGA 0.08	// Update process convariance
#define SIGMA_GPS_MODE_5 0.05		// update measurement covariance with DGPS mode 0.05(m)
#define SIGMA_GPS_MODE_1 10.0		// update measurement covariance with GPS mode 10(m)
#define SIGMA_HEADING 2		        // heading covariance update
#define GPS_OFFSET_Y 455456         // GPS offset in y direction
#define GPS_OFFSET_X 203841         // GPS offset in x direction
#define INITIAL_POSE_ERROR 1000.0   // Initial pose error 
#define INITIAL_ANGLE_ERROR 10.0    // Initial pose error 

class Estimator
{
public:
	Estimator();
	~Estimator(){};

	Eigen::Vector3d X_enc;
	Eigen::Vector3d X_gps;
	Eigen::MatrixXd P;
	RobotPose robotpose;

	bool IsItFirstStep_Enc;
	bool IsItFirstStep_GPS;

	void Prediction_by_ENC(Encoder enc);
	void Update_by_GPS(GPS g);

	int pre_delta_1;
	int pre_delta_2;
	int pre_delta_3;
	int pre_delta_4;

	int pre_v1;
	int pre_v2;
	int pre_v3;
	int pre_v4;

	double pre_x;
	double pre_y;
};