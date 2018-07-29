#include <Python.h>
#include <qdebug.h>

#include <ui_mainwindow.h>
#include <mainwindow.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->Button_test,SIGNAL(clicked()),this,SLOT(on_pushButton_clicked()));
}

void MainWindow::on_pushButton_clicked()
{
    //初始化python模块
    Py_Initialize();
    if ( !Py_IsInitialized() )
    {
        return;
    }
    //给出调用模块的路径并导入
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('C:/Users/Luodai Yang/Projects/AI-functions')");
    PyObject* pmodule = PyImport_ImportModule("image_description_copy");
    //PyObject* pmodule = PyImport_ImportModule("test002");
    if (!pmodule)
    {
        qDebug()<<"cant open file";
        return;
    }
    //获取hello函数
    PyObject* phello = PyObject_GetAttrString(pmodule,"recognize_image");
    if (!phello)
    {
        qDebug()<<"get function failed";
        return;
    }
    //调用hello函数
    PyObject_CallFunction(phello,"s","http://p3.pstatp.com/large/666d0002d3cf79529be8");
    //释放python
    Py_Finalize();
}

MainWindow::~MainWindow()
{
    delete ui;
}
