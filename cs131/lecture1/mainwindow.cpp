#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    //QObject::connect(ui->buttonLoadImage, SIGNAL(clicked()), this, SLOT(LoadAndShowImage()));
    QObject::connect(ui->toDoList, SIGNAL(currentIndexChanged(int)), this, SLOT(ToDoListChanged(int)));
}

void MainWindow::ToDoListChanged(int indx){
    switch(indx){
        case 0:
            break;
        case 1:
            LoadAndShowImage();
            break;
        case 2:
            CalAvg();
            break;
        case 3:
            AvgBright();
            break;
        case 4:
            DetectEdge();
            break;
        case 5:
            BlurBox();
            break;
    }
}

void MainWindow::LoadAndShowImage() {
    QString x = ui->plainTextEdit->toPlainText();
    std::string image_address = x.toStdString();

    cv::Mat image;
    image = cv::imread(image_address, -1);
    cv::cvtColor(image, image, cv::COLOR_BGR2RGB);

    QGraphicsScene *scene = new QGraphicsScene;
    QPixmap pixmap = QPixmap::fromImage(QImage(image.data,image.cols, image.rows, QImage::Format_RGB888));
    scene->addPixmap(pixmap);

    ui->graphicsView->setScene(scene);
    ui->graphicsView->fitInView(scene->sceneRect(), Qt::KeepAspectRatio);
    ui->graphicsView->show();
}

void MainWindow::CalAvg() {
    QString x = ui->plainTextEdit->toPlainText();
    std::string image_address = x.toStdString();

    cv::Mat image;
    image = cv::imread(image_address, 0);

    QGraphicsScene *scene = new QGraphicsScene;
    QPixmap pixmap = QPixmap::fromImage(QImage(image.data,image.cols, image.rows, QImage::Format_Grayscale8));
    scene->addPixmap(pixmap);

    ui->graphicsView->setScene(scene);
    ui->graphicsView->fitInView(scene->sceneRect(), Qt::KeepAspectRatio);
    ui->graphicsView->show();

    cv::Scalar mean = cv::mean(image);
    QString result = "The mean is: ";
    result.append(QString::number(mean[0]));
    ui->resultsOutput->setText(result);
}

void MainWindow::AvgBright(){
    QString x = ui->plainTextEdit->toPlainText();
    std::string image_address = x.toStdString();

    cv::Mat image;
    image = cv::imread(image_address, 0);

    double minv;
    double maxv;
    cv::minMaxIdx(image, &minv, &maxv);
    QString result = "The minimum value is: ";
    result.append(QString::number(minv));
    result.append("\n");
    result.append("The maximum value is: ");
    result.append(QString::number(maxv));
    result.append("\n");
    result.append("Applied ((i,j)-min)*(255/(max-min))");

    for(int i=0; i<image.rows; i++){
        for(int j=0; j<image.cols; j++){
            image.at<uchar>(i,j)=(image.at<uchar>(i,j)-minv)*(255/(maxv-minv));
        }
    }

    QGraphicsScene *scene = new QGraphicsScene;
    QPixmap pixmap = QPixmap::fromImage(QImage(image.data,image.cols, image.rows, QImage::Format_Grayscale8));
    scene->addPixmap(pixmap);

    ui->graphicsView->setScene(scene);
    ui->graphicsView->fitInView(scene->sceneRect(), Qt::KeepAspectRatio);
    ui->graphicsView->show();

    ui->resultsOutput->setText(result);
}

void MainWindow::DetectEdge(){
    QString x = ui->plainTextEdit->toPlainText();
    std::string image_address = x.toStdString();

    cv::Mat image;
    image = cv::imread(image_address, 0);

    QGraphicsScene *scene = new QGraphicsScene;
    QPixmap pixmap = QPixmap::fromImage(QImage(image.data,image.cols, image.rows, QImage::Format_Grayscale8));
    scene->addPixmap(pixmap);

    ui->graphicsView->setScene(scene);
    ui->graphicsView->fitInView(scene->sceneRect(), Qt::KeepAspectRatio);
    ui->graphicsView->show();

    for(int i=0; i<image.rows; i++){
        for(int j=1; j<image.cols; j++){
            image.at<uchar>(i,j-1) = image.at<uchar>(i,j) - image.at<uchar>(i,j-1);
        }
    }

    namedWindow( "Display window", cv::WINDOW_AUTOSIZE);
    imshow( "Display window", image);
    cv::waitKey(0);
}

void MainWindow::BlurBox(){
    QString x = ui->plainTextEdit->toPlainText();
    std::string image_address = x.toStdString();

    cv::Mat image;
    image = cv::imread(image_address, 0);

    QGraphicsScene *scene = new QGraphicsScene;
    QPixmap pixmap = QPixmap::fromImage(QImage(image.data,image.cols, image.rows, QImage::Format_Grayscale8));
    scene->addPixmap(pixmap);

    ui->graphicsView->setScene(scene);
    ui->graphicsView->fitInView(scene->sceneRect(), Qt::KeepAspectRatio);
    ui->graphicsView->show();

    int kernel_unit = 4;

    cv::Mat result(image.rows, image.cols, CV_8UC1, cv::Scalar(0));

    for(int i=0; i <= image.rows - kernel_unit; i += kernel_unit){
        for(int j=0; j <= image.cols - kernel_unit; j += kernel_unit){
            double s = cv::sum(image(cv::Rect(j, i, kernel_unit, kernel_unit)))[0];
            result(cv::Rect(j, i, kernel_unit, kernel_unit)) = s/pow(kernel_unit, 2);
        }
    }

    namedWindow( "Display window", cv::WINDOW_AUTOSIZE);
    imshow( "Display window", result);
    cv::waitKey(0);
}

void MainWindow::NewWindow(){
    PicResult pr;
    pr.show();
}

MainWindow::~MainWindow()
{
    delete ui;
}
