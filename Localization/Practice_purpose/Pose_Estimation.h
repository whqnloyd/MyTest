// Class Pose estimation is for estimating robot pose (x,y, theta)

#pragma once

#include "SAT_Const.h"
#include "SAT_VecMat.h"
//#include "StdAfx.h"

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

struct enc_data
{
	int v1,v2,v3,v4;	// encoder value 
	int t;				// time tick
};

struct GPS_data
{
	float x,y;		// x,y position from GPS
	int GPS_mode;	// GPS mode, if 5, DGPS mode, if 1, one GPS mode
	int sat_number;	// Satelite number, if larger, more reliable
	int t;			// time tick
};

struct Robot_Pose{
	double x;
	double y;
	double theta;
};

class Pose_Estimation
{

	Vector	X;		// robot state mean 3-d vector
	Matrix	P;		// robot state covariance 3x3 matrix

	float rho;


	long previous_e1;
	long previous_e2;
	long previous_e3;
	long previous_e4;

	long previous_v1;
	long previous_v2;
	long previous_v3;
	long previous_v4;

	// gps data x,y
	float previous_z[2];
	
	bool IsItFirstStep_Enc;
	bool IsItFirstStep_GPS;

public:
	
	Pose_Estimation(void);
	~Pose_Estimation(void);
	void Prediction_by_Odometry( enc_data enc_from_file );
	void Update_by_GPS( GPS_data gd );
	Robot_Pose Get_Robot_Pose();
	void Get_Robot_Covariance(Matrix& Cov);

};

