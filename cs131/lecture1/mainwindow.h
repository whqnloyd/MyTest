#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <picresult.h>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    PicResult *pr;

private slots:
    void ToDoListChanged(int);
    void LoadAndShowImage();
    void CalAvg();
    void AvgBright();
    void DetectEdge();
    void BlurBox();
    void NewWindow();
};

#endif // MAINWINDOW_H
