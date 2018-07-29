#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <qmainwindow.h>

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    QImage *image;

private slots:
    void next_clicked();
    void play_clicked();
    void record_clicked();
    void replay_clicked();
};

#endif // MAINWINDOW_H
