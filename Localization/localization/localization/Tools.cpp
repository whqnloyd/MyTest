#include "Tools.h"

GPSreader::GPSreader(std::string file){
	file_path = file;
	UpdateGPS(file_path);
}

void GPSreader::UpdateGPS(std::string file)
{
	GPS gps_temp;
	std::ifstream f_gps(file);
	while (1)
	{
		if (f_gps.eof()) break;
		f_gps >> gps_temp.time >> gps_temp.x >> gps_temp.y >> gps_temp.gps_mode >> gps_temp.sat_num;
		data.push_back(gps_temp);
	}
}

ENCreader::ENCreader(std::string file)
{
	file_path = file;
	UpdateENC(file_path);
}

void ENCreader::UpdateENC(std::string file)
{
	Encoder enc_temp;
	std::ifstream f_enc(file);
	while (1)
	{
		if (f_enc.eof()) break;
		f_enc >> enc_temp.time >> enc_temp.v1 >> enc_temp.v2 >> enc_temp.v3 >> enc_temp.v4;
		data.push_back(enc_temp);
	}
}

void DrawPose(cv::Mat image, RobotPose pose)
{
	int mut = 20;
	cv::Point center(pose.x*mut, -pose.y*mut);
	cv::Point shift(50, 50);
	center = center + shift;

	cv::Scalar color(0, 0, 255);
	cv::circle(image, center, 2, color);

	cv::Point c2(center.x + cos(pose.theta) * 25, center.y - sin(pose.theta) * 25);
	cv::arrowedLine(image, center, c2, color);

	cv::imshow("test", image);
	cv::waitKey(3);
}