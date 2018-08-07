#include "chooselesson.h"
#include "ui_chooselesson.h"

ChooseLesson::ChooseLesson(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ChooseLesson)
{
    ui->setupUi(this);
}

ChooseLesson::~ChooseLesson()
{
    delete ui;
}
