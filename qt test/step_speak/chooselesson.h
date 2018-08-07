#ifndef CHOOSELESSON_H
#define CHOOSELESSON_H

#include <QMainWindow>

namespace Ui {
class ChooseLesson;
}

class ChooseLesson : public QMainWindow
{
    Q_OBJECT

public:
    explicit ChooseLesson(QWidget *parent = 0);
    ~ChooseLesson();

private:
    Ui::ChooseLesson *ui;
};

#endif // CHOOSELESSON_H
