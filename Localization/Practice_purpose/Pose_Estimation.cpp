#include "stdafx.h"
#include "Pose_Estimation.h"
#include <cmath>


#include <iostream>  // for debugging
using namespace std ;

Pose_Estimation::Pose_Estimation(void)
{
	//X=VectorXd(0.0, 0.0, 0.0);	// robot state mean 
	X(0) = 0; X(1) = 0; X(2) = 0; 
	P=MatrixXd(3,3);				// robot state covariance
	P(0,0) = pow(INITIAL_POSE_ERROR,2); P(0,1) =0;  P(0,2) =0;
	P(1,0) =0; P(1,1) = pow(INITIAL_POSE_ERROR,2); P(1,2) =0;
	P(2,0) =0; P(2,1) =0; P(2,2) = pow(INITIAL_ANGLE_ERROR,2);
	
	
	previous_z[0]= 0;
	previous_z[1]= 0;

	previous_e1=0;
	previous_e2=0;
	previous_e3=0;
	previous_e4=0;

	previous_v1=0;
	previous_v2=0;
	previous_v3=0;
	previous_v4=0;
	
	rho = 0;

	IsItFirstStep_Enc = true;
	IsItFirstStep_GPS = true;

}

Pose_Estimation::~Pose_Estimation(void)
{
}

void Pose_Estimation::Prediction_by_Odometry( enc_data enc_from_file ){
	
	int e1;
	int e2;
	int e3;
	int e4;
	
	// first step:
	if ( IsItFirstStep_Enc ){
		e1 = 0;
		e2 = 0;
		e3 = 0;
		e4 = 0;
		IsItFirstStep_Enc = false;
		
	}
	else{

		e1 = enc_from_file.v1 - previous_v1;
		e2 = enc_from_file.v2 - previous_v2;
		e3 = enc_from_file.v3 - previous_v3;
		e4 = enc_from_file.v4 - previous_v4;
	}
	
	
	if ( abs(e1) > ENCODER_THSH ){
		e1 = previous_e1;
	}
	if ( abs(e2) > ENCODER_THSH ){
		e2 = previous_e2;
	}
	if ( abs(e3) > ENCODER_THSH ){
		e3 = previous_e3;
	}
	if ( abs(e4) > ENCODER_THSH ){
		e4 = previous_e1;
	}

	// Obtain wheel transverse distance
	int	re = e3;	// re: right wheel transverse distance
	int le = e1;	// le: left wheel transverse distance
	
	// prediction step
	rho = (W_R * re + W_L * le ) * 0.5 ;
	double omega = (W_R * re - W_L * le ) / WB ;
	double Phi = X(2) + 0.5 * omega;
	
	// mean prediction
	X(0) = X(0) + rho * cos(Phi);
	X(1) = X(1) + rho * sin(Phi);
	X(2) = X(2) + omega;
	
	// covariance prediction
	MatrixXd A(3,3); // jacobian wrt X

	A(0,0) = 1; A(1,1) = 1; A(2,2) = 1;
	A(0,1) = 0; A(1,0) = 0; A(2,0) = 0; A(2,1) = 0;
	A(0,2) = -rho * sin(Phi);
	A(1,2) = rho * cos(Phi);

// 	cout << "A" << endl;
// 	cout << A(0,0) << "\t"<< A(0,1) << "\t" << A(0,2) << endl;
// 	cout << A(1,0) << "\t"<< A(1,1) << "\t" << A(1,2) << endl;
// 	cout << A(2,0) << "\t"<< A(2,1) << "\t" << A(2,2) << endl;


	MatrixXd B(3,2);	// jacobian wrt U
	B(0,0) = cos(Phi);	B(0,1)= -0.5 * rho * sin(Phi);
	B(1,0) = sin(Phi);	B(1,1)= 0.5 * rho * cos(Phi);
	B(2,0) = 0;			B(2,1)= 1;
// 	
// 	cout << "B" << endl;
// 	cout << B(0,0) << "\t"<< B(0,1) << endl;
// 	cout << B(1,0) << "\t"<< B(1,1) << endl;
// 	cout << B(2,0) << "\t"<< B(2,1) << endl;

	MatrixXd Q(2,2);	// control noise
	Q(0,0) = pow(rho*SIGMA_RHO ,2);			Q(0,1) = 0;
	Q(1,0) = 0;								Q(1,1) = pow(omega * SIGMA_OMEGA ,2) ;
	
	// covariance prediction
	P = A*P*A.transpose()  +B*Q*B.transpose();

	previous_e1 = e1;
	previous_e2 = e2;
	previous_e3 = e3;
	previous_e4 = e4;
	previous_v1 = enc_from_file.v1;
	previous_v2 = enc_from_file.v2;
	previous_v3 = enc_from_file.v3;
	previous_v4 = enc_from_file.v4;

}

