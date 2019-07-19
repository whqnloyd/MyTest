#include <conio.h>
#include <boost/python.hpp>

void workspace_c(int a, int b)
{
	int c;
	c = a + b;
	printf("%d",c);
}

BOOST_PYTHON_MODULE(workspace)
{
	using namespace boost::python;
	def("workspace_b", workspace_c);
}