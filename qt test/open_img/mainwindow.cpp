#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QImage>
#include <QFile>
#include <QTextStream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    resize(489,354);

    this->image = new QImage();

    connect(ui->Button_next,SIGNAL(clicked()),this,SLOT(next_clicked()));
}

void MainWindow::next_clicked()
{
    QPixmap image(":/image/L1_image");
    ui->image->clear();
    ui->image->setPixmap(image);

    QFile file(":/text/L1_text");
    file.open(QFile::ReadOnly | QFile::Text);
    QTextStream in(&file);
    QString text=in.readAll();
    ui->text->setText(text);
}

MainWindow::~MainWindow()
{
    delete image;
    delete ui;
}
