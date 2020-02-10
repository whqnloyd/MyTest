#-------------------------------------------------
#
# Project created by QtCreator 2020-01-13T17:29:32
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = lecture1
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++11

SOURCES += \
        main.cpp \
        mainwindow.cpp \
        picresult.cpp

HEADERS += \
        mainwindow.h \
        picresult.h

FORMS += \
        mainwindow.ui \
        picresult.ui

INCLUDEPATH += D:\local\opencv\build\include

#LIBS += D:\local\opencv\build\bin\opencv_ffmpeg349.dll
#LIBS += D:\local\opencv\build\x64\vc15\bin\opencv_world349.dll

LIBS += D:\local\opencv\build\x64\vc15\lib\opencv_world349.lib

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
