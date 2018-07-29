#include <Python.h>
#include <qdebug.h>

#include <qimage.h>
#include <qfile.h>
#include <qtextstream.h>

#include <ui_mainwindow.h>
#include <mainwindow.h>

#include <iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    resize(489,354);

    this->image = new QImage();

    connect(ui->Button_next,SIGNAL(clicked()),this,SLOT(next_clicked()));
    connect(ui->Button_play,SIGNAL(clicked()),this,SLOT(play_clicked()));
    connect(ui->Button_record,SIGNAL(clicked()),this,SLOT(record_clicked()));
    connect(ui->Button_replay,SIGNAL(clicked()),this,SLOT(replay_clicked()));
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

    //初始化python模块
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs')");
    PyObject* pmodule = PyImport_ImportModule("googleTTS");
    if (!pmodule)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello = PyObject_GetAttrString(pmodule,"text2speech");
    if (!phello)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject_CallFunction(phello,"s,","C:/Users/Luodai Yang/Projects/Mytest/qt test/open_img/text/L1.txt");
    //释放python
    Py_Finalize();
}

void MainWindow::play_clicked()
{
    //初始化python模块
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs')");
    PyObject* pmodule = PyImport_ImportModule("playaudio");
    if (!pmodule)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello = PyObject_GetAttrString(pmodule,"play_speech");
    if (!phello)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject_CallFunction(phello,NULL);
    //释放python
    Py_Finalize();
}

void MainWindow::record_clicked()
{
    //记录音频
    //初始化python模块
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs')");
    PyObject* pmodule1 = PyImport_ImportModule("record_speech");
    if (!pmodule1)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello1 = PyObject_GetAttrString(pmodule1,"record_audio_file");
    if (!phello1)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject_CallFunction(phello1,"i,s",10,"C:/Users/Luodai Yang/Projects/Mytest/qt test/open_img/audio/speech.wav");
    //释放python
    Py_Finalize();

    //音频转文字
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs')");
    PyObject* pmodule2 = PyImport_ImportModule("googleSTT");
    if (!pmodule2)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello2 = PyObject_GetAttrString(pmodule2,"speech_to_txt");
    if (!phello2)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject_CallFunction(phello2,NULL);
    //释放python
    Py_Finalize();

    //评估
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs')");
    PyObject* pmodule3 = PyImport_ImportModule("evaluation");
    if (!pmodule3)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello3 = PyObject_GetAttrString(pmodule3,"evaluation");
    if (!phello3)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject* result = PyObject_CallObject(phello3,NULL);
    // 验证是否调用成功
    if (!result)
    {
        qDebug()<<"get return failed";
        return;
    }
    int grade;
    PyArg_Parse(result, "i", &grade);
    //打分
    ui->grade->setNum(grade);
    //释放python
    Py_Finalize();
}

void MainWindow::replay_clicked()
{
    //初始化python模块
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs')");
    PyObject* pmodule = PyImport_ImportModule("replay_speech");
    if (!pmodule)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello = PyObject_GetAttrString(pmodule,"replay_speech_file");
    if (!phello)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject_CallFunction(phello,"s","C:/Users/Luodai Yang/Projects/Mytest/qt test/open_img/audio/speech.wav");
    //释放python
    Py_Finalize();
}

MainWindow::~MainWindow()
{
    delete image;
    delete ui;
}
