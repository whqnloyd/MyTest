#include "MyCamera.h"

MyCamera::MyCamera(YAML::Node cam)
{
	//load image solution and roi
	for (int i = 0; i < 2; i++)
	{
		size[i] = cam["ImageSize"][i].as<int>();
		ROI[i] = cam["ROI"][i].as<double>();
	}
	//load rotation in degree (x, y, z)
	for (int i = 0; i < 3; i++) 
	{ 
		RotationDegree[i] = cam["Transformation"]["Rotation"][i].as<double>(); 
		Translation[i] = cam["Transformation"]["Translation"][i].as<double>();
	}
	//load camera intrinsic matrix
	for (int r = 0; r < 3; r++)
	{
		for (int c = 0; c < 3; c++){ CameraMat(r, c) = cam["CameraMat"][r][c].as<double>(); }
	}
	//load camera distortion parameters, the calibration method from ROS only offer 5 parameters
	for (int i = 0; i < 5; i++)
	{
		DistCoff[i] = cam["Transformation"]["DistCoeff"][i].as<double>();
	}
	
	UpdateRotationMatrix(RotationDegree);
	UpdateTransformationMatrix(RotationMatrix, Translation);
}

MyCamera::~MyCamera(){}

void MyCamera::UpdateRotationMatrix(Eigen::Vector3d RotationDegree)
{
	RotationMatrix = Euler2RotationMatrix(RotationDegree);
}

void MyCamera::UpdateTransformationMatrix(Eigen::MatrixXd RotationMatrix, Eigen::Vector3d Translation)
{
	TransformationAll << RotationMatrix, Translation;
}