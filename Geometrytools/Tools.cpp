#include "Tools.h"

//flags
bool REVERSE_ANGLE;
//bool SPECIAL90D;

Eigen::MatrixXd Euler2RotationMatrix(Eigen::Vector3d rpy)
{
	REVERSE_ANGLE = (rpy[1] > 90.);
	//SPECIAL90D = (fmod(rpy[1], 90) == 0.);
	rpy = DegreesToRadians(rpy);

	Eigen::AngleAxisd pitchAngle(rpy[0], Eigen::Vector3d::UnitX());
	Eigen::AngleAxisd yawAngle(rpy[1], Eigen::Vector3d::UnitY());
	Eigen::AngleAxisd rollAngle(rpy[2], Eigen::Vector3d::UnitZ());

	Eigen::Quaterniond q = pitchAngle * yawAngle * rollAngle;
	Eigen::MatrixXd R = q.matrix();

	return R;
}

Eigen::Vector3d RotationMatrix2euler(Eigen::MatrixXd Rr)
{
	Eigen::MatrixXd R = Rr.transpose();
	double sy = sqrt(R(0, 0) * R(0, 0) + R(1, 0) * R(1, 0));
	bool singular = sy < 1e-6;
	double x, y, z;
	if (!singular) {
		x = atan2(R(2, 1), R(2, 2));
		y = atan2(-R(2, 0), sy);
		z = atan2(R(1, 0), R(0, 0));
	}
	else {
		x = atan2(R(1, 2), R(1, 1));
		y = atan2(R(2, 0), sy);
		z = 0;
	}

	x = RadiansToDegrees(x);
	y = RadiansToDegrees(y);
	z = RadiansToDegrees(z);
	Eigen::Vector3d euler(-x, -y, -z);
	if (REVERSE_ANGLE)
	{
		euler[0] = ReverseAngleDegree(euler[0]);
		euler[1] = -ReverseAngleDegree(euler[1]);
		euler[2] = ReverseAngleDegree(euler[2]);
	}
	//euler = (SPECIAL90D) ? (-euler) : (euler);

	return euler;
}