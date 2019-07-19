#include<pybind11/pybind11.h>

namespace py = pybind11;

int add(int a, int b) {
	return a + b;
}

int add2(int a, int b) {
	return a + b;
}

int add3(int a, int b) {
	return a + b;
}

PYBIND11_MODULE(pybind11hello, m) {

	m.doc() = "pybind11 example module";

	// Add bindings here
	m.def("hello", []() {
		return "Hello, World!";
		});

	m.def("add", &add, "add two numbers");

	//py::arg("a")
	m.def("add2", &add2, "A function which adds two numbers", py::arg("a"), py::arg("b"));

	//default arguments
	m.def("add3", &add3, "A function which adds two numbers", py::arg("a") = 10, py::arg("b") = 5);

	//Exporting variables
	m.attr("num1") = 100;
	py::object world = py::cast("World");
	m.attr("what") = world;
}