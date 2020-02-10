/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QPlainTextEdit *plainTextEdit;
    QGraphicsView *graphicsView;
    QTextBrowser *resultsOutput;
    QComboBox *toDoList;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(774, 576);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        plainTextEdit = new QPlainTextEdit(centralWidget);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(30, 20, 591, 31));
        graphicsView = new QGraphicsView(centralWidget);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setGeometry(QRect(30, 70, 591, 441));
        resultsOutput = new QTextBrowser(centralWidget);
        resultsOutput->setObjectName(QString::fromUtf8("resultsOutput"));
        resultsOutput->setEnabled(true);
        resultsOutput->setGeometry(QRect(640, 70, 121, 441));
        toDoList = new QComboBox(centralWidget);
        toDoList->addItem(QString());
        toDoList->addItem(QString());
        toDoList->addItem(QString());
        toDoList->addItem(QString());
        toDoList->addItem(QString());
        toDoList->addItem(QString());
        toDoList->setObjectName(QString::fromUtf8("toDoList"));
        toDoList->setGeometry(QRect(640, 20, 121, 31));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 774, 21));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        plainTextEdit->setPlaceholderText(QApplication::translate("MainWindow", "Image Address", nullptr));
        resultsOutput->setPlaceholderText(QApplication::translate("MainWindow", "Output", nullptr));
        toDoList->setItemText(0, QString());
        toDoList->setItemText(1, QApplication::translate("MainWindow", "Load Image", nullptr));
        toDoList->setItemText(2, QApplication::translate("MainWindow", "Gray Image and Calculate Mean", nullptr));
        toDoList->setItemText(3, QApplication::translate("MainWindow", "Average Brightness", nullptr));
        toDoList->setItemText(4, QApplication::translate("MainWindow", "Detect Edge", nullptr));
        toDoList->setItemText(5, QApplication::translate("MainWindow", "BlurBox", nullptr));

    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
