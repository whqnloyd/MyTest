#include "Estimator.h"

Estimator::Estimator()
{
	X_enc = { 0, 0, 0 };
	X_gps = { 0, 0, 0 };

	P = Eigen::MatrixXd(3, 3);
	P(0, 0) = pow(INITIAL_POSE_ERROR, 2); P(0, 1) = 0;  P(0, 2) = 0;
	P(1, 0) = 0; P(1, 1) = pow(INITIAL_POSE_ERROR, 2); P(1, 2) = 0;
	P(2, 0) = 0; P(2, 1) = 0; P(2, 2) = pow(INITIAL_ANGLE_ERROR, 2);

	robotpose = { 0, 0, 0, 0, 0};

	IsItFirstStep_Enc = true;
	IsItFirstStep_GPS = true;

	pre_delta_1 = 0;
	pre_delta_2 = 0;
	pre_delta_3 = 0;
	pre_delta_4 = 0;

	pre_v1 = 0;
	pre_v2 = 0;
	pre_v3 = 0;
	pre_v4 = 0;

	pre_x = 0;
	pre_y = 0;
}

void Estimator::Prediction_by_ENC(Encoder enc)
{
	int delta_1, delta_2, delta_3, delta_4;
	double delta_theta;

	if (IsItFirstStep_Enc)
	{
		delta_1 = delta_2 = delta_3 = delta_4 = 0;
		IsItFirstStep_Enc = false;
	}
	else
	{
		delta_1 = enc.v1 - pre_v1;
		delta_2 = enc.v2 - pre_v2;
		delta_3 = enc.v3 - pre_v3;
		delta_4 = enc.v4 - pre_v4;
	}

	if (abs(delta_1) > ENCODER_THSH){
		delta_1 = pre_delta_1;
	}
	if (abs(delta_2) > ENCODER_THSH){
		delta_2 = pre_delta_2;
	}
	if (abs(delta_3) > ENCODER_THSH){
		delta_3 = pre_delta_3;
	}
	if (abs(delta_4) > ENCODER_THSH){
		delta_4 = pre_delta_1;
	}

	// obtain transverse distance for re: right wheel and le: left wheel
	int	re = delta_3;
	int le = delta_1;

	// caculate angle, linear and angular velocity
	robotpose.v = (W_R * re + W_L * le) * 0.5;
	robotpose.w = (W_R * re - W_L * le) / WB;
	delta_theta = X_enc(2) + 0.5 * robotpose.w;

	// X[x, y, angle]
	X_enc(0) = X_enc(0) + robotpose.v * cos(delta_theta);
	X_enc(1) = X_enc(1) + robotpose.v * sin(delta_theta);
	X_enc(2) = X_enc(2) + robotpose.w;

	////////////////////////////////////////////////////////////////////////////
	// jacobian wrt X
	Eigen::MatrixXd A(3, 3); 
	A(0, 0) = 1; A(0, 1) = 0; A(0, 2) = -robotpose.v * sin(delta_theta);
	A(1, 0) = 0; A(1, 1) = 1; A(1, 2) = robotpose.v * cos(delta_theta);
	A(2, 0) = 0; A(2, 1) = 0; A(2, 2) = 1;
	
	// jacobian wrt U
	Eigen::MatrixXd B(3, 2);	
	B(0, 0) = cos(delta_theta);	B(0, 1) = -0.5 * robotpose.v * sin(delta_theta);
	B(1, 0) = sin(delta_theta);	B(1, 1) = 0.5 * robotpose.v * cos(delta_theta);
	B(2, 0) = 0; B(2, 1) = 1;

	// control noise
	Eigen::MatrixXd Q(2, 2);	
	Q(0, 0) = pow(robotpose.v * SIGMA_RHO, 2); Q(0, 1) = 0;
	Q(1, 0) = 0; Q(1, 1) = pow(robotpose.w * SIGMA_OMEGA, 2);

	// covariance prediction
	P = A*P*A.transpose() + B*Q*B.transpose();

	pre_delta_1 = delta_1;
	pre_delta_2 = delta_2;
	pre_delta_3 = delta_3;
	pre_delta_4 = delta_4;
	pre_v1 = enc.v1;
	pre_v2 = enc.v2;
	pre_v3 = enc.v3;
	pre_v4 = enc.v4;

	// update information to robot
	robotpose.x = X_enc(0);
	robotpose.y = X_enc(1);
	robotpose.theta = X_enc(2);
}

void Estimator::Update_by_GPS(GPS g){
	double sigma_gps;
	if (g.gps_mode == 5) {
		sigma_gps = SIGMA_GPS_MODE_5;
	}
	else{
		sigma_gps = SIGMA_GPS_MODE_1;
	}

	// local position is obtained by substracting gps offsest
	double x = g.x - GPS_OFFSET_X;
	double y = g.y - GPS_OFFSET_Y;

	double delta_x;
	double delta_y;

	if (IsItFirstStep_GPS){
		delta_x = 0;
		delta_y = 0;
		IsItFirstStep_GPS = false;
	}
	else{
		delta_x = x - pre_x;
		delta_y = y - pre_y;
	}

	double angle = atan2(delta_y, delta_x);

	// moving in backward direction 
	if (robotpose.v < 0){
		angle = -angle;
	}

	// meansurement
	X_gps = { x, y, angle };

	/////////////////////////////////////////////////////////////////////////////
	Eigen::MatrixXd H(3, 3);
	H(0, 0) = 1.0; H(0, 1) = 0; H(0, 2) = 0;
	H(1, 0) = 0; H(1, 1) = 1.0; H(1, 2) = 0;
	H(2, 0) = 0; H(2, 1) = 0; H(2, 2) = 1.0;

	Eigen::MatrixXd R(3, 3);
	R(0, 0) = pow(sigma_gps, 2); R(0, 1) = 0; R(0, 2) = 0; 
	R(1, 0) = 0; R(1, 1) = pow(sigma_gps, 2); R(1, 2) = 0; 
	R(2, 0) = 0; R(2, 1) = 0; R(2, 2) = pow(SIGMA_HEADING, 2);

	Eigen::MatrixXd Psi(3, 3);
	Psi = H*P*H.transpose() + R;

	Eigen::MatrixXd K(3, 3);
	K = P*H.transpose()*Psi.inverse();

	Eigen::MatrixXd eye3(3, 3);
	eye3(0, 1) = eye3(0, 2) = eye3(1, 0) = eye3(1, 2) = eye3(2, 0) = eye3(2, 1) = 0;
	eye3(0, 0) = eye3(1, 1) = eye3(2, 2) = 1.0;

	// Update P and X_enc by GPS information
	Eigen::VectorXd delta_z(3);
	delta_z = X_gps - X_enc;
	delta_z(2) = fmod(delta_z(2), 2 * PI);

	if (delta_z(2) > PI){
		delta_z(2) = delta_z(2) - 2 * PI;
	}

	X_enc = X_enc + K * (delta_z);			// A posteriori state estimate

	P = (eye3 - K*H) *P;

	pre_x = x;
	pre_y = y;

	// update information to robot
	robotpose.x = X_enc(0);
	robotpose.y = X_enc(1);
	robotpose.theta = X_enc(2);
}