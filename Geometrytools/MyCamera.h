#pragma once
#include <Eigen/Core.h>
#include <Eigen/Geometry>
#include <iostream>
#include <string>
#include <yaml-cpp/yaml.h>
#include <stdio.h>
#include "Tools.h"

#ifndef YAML_CPP_DLL
#define YAML_CPP_DLL
#endif

class MyCamera
{
public:
	MyCamera(YAML::Node cam);
	~MyCamera();

	//data
	Eigen::Vector2d size;
	Eigen::Vector2d ROI;
	Eigen::Vector3d RotationDegree;
	Eigen::Vector3d Translation;
	Eigen::MatrixXd CameraMat = Eigen::MatrixXd::Zero(3, 3);
	Eigen::VectorXd DistCoff = Eigen::VectorXd::Zero(5);
	Eigen::MatrixXd RotationMatrix = Eigen::MatrixXd::Zero(3, 3);
	Eigen::MatrixXd TransformationAll = Eigen::MatrixXd::Zero(3, 4);

	//function
	void UpdateRotationMatrix(Eigen::Vector3d RotationDegree);
	void UpdateTransformationMatrix(Eigen::MatrixXd RotationMatrix, Eigen::Vector3d Translation);
};