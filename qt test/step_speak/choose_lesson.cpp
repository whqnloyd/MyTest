#include "choose_lesson.h"
#include "ui_choose_lesson.h"
#include <program_one.h>

Choose_Lesson::Choose_Lesson(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Choose_Lesson)
{
    ui->setupUi(this);
    //选择课程
    ui->lesson->addItem("Lesson 1");
    ui->lesson->addItem("Lesson 2");
    //选择程序
    ui->program->addItem("Program 1");
    ui->program->addItem("Program 2");
    //开始
    connect(ui->start,SIGNAL(clicked()),this,SLOT(start_study()));
}

 void Choose_Lesson::start_study()
{
    Program_One *w = new Program_One(this);
    w->show();
}

Choose_Lesson::~Choose_Lesson()
{
    delete ui;
}
