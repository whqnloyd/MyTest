#-------------------------------------------------
#
# Project created by QtCreator 2018-07-08T17:52:14
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = open_img
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


SOURCES += \
        main.cpp \
    choose_lesson.cpp \
    program_one.cpp

HEADERS += \
    choose_lesson.h \
    program_one.h \
    ui_choose_lesson.h \
    ui_program_one.h

FORMS += \
    choose_lesson.ui \
    program_one.ui

RESOURCES += \
          res.qrc

win32: LIBS += -LC:/Users/yangl/AppData/Local/Programs/Python/Python36/libs/ -lpython36

INCLUDEPATH += C:/Users/yangl/AppData/Local/Programs/Python/Python36/include
DEPENDPATH += C:/Users/yangl/AppData/Local/Programs/Python/Python36/include
