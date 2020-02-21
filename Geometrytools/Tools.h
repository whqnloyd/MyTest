#pragma once
#include <Eigen/Core.h>
#include <Eigen/Geometry>
#include <cmath>

#ifndef _USE_MATH_DEFINES
#define _USE_MATH_DEFINES
#endif

//useful tools
#define DegreesToRadians(angleDegrees) ((angleDegrees) * M_PI / 180.0)
#define RadiansToDegrees(angleRadians) ((angleRadians) * 180.0 / M_PI)
#define ReverseAngleDegree(angle) (angle = (angle >= 0) ? (angle - 180) : (angle + 180))

Eigen::MatrixXd Euler2RotationMatrix(Eigen::Vector3d rpy);
Eigen::Vector3d RotationMatrix2euler(Eigen::MatrixXd R);