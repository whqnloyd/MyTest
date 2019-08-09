#include <iostream>
#include <string>

using namespace std;

void main() {
	string info_file_path;
	printf("information file path: ");
	getline(cin, info_file_path);
	if (info_file_path.size() == 0) {
		printf("hellyeah\n");
	}
}
