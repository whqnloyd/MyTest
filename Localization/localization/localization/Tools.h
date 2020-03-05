#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>


struct GPS{
	int time, gps_mode, sat_num;
	double x, y;
};

struct Encoder{
	int v1, v2, v3, v4, time;
};

struct RobotPose{
	double x, y, theta, v, w;
};

class GPSreader
{
public:
	GPSreader(std::string file);
	~GPSreader(){};

	std::string file_path;
	std::vector<GPS> data;

	void UpdateGPS(std::string file);
};

class ENCreader
{
public:
	ENCreader(std::string file);
	~ENCreader(){};

	std::string file_path;
	std::vector<Encoder> data;

	void UpdateENC(std::string file);
};

void DrawPose(cv::Mat image, RobotPose pose);