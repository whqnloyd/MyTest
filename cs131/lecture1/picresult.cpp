#include "picresult.h"
#include "ui_picresult.h"

PicResult::PicResult(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::PicResult)
{
    ui->setupUi(this);
}

PicResult::~PicResult()
{
    delete ui;
}
