/********************************************************************************
** Form generated from reading UI file 'choose_lesson.ui'
**
** Created by: Qt User Interface Compiler version 5.6.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CHOOSE_LESSON_H
#define UI_CHOOSE_LESSON_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Choose_Lesson
{
public:
    QWidget *centralwidget;
    QComboBox *lesson;
    QComboBox *program;
    QPushButton *start;
    QStatusBar *statusbar;
    QMenuBar *menubar;
    QMenu *menu;

    void setupUi(QMainWindow *Choose_Lesson)
    {
        if (Choose_Lesson->objectName().isEmpty())
            Choose_Lesson->setObjectName(QStringLiteral("Choose_Lesson"));
        Choose_Lesson->resize(500, 350);
        centralwidget = new QWidget(Choose_Lesson);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        lesson = new QComboBox(centralwidget);
        lesson->setObjectName(QStringLiteral("lesson"));
        lesson->setGeometry(QRect(120, 30, 260, 30));
        lesson->setAcceptDrops(false);
        lesson->setEditable(true);
        program = new QComboBox(centralwidget);
        program->setObjectName(QStringLiteral("program"));
        program->setGeometry(QRect(120, 100, 260, 30));
        program->setEditable(true);
        start = new QPushButton(centralwidget);
        start->setObjectName(QStringLiteral("start"));
        start->setGeometry(QRect(210, 210, 81, 41));
        Choose_Lesson->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(Choose_Lesson);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        Choose_Lesson->setStatusBar(statusbar);
        menubar = new QMenuBar(Choose_Lesson);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 500, 22));
        menu = new QMenu(menubar);
        menu->setObjectName(QStringLiteral("menu"));
        Choose_Lesson->setMenuBar(menubar);

        menubar->addAction(menu->menuAction());

        retranslateUi(Choose_Lesson);

        QMetaObject::connectSlotsByName(Choose_Lesson);
    } // setupUi

    void retranslateUi(QMainWindow *Choose_Lesson)
    {
        Choose_Lesson->setWindowTitle(QApplication::translate("Choose_Lesson", "MainWindow", Q_NULLPTR));
        start->setText(QApplication::translate("Choose_Lesson", "Start", Q_NULLPTR));
        menu->setTitle(QApplication::translate("Choose_Lesson", "\351\200\211\346\213\251\344\275\240\347\232\204\350\257\276\347\250\213\345\222\214\347\250\213\345\272\217", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Choose_Lesson: public Ui_Choose_Lesson {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CHOOSE_LESSON_H
