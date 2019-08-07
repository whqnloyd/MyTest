#include <opencv2/opencv.hpp>

using namespace cv;

void main() {
	std::vector<Mat> channels;
	const char* filename = "D:\\LR-Projects\\volo\\data\\img\\1.png";

	Mat* mat_ptr = new cv::Mat();
	Mat& mat = *mat_ptr;
	mat = cv::imread(filename);
	Mat mat_changed;
	//int sz[] = { mat.rows, mat.cols, 2 };
	//Mat mat_changed(3, sz, CV_32F, Scalar::all(0));

	split(mat, channels);
	channels.pop_back();
	//imshow("img1", channels[0]);
	//imshow("img2", channels[1]);
	merge(channels, mat_changed);
	waitKey(0);

	//for (int c = 0; c < 2; c++) {
	//	for (int h = 0; h < mat.rows; h++) {
	//		for (int w = 0; w < mat.cols; w++) {
	//			int dst_index = w + mat.cols * h + mat.cols * mat.rows * c;
	//			int src_index = c + 2 * w + 2 * mat.cols * h;
	//			mat_changed.ptr<float>(dst_index) = mat.ptr<float>(src_index);
	//		}
	//	}
	//}
}
		
//if (mat.channels() == 3) cv::cvtColor(mat, mat, cv::COLOR_RGB2BGR);
//else if (mat.channels() == 4) cv::cvtColor(mat, mat, cv::COLOR_RGBA2BGRA);

// ----------------------------------------

//cv::Mat load_image_mat(char* filename, int channels)
//{
//	int flag = cv::IMREAD_UNCHANGED;
//	if (channels == 0) flag = cv::IMREAD_COLOR;
//	else if (channels == 1) flag = cv::IMREAD_GRAYSCALE;
//	else if (channels == 3) flag = cv::IMREAD_COLOR;
//	else {
//		fprintf(stderr, "OpenCV can't force load with %d channels\n", channels);
//	}
//	//flag |= IMREAD_IGNORE_ORIENTATION;    // un-comment it if you want
//
//	cv::Mat* mat_ptr = (cv::Mat*)load_image_mat_cv(filename, flag);
//
//	if (mat_ptr == NULL) {
//		return cv::Mat();
//	}
//	cv::Mat mat = *mat_ptr;
//	delete mat_ptr;
//
//	return mat;
//}
//
//image load_image_cv(char* filename, int channels)
//{
//	cv::Mat mat = load_image_mat(filename, channels);
//
//	if (mat.empty()) {
//		return make_image(10, 10, channels);
//	}
//	return mat_to_image(mat);
//}
//// ----------------------------------------
//
//image load_image_resize(char* filename, int w, int h, int c, image* im)
//{
//	image out;
//	try {
//		cv::Mat loaded_image = load_image_mat(filename, c);
//
//		*im = mat_to_image(loaded_image);
//
//		cv::Mat resized(h, w, CV_8UC3);
//		cv::resize(loaded_image, resized, cv::Size(w, h), 0, 0, cv::INTER_LINEAR);
//		out = mat_to_image(resized);
//	}
//	catch (...) {
//		cerr << " OpenCV exception: load_image_resize() can't load image %s " << filename << " \n";
//		out = make_image(w, h, c);
//		*im = make_image(w, h, c);
//	}
//	return out;
//}