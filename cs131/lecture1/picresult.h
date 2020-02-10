#ifndef PICRESULT_H
#define PICRESULT_H

#include <QDialog>

namespace Ui {
class PicResult;
}

class PicResult : public QDialog
{
    Q_OBJECT

public:
    explicit PicResult(QWidget *parent = nullptr);
    ~PicResult();

private:
    Ui::PicResult *ui;
};

#endif // PICRESULT_H
