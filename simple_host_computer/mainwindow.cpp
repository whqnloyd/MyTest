#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtSerialPort/QtSerialPort>
#include <QSerialPortInfo>

QString * port_info(){
    static QString info_list[6];
    foreach (const QSerialPortInfo &info, QSerialPortInfo::availablePorts())
        {
            info_list[0] = "Name : " + info.portName();
            info_list[1] = "Description : " + info.description();
            info_list[2] = "Manufacturer: " + info.manufacturer();
            info_list[3] = "Serial Number: " + info.serialNumber();
            info_list[4] = "System Location: " + info.systemLocation();
        }
    info_list[5]="This device has added to your list!";
    return info_list;
}

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->box_message->append("Welcome!");
    if (*port_info()!=""){
        ui->box_message->append(*port_info());
    }
    else{ui->box_message->append("no available device!");}
}

MainWindow::~MainWindow()
{
    delete ui;
}
