#include "MyCamera.h"

using namespace std;

int main(int argc, char *argv[])
{
	YAML::Node config = YAML::LoadFile("cal.yaml");
	MyCamera Cam1(config["Camera1"]);
	MyCamera Cam2(config["Camera2"]);

	getchar();
}