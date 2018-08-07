#ifndef CHOOSE_LESSON_H
#define CHOOSE_LESSON_H

#include <qmainwindow.h>

namespace Ui {
    class Choose_Lesson;
}

class Choose_Lesson : public QMainWindow
{
    Q_OBJECT

public:
    explicit Choose_Lesson(QWidget *parent = 0);
    ~Choose_Lesson();

private:
    Ui::Choose_Lesson *ui;

private slots:
    void start_study();
};

#endif // CHOOSE_LESSON_H
