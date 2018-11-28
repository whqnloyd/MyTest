/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *label_frequency;
    QPushButton *button_apply;
    QTextBrowser *box_message;
    QPushButton *button_refresh;
    QComboBox *port_list;
    QTextEdit *input_fre;
    QPushButton *button_open;
    QMenuBar *menuBar;
    QMenu *menusimple_host_computer;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(398, 237);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        label_frequency = new QLabel(centralWidget);
        label_frequency->setObjectName(QStringLiteral("label_frequency"));
        label_frequency->setGeometry(QRect(140, 20, 111, 16));
        button_apply = new QPushButton(centralWidget);
        button_apply->setObjectName(QStringLiteral("button_apply"));
        button_apply->setGeometry(QRect(290, 39, 80, 31));
        box_message = new QTextBrowser(centralWidget);
        box_message->setObjectName(QStringLiteral("box_message"));
        box_message->setGeometry(QRect(140, 80, 231, 101));
        button_refresh = new QPushButton(centralWidget);
        button_refresh->setObjectName(QStringLiteral("button_refresh"));
        button_refresh->setGeometry(QRect(0, 0, 93, 28));
        port_list = new QComboBox(centralWidget);
        port_list->setObjectName(QStringLiteral("port_list"));
        port_list->setGeometry(QRect(30, 40, 91, 31));
        input_fre = new QTextEdit(centralWidget);
        input_fre->setObjectName(QStringLiteral("input_fre"));
        input_fre->setGeometry(QRect(140, 40, 121, 31));
        button_open = new QPushButton(centralWidget);
        button_open->setObjectName(QStringLiteral("button_open"));
        button_open->setGeometry(QRect(30, 80, 93, 28));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 398, 26));
        menusimple_host_computer = new QMenu(menuBar);
        menusimple_host_computer->setObjectName(QStringLiteral("menusimple_host_computer"));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menusimple_host_computer->menuAction());

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label_frequency->setText(QApplication::translate("MainWindow", "Frequency", nullptr));
        button_apply->setText(QApplication::translate("MainWindow", "Apply", nullptr));
        button_refresh->setText(QApplication::translate("MainWindow", "Refresh", nullptr));
        button_open->setText(QApplication::translate("MainWindow", "Open", nullptr));
        menusimple_host_computer->setTitle(QApplication::translate("MainWindow", "Simple Host Computer", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
