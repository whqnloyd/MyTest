#ifndef PROGRAM_ONE_H
#define PROGRAM_ONE_H

#include <qmainwindow.h>

namespace Ui {
    class Program_One;
}

class Program_One : public QMainWindow
{
    Q_OBJECT

public:
    explicit Program_One(QWidget *parent = nullptr);
    ~Program_One();

private:
    Ui::Program_One *ui;
    QImage *image;

private slots:
    void start_clicked();
    void play_clicked();
    void record_clicked();
    void replay_clicked();
};

#endif // PROGRAM_ONE_H