void Pose_Estimation::Update_by_GPS( GPS_data gd ){
	double sigma_gps;
	
	// covariance based on GPS mode
	if ( gd.GPS_mode == 5 ) {
		sigma_gps = SIGMA_GPS_MODE_5;
	}
	else{
		sigma_gps = SIGMA_GPS_MODE_1;
	}

	// local position is obtained by substracting gps offsest
	double z_x = gd.x - GPS_OFFSET_X; 
	double z_y = gd.y - GPS_OFFSET_Y;

	// 
	double delta_x;
	double delta_y;

	if ( IsItFirstStep_GPS ){
		delta_x = 0;
		delta_y = 0;
		IsItFirstStep_GPS = false;
	}else{
		delta_x = z_x - previous_z[0];
		delta_y = z_y - previous_z[1];
	}
	
	double z_theta = atan2( delta_y , delta_x );
	
	// moving in backward direction 
	if( rho < 0 ){
		z_theta = -z_theta;
	}
	
	// meansurement
	Vector3d z;
	z(0) = z_x; z(1) = z_y; z(2) = z_theta; 
	Vector3d z_hat(3);
	z_hat = X;

 	//cout << "z" << endl;
 	//cout << z(0) << "\t"<< z(1) << "\t" << z(2) << endl;


	MatrixXd H(3,3);
	H(0,1) = 0; H(0,2) =0; H(1,0) = 0; H(1,2) = 0; H(2,0) = 0; H(2,1) = 0;
	H(0,0) = 1.0; H (1,1) = 1.0; H(2,2) =1.0;


// 	cout << "H" << endl;
// 	cout << H(0,0) << "\t"<< H(0,1) << "\t" << H(0,2) << endl;
// 	cout << H(1,0) << "\t"<< H(1,1) << "\t" << H(1,2) << endl;
// 	cout << H(2,0) << "\t"<< H(2,1) << "\t" << H(2,2) << endl;

	MatrixXd R(3,3);
	R(0,1) = 0; R(0,2) =0; R(1,0) = 0; R(1,2) = 0; R(2,0) = 0; R(2,1) = 0;
	R(0,0) = pow(sigma_gps,2);
	R(1,1) = pow(sigma_gps,2);
	double temp=SIGMA_HEADING;
	R(2,2) = pow(temp,2);
	
// 	cout << "R" << endl;
// 	cout << R(0,0) << "\t"<< R(0,1) << "\t" << R(0,2) << endl;
// 	cout << R(1,0) << "\t"<< R(1,1) << "\t" << R(1,2) << endl;
// 	cout << R(2,0) << "\t"<< R(2,1) << "\t" << R(2,2) << endl;


	MatrixXd Psi(3,3);
	Psi = H*P*H.transpose()+R;

// 	cout << "Psi" << endl;
// 	cout << Psi(0,0) << "\t"<< Psi(0,1) << "\t" << Psi(0,2) << endl;
// 	cout << Psi(1,0) << "\t"<< Psi(1,1) << "\t" << Psi(1,2) << endl;
// 	cout << Psi(2,0) << "\t"<< Psi(2,1) << "\t" << Psi(2,2) << endl;


	MatrixXd K(3,3);
	K=P*H.transpose()*Psi.inverse();

// 	cout << "K" << endl;
// 	cout << K(0,0) << "\t"<< K(0,1) << "\t" << K(0,2) << endl;
// 	cout << K(1,0) << "\t"<< K(1,1) << "\t" << K(1,2) << endl;
// 	cout << K(2,0) << "\t"<< K(2,1) << "\t" << K(2,2) << endl;

	// 
	VectorXd delta_z(3);
	delta_z = z - z_hat ; // updated by JF 4/4/2015
	delta_z(2) = fmod( delta_z(2),2*PI);

	if (delta_z(2) > PI ){
		delta_z(2) = delta_z(2) - 2* PI;
	}
	
// 	cout << "delta_z" << endl;
// 	cout << delta_z(0) << "\t"<< delta_z(1) << "\t" << delta_z(2) << endl;

	// A posteriori state estimate
	X = X + K * ( delta_z );

// 	cout << "X" << endl;
// 	cout << X(0) << "\t"<< X(1) << "\t" << X(2) << endl;


	MatrixXd eye3(3,3);
	eye3(0,1) = eye3(0,2) =eye3(1,0) = eye3(1,2) = eye3(2,0) = eye3(2,1) = 	0;
	eye3(0,0) = eye3 (1,1) = eye3(2,2) =1.0;

	P = ( eye3 - K*H ) *P;

// 	cout << "P" << endl;
// 	cout << P(0,0) << "\t"<< P(0,1) << "\t" << P(0,2) << endl;
// 	cout << P(1,0) << "\t"<< P(1,1) << "\t" << P(1,2) << endl;
// 	cout << P(2,0) << "\t"<< P(2,1) << "\t" << P(2,2) << endl;


	// 
	previous_z[0] = z_x;
	previous_z[1] = z_y;


}

Robot_Pose Pose_Estimation::Get_Robot_Pose(){
	Robot_Pose temp;
	temp.x = X(0);
	temp.y = X(1);
	temp.theta = X(2);
	return temp;
};

void Pose_Estimation::Get_Robot_Covariance(MatrixXd & Cov){
	Cov = P;
	
}