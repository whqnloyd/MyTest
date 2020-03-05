#include "Tools.h"
#include "Estimator.h"

int main()
{
	std::string gps_path = "D:\\MyTest\\Localization\\localization\\x64\\Release\\data\\20120229_180327_GPS.txt";
	std::string enc_path = "D:\\MyTest\\Localization\\localization\\x64\\Release\\data\\20120229_180327_Wheel.txt";

	GPSreader gps(gps_path);
	ENCreader encoder(enc_path);

	cv::Mat image(640, 480, CV_8UC1, cv::Scalar(255));

	int j = 0;
	while (gps.data[j].time < encoder.data[0].time) j++;

	Estimator estimate;
	RobotPose robot_pose;

	for (int i = 0; i < encoder.data.size(); i++)
	{
		estimate.Prediction_by_ENC(encoder.data[i]);
		if (gps.data[j].time < encoder.data[i].time)
		{
			estimate.Update_by_GPS(gps.data[j]);
			j++;
		}
		
		robot_pose = estimate.robotpose;
		if (i % 10 == 0)
		{
			DrawPose(image, robot_pose);
		}
	}

	cv::waitKey();
	return 0;
}
