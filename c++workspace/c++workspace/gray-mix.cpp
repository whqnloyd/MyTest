#include <opencv2/opencv.hpp>

using namespace cv;

void GrayDepthSeperate() {
	std::vector<Mat> channels;
	const char* filename = "D:\\LR-Projects\\volo\\data\\img\\1.png";

	Mat* mat_ptr = new cv::Mat();
	Mat& mat = *mat_ptr;
	mat = cv::imread(filename);
	Mat mat_changed;

	split(mat, channels);
	channels.pop_back();
	imshow("img1", channels[0]);
	imshow("img2", channels[1]);
	//merge(channels, mat_changed);
	waitKey(0);
}
