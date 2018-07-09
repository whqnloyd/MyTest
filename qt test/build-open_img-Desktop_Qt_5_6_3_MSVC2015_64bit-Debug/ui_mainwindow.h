/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.6.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGraphicsView *image;
    QPushButton *Button_next;
    QPushButton *Button_play;
    QPushButton *Button_record;
    QPushButton *Button_replay;
    QTextBrowser *text;
    QMenuBar *menuBar;
    QMenu *menuVersion_1_0;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(489, 354);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        image = new QGraphicsView(centralWidget);
        image->setObjectName(QStringLiteral("image"));
        image->setGeometry(QRect(110, 0, 256, 192));
        Button_next = new QPushButton(centralWidget);
        Button_next->setObjectName(QStringLiteral("Button_next"));
        Button_next->setGeometry(QRect(420, 210, 51, 31));
        Button_play = new QPushButton(centralWidget);
        Button_play->setObjectName(QStringLiteral("Button_play"));
        Button_play->setGeometry(QRect(80, 260, 61, 21));
        Button_record = new QPushButton(centralWidget);
        Button_record->setObjectName(QStringLiteral("Button_record"));
        Button_record->setGeometry(QRect(210, 260, 61, 21));
        Button_replay = new QPushButton(centralWidget);
        Button_replay->setObjectName(QStringLiteral("Button_replay"));
        Button_replay->setGeometry(QRect(330, 260, 61, 21));
        text = new QTextBrowser(centralWidget);
        text->setObjectName(QStringLiteral("text"));
        text->setGeometry(QRect(110, 190, 251, 61));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 489, 22));
        menuVersion_1_0 = new QMenu(menuBar);
        menuVersion_1_0->setObjectName(QStringLiteral("menuVersion_1_0"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuVersion_1_0->menuAction());

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        Button_next->setText(QApplication::translate("MainWindow", "Next", Q_NULLPTR));
        Button_play->setText(QApplication::translate("MainWindow", "Play", Q_NULLPTR));
        Button_record->setText(QApplication::translate("MainWindow", "Record", Q_NULLPTR));
        Button_replay->setText(QApplication::translate("MainWindow", "Replay", Q_NULLPTR));
        menuVersion_1_0->setTitle(QApplication::translate("MainWindow", "Version 1.0", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
