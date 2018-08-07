#include <qcoreapplication.h>
//#include <program_one.h>
#include <qapplication.h>
#include <choose_lesson.h>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    //Program_One c;
    Choose_Lesson c;
    c.show();

    return a.exec();
}
