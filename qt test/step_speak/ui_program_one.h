/********************************************************************************
** Form generated from reading UI file 'program_one.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PROGRAM_ONE_H
#define UI_PROGRAM_ONE_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Program_One
{
public:
    QWidget *centralWidget;
    QPushButton *Button_start;
    QPushButton *Button_play;
    QPushButton *Button_record;
    QPushButton *Button_replay;
    QLabel *image;
    QLabel *text;
    QLabel *grade;
    QMenuBar *menuBar;
    QMenu *menuVersion_1_0;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *Program_One)
    {
        if (Program_One->objectName().isEmpty())
            Program_One->setObjectName(QStringLiteral("Program_One"));
        Program_One->resize(500, 350);
        centralWidget = new QWidget(Program_One);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        Button_start = new QPushButton(centralWidget);
        Button_start->setObjectName(QStringLiteral("Button_start"));
        Button_start->setGeometry(QRect(200, 80, 81, 51));
        Button_play = new QPushButton(centralWidget);
        Button_play->setObjectName(QStringLiteral("Button_play"));
        Button_play->setGeometry(QRect(80, 260, 61, 21));
        Button_record = new QPushButton(centralWidget);
        Button_record->setObjectName(QStringLiteral("Button_record"));
        Button_record->setGeometry(QRect(210, 260, 61, 21));
        Button_replay = new QPushButton(centralWidget);
        Button_replay->setObjectName(QStringLiteral("Button_replay"));
        Button_replay->setGeometry(QRect(330, 260, 61, 21));
        image = new QLabel(centralWidget);
        image->setObjectName(QStringLiteral("image"));
        image->setGeometry(QRect(110, 0, 261, 181));
        text = new QLabel(centralWidget);
        text->setObjectName(QStringLiteral("text"));
        text->setGeometry(QRect(80, 210, 311, 51));
        grade = new QLabel(centralWidget);
        grade->setObjectName(QStringLiteral("grade"));
        grade->setGeometry(QRect(410, 10, 54, 51));
        Program_One->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(Program_One);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 500, 22));
        menuVersion_1_0 = new QMenu(menuBar);
        menuVersion_1_0->setObjectName(QStringLiteral("menuVersion_1_0"));
        Program_One->setMenuBar(menuBar);
        statusBar = new QStatusBar(Program_One);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        Program_One->setStatusBar(statusBar);

        menuBar->addAction(menuVersion_1_0->menuAction());

        retranslateUi(Program_One);

        QMetaObject::connectSlotsByName(Program_One);
    } // setupUi

    void retranslateUi(QMainWindow *Program_One)
    {
        Program_One->setWindowTitle(QApplication::translate("Program_One", "MainWindow", nullptr));
        Button_start->setText(QApplication::translate("Program_One", "Start", nullptr));
        Button_play->setText(QApplication::translate("Program_One", "Play", nullptr));
        Button_record->setText(QApplication::translate("Program_One", "Record", nullptr));
        Button_replay->setText(QApplication::translate("Program_One", "Replay", nullptr));
        image->setText(QString());
        text->setText(QString());
        grade->setText(QString());
        menuVersion_1_0->setTitle(QApplication::translate("Program_One", "Version 1.0", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Program_One: public Ui_Program_One {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PROGRAM_ONE_H
