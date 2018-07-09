#include <QAction>
#include <QMenuBar>
#include <QMessageBox>
#include <QStatusBar>
#include <QToolBar>

#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    //设置标题
    setWindowTitle(tr("welcome"));

    //传入图标、文本和指针
    openAction = new QAction(QIcon(":/images/open_file"), tr("open..."), this);
    //快捷键设置
    openAction->setShortcuts(QKeySequence::Open);
    //状态栏显示提示
    openAction->setStatusTip(tr("open an file"));
    connect(openAction, &QAction::triggered, this, &MainWindow::open);

    QMenu *fileM = menuBar()->addMenu(tr("&File"));
    fileM->addAction(openAction);

    QToolBar *toolB = addToolBar(tr("&File"));
    toolB->addAction(openAction);

    QStatusBar *statuB = statusBar();
    statuB->addAction(openAction);
}

MainWindow::~MainWindow()
{
}

void MainWindow::open()
{
    QMessageBox::information(this, tr("tip"), tr("open"));
}
