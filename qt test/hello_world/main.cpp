#include <QApplication>
#include <QPushButton>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QPushButton button1("Quit");
    QObject::connect(&button1, &QPushButton::clicked, &QApplication::quit);

    button1.show();

    return app.exec();
}
