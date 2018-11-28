#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QSerialPortInfo>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->box_message->append("Welcome!");
    Detection();
    ui->button_apply->setEnabled(false);

    //connect(serial,SIGNAL(readyRead()),this,SLOT(Read_Message()));
    connect(ui->button_refresh,SIGNAL(clicked()),this,SLOT(Detection()));
    connect(ui->button_open,SIGNAL(clicked()),this,SLOT(Open_port()));
    connect(ui->button_apply,SIGNAL(clicked()),this,SLOT(Change()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::Detection(){
    foreach (const QSerialPortInfo &info, QSerialPortInfo::availablePorts())
        {
        QSerialPort serial;
            serial.setPort(info);
            if(serial.open(QIODevice::ReadWrite))
            {
                if (serial.portName()!=ui->port_list->currentText()){
                    ui->port_list->addItem(serial.portName());
                    serial.close();
                }
                //else{
                //    ui->port_list->removeItem(1);
                //    serial.close();
               // }
            }
        }
}

void MainWindow::Open_port(){
    serial = new QSerialPort();
    serial->setPortName(ui->port_list->currentText());
    serial->open(QIODevice::ReadWrite);
    serial->setBaudRate(QSerialPort::Baud9600);
    serial->setDataBits(QSerialPort::Data8);
    serial->setStopBits(QSerialPort::OneStop);
    serial->setFlowControl(QSerialPort::NoFlowControl);

    ui->button_apply->setEnabled(true);
    ui->box_message->append("Port has been opened!");
    //connect(serial,SIGNAL(readyRead()),this,SLOT(Read_Message()));
}

void MainWindow::Change()
{
    serial->write(ui->input_fre->toPlainText().toLatin1());
    ui->input_fre->clear();
    ui->box_message->append("Sent!");
}

void MainWindow::Read_Message(){
    QByteArray buf;
        buf = serial->readAll();
        if(!buf.isEmpty())
        {
            QString str = ui->box_message->toPlainText();
            str+=tr(buf);
            ui->box_message->append(str);
        }
        buf.clear();
}
