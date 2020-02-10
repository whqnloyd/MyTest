/********************************************************************************
** Form generated from reading UI file 'picresult.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PICRESULT_H
#define UI_PICRESULT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGraphicsView>

QT_BEGIN_NAMESPACE

class Ui_PicResult
{
public:
    QGraphicsView *graphicsView;

    void setupUi(QDialog *PicResult)
    {
        if (PicResult->objectName().isEmpty())
            PicResult->setObjectName(QString::fromUtf8("PicResult"));
        PicResult->resize(400, 300);
        graphicsView = new QGraphicsView(PicResult);
        graphicsView->setObjectName(QString::fromUtf8("graphicsView"));
        graphicsView->setGeometry(QRect(0, 0, 401, 301));

        retranslateUi(PicResult);

        QMetaObject::connectSlotsByName(PicResult);
    } // setupUi

    void retranslateUi(QDialog *PicResult)
    {
        PicResult->setWindowTitle(QApplication::translate("PicResult", "Dialog", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PicResult: public Ui_PicResult {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PICRESULT_H
