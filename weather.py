# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_weather(object):
    def setupUi(self, weather):
        if not weather.objectName():
            weather.setObjectName(u"weather")
        weather.setEnabled(True)
        weather.resize(957, 225)
        weather.setStyleSheet(u"background-color: #D9D9D9;")
        self.groupBox_2 = QGroupBox(weather)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, -10, 961, 211))
        self.groupBox_2.setStyleSheet(u"background-color: #D9D9D9;\n"
"border: 0;")
        self.weather_detail_block = QGroupBox(self.groupBox_2)
        self.weather_detail_block.setObjectName(u"weather_detail_block")
        self.weather_detail_block.setGeometry(QRect(410, 20, 161, 141))
        self.weather_detail_block.setStyleSheet(u"background-color: #D9D9D9;")
        self.yandex_week_logo_2 = QLabel(self.weather_detail_block)
        self.yandex_week_logo_2.setObjectName(u"yandex_week_logo_2")
        self.yandex_week_logo_2.setGeometry(QRect(10, 20, 31, 31))
        self.yandex_week_logo_2.setPixmap(QPixmap(u"C:/Users/zinch/Downloads/Yandex_znak.png"))
        self.yandex_week_logo_2.setScaledContents(True)
        self.mailru_week_logo_2 = QLabel(self.weather_detail_block)
        self.mailru_week_logo_2.setObjectName(u"mailru_week_logo_2")
        self.mailru_week_logo_2.setGeometry(QRect(10, 80, 31, 31))
        self.mailru_week_logo_2.setPixmap(QPixmap(u"C:/Users/zinch/Downloads/mail_ru_logo_icon_147267.png"))
        self.mailru_week_logo_2.setScaledContents(True)
        self.layoutWidget = QWidget(self.weather_detail_block)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 80, 91, 29))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.weather_mailru = QLabel(self.layoutWidget)
        self.weather_mailru.setObjectName(u"weather_mailru")
        self.weather_mailru.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_2.addWidget(self.weather_mailru)

        self.weather_mailru_data = QLabel(self.layoutWidget)
        self.weather_mailru_data.setObjectName(u"weather_mailru_data")
        self.weather_mailru_data.setStyleSheet(u"font-size: 20px;")
        self.weather_mailru_data.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.weather_mailru_data)

        self.layoutWidget1 = QWidget(self.weather_detail_block)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(51, 21, 91, 29))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.weather_yandex = QLabel(self.layoutWidget1)
        self.weather_yandex.setObjectName(u"weather_yandex")
        self.weather_yandex.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout.addWidget(self.weather_yandex)

        self.weather_yandex_data = QLabel(self.layoutWidget1)
        self.weather_yandex_data.setObjectName(u"weather_yandex_data")
        self.weather_yandex_data.setStyleSheet(u"font-size: 20px;")
        self.weather_yandex_data.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.weather_yandex_data)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(720, 20, 211, 191))
        self.label_2.setPixmap(QPixmap(u"C:/Users/zinch/Downloads/pngegg.png"))
        self.label_2.setScaledContents(True)
        self.groupBox = QGroupBox(weather)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, -10, 561, 211))
        self.groupBox.setStyleSheet(u"background-color: #D9D9D9;")
        self.weather_today = QLabel(self.groupBox)
        self.weather_today.setObjectName(u"weather_today")
        self.weather_today.setEnabled(True)
        self.weather_today.setGeometry(QRect(450, 20, 101, 81))
        font = QFont()
        font.setPointSize(60)
        self.weather_today.setFont(font)
        self.weather_today.setStyleSheet(u"padding: 0;\n"
"margin: 0;\n"
"color: black;\n"
"")
        self.weather_today.setAlignment(Qt.AlignCenter)
        self.refresh_weather_today = QPushButton(self.groupBox)
        self.refresh_weather_today.setObjectName(u"refresh_weather_today")
        self.refresh_weather_today.setGeometry(QRect(20, 120, 371, 71))
        font1 = QFont()
        font1.setBold(True)
        self.refresh_weather_today.setFont(font1)
        self.refresh_weather_today.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_weather_today.setStyleSheet(u"display: inline-block;\n"
"border-radius: 20px;\n"
"color: #1F1F1F;\n"
"font-size: 33px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #75D6FF, stop:1 #E3FF36);\n"
"font-weight: 600;\n"
"\n"
"")
        self.refresh_weather_today.setIconSize(QSize(16, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(20, 10, 421, 111))
        font2 = QFont()
        font2.setPointSize(18)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: black;")
        self.label.setWordWrap(True)
        self.weather_detail_btn = QPushButton(self.groupBox)
        self.weather_detail_btn.setObjectName(u"weather_detail_btn")
        self.weather_detail_btn.setEnabled(False)
        self.weather_detail_btn.setGeometry(QRect(450, 120, 101, 31))
        self.weather_detail_btn.setMaximumSize(QSize(16777215, 16777214))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.weather_detail_btn.setFont(font3)
        self.weather_detail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.weather_detail_btn.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #75D6FF, stop:1 #E3FF36);\n"
"font-weight: 600;\n"
"border: 0;\n"
"border-radius: 10px;\n"
"enabled: true;")
        self.weather_detail_btn.setCheckable(True)
        self.weather_week_detail_btn = QPushButton(self.groupBox)
        self.weather_week_detail_btn.setObjectName(u"weather_week_detail_btn")
        self.weather_week_detail_btn.setEnabled(False)
        self.weather_week_detail_btn.setGeometry(QRect(420, 160, 131, 31))
        self.weather_week_detail_btn.setMaximumSize(QSize(16777215, 16777214))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.weather_week_detail_btn.setFont(font4)
        self.weather_week_detail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.weather_week_detail_btn.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #75D6FF, stop:1 #E3FF36);\n"
"font-weight: 600;\n"
"border: 0;\n"
"border-radius: 10px;\n"
"enabled: true;")
        self.weather_week_detail_btn.setCheckable(True)
        self.week_detail_block = QGroupBox(weather)
        self.week_detail_block.setObjectName(u"week_detail_block")
        self.week_detail_block.setGeometry(QRect(0, -50, 951, 311))
        self.week_detail_block.setStyleSheet(u"background-color: 0;\n"
"")
        self.week_days_mailru_3 = QGroupBox(self.week_detail_block)
        self.week_days_mailru_3.setObjectName(u"week_days_mailru_3")
        self.week_days_mailru_3.setGeometry(QRect(180, 180, 761, 41))
        self.week_days_mailru_3.setStyleSheet(u"border: 0;")
        self.week_days_mailru_2 = QHBoxLayout(self.week_days_mailru_3)
        self.week_days_mailru_2.setObjectName(u"week_days_mailru_2")
        self.week_day_mailru = QLabel(self.week_days_mailru_3)
        self.week_day_mailru.setObjectName(u"week_day_mailru")
        font5 = QFont()
        font5.setPointSize(16)
        self.week_day_mailru.setFont(font5)
        self.week_day_mailru.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru)

        self.week_day_mailru_2 = QLabel(self.week_days_mailru_3)
        self.week_day_mailru_2.setObjectName(u"week_day_mailru_2")
        self.week_day_mailru_2.setFont(font5)
        self.week_day_mailru_2.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru_2)

        self.week_day_mailru_3 = QLabel(self.week_days_mailru_3)
        self.week_day_mailru_3.setObjectName(u"week_day_mailru_3")
        self.week_day_mailru_3.setFont(font5)
        self.week_day_mailru_3.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru_3)

        self.week_day_mailru_4 = QLabel(self.week_days_mailru_3)
        self.week_day_mailru_4.setObjectName(u"week_day_mailru_4")
        self.week_day_mailru_4.setFont(font5)
        self.week_day_mailru_4.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru_4)

        self.week_day_mailru_5 = QLabel(self.week_days_mailru_3)
        self.week_day_mailru_5.setObjectName(u"week_day_mailru_5")
        self.week_day_mailru_5.setFont(font5)
        self.week_day_mailru_5.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru_5)

        self.week_day_mailru_6 = QLabel(self.week_days_mailru_3)
        self.week_day_mailru_6.setObjectName(u"week_day_mailru_6")
        self.week_day_mailru_6.setFont(font5)
        self.week_day_mailru_6.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru_6)

        self.week_day_mailru_7 = QLabel(self.week_days_mailru_3)
        self.week_day_mailru_7.setObjectName(u"week_day_mailru_7")
        self.week_day_mailru_7.setFont(font5)
        self.week_day_mailru_7.setAlignment(Qt.AlignCenter)

        self.week_days_mailru_2.addWidget(self.week_day_mailru_7)

        self.mailru_week_title = QLabel(self.week_detail_block)
        self.mailru_week_title.setObjectName(u"mailru_week_title")
        self.mailru_week_title.setGeometry(QRect(70, 180, 81, 41))
        font6 = QFont()
        font6.setPointSize(14)
        self.mailru_week_title.setFont(font6)
        self.yandex_week_title = QLabel(self.week_detail_block)
        self.yandex_week_title.setObjectName(u"yandex_week_title")
        self.yandex_week_title.setGeometry(QRect(70, 90, 81, 41))
        self.yandex_week_title.setFont(font6)
        self.week_days_3 = QGroupBox(self.week_detail_block)
        self.week_days_3.setObjectName(u"week_days_3")
        self.week_days_3.setGeometry(QRect(180, 20, 761, 41))
        self.week_days_2 = QHBoxLayout(self.week_days_3)
        self.week_days_2.setObjectName(u"week_days_2")
        self.week_day = QLabel(self.week_days_3)
        self.week_day.setObjectName(u"week_day")
        font7 = QFont()
        font7.setPointSize(11)
        self.week_day.setFont(font7)
        self.week_day.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day)

        self.week_day_2 = QLabel(self.week_days_3)
        self.week_day_2.setObjectName(u"week_day_2")
        self.week_day_2.setFont(font7)
        self.week_day_2.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day_2)

        self.week_day_3 = QLabel(self.week_days_3)
        self.week_day_3.setObjectName(u"week_day_3")
        self.week_day_3.setFont(font7)
        self.week_day_3.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day_3)

        self.week_day_4 = QLabel(self.week_days_3)
        self.week_day_4.setObjectName(u"week_day_4")
        self.week_day_4.setFont(font7)
        self.week_day_4.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day_4)

        self.week_day_5 = QLabel(self.week_days_3)
        self.week_day_5.setObjectName(u"week_day_5")
        self.week_day_5.setFont(font7)
        self.week_day_5.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day_5)

        self.week_day_6 = QLabel(self.week_days_3)
        self.week_day_6.setObjectName(u"week_day_6")
        self.week_day_6.setFont(font7)
        self.week_day_6.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day_6)

        self.week_day_7 = QLabel(self.week_days_3)
        self.week_day_7.setObjectName(u"week_day_7")
        self.week_day_7.setFont(font7)
        self.week_day_7.setAlignment(Qt.AlignCenter)

        self.week_days_2.addWidget(self.week_day_7)

        self.week_day.raise_()
        self.week_day_2.raise_()
        self.week_day_3.raise_()
        self.week_day_5.raise_()
        self.week_day_6.raise_()
        self.week_day_7.raise_()
        self.week_day_4.raise_()
        self.mailru_week_logo = QLabel(self.week_detail_block)
        self.mailru_week_logo.setObjectName(u"mailru_week_logo")
        self.mailru_week_logo.setGeometry(QRect(20, 180, 41, 41))
        self.mailru_week_logo.setPixmap(QPixmap(u"C:/Users/zinch/Downloads/mail_ru_logo_icon_147267.png"))
        self.mailru_week_logo.setScaledContents(True)
        self.yandex_week_logo = QLabel(self.week_detail_block)
        self.yandex_week_logo.setObjectName(u"yandex_week_logo")
        self.yandex_week_logo.setGeometry(QRect(20, 90, 41, 41))
        self.yandex_week_logo.setPixmap(QPixmap(u"C:/Users/zinch/Downloads/Yandex_znak.png"))
        self.yandex_week_logo.setScaledContents(True)
        self.week_days_yandex_3 = QGroupBox(self.week_detail_block)
        self.week_days_yandex_3.setObjectName(u"week_days_yandex_3")
        self.week_days_yandex_3.setGeometry(QRect(180, 90, 761, 41))
        self.week_days_yandex_3.setStyleSheet(u"border: 0;")
        self.week_days_yandex_2 = QHBoxLayout(self.week_days_yandex_3)
        self.week_days_yandex_2.setObjectName(u"week_days_yandex_2")
        self.week_day_yandex = QLabel(self.week_days_yandex_3)
        self.week_day_yandex.setObjectName(u"week_day_yandex")
        self.week_day_yandex.setFont(font5)
        self.week_day_yandex.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex)

        self.week_day_yandex_2 = QLabel(self.week_days_yandex_3)
        self.week_day_yandex_2.setObjectName(u"week_day_yandex_2")
        self.week_day_yandex_2.setFont(font5)
        self.week_day_yandex_2.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex_2)

        self.week_day_yandex_3 = QLabel(self.week_days_yandex_3)
        self.week_day_yandex_3.setObjectName(u"week_day_yandex_3")
        self.week_day_yandex_3.setFont(font5)
        self.week_day_yandex_3.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex_3)

        self.week_day_yandex_4 = QLabel(self.week_days_yandex_3)
        self.week_day_yandex_4.setObjectName(u"week_day_yandex_4")
        self.week_day_yandex_4.setFont(font5)
        self.week_day_yandex_4.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex_4)

        self.week_day_yandex_5 = QLabel(self.week_days_yandex_3)
        self.week_day_yandex_5.setObjectName(u"week_day_yandex_5")
        self.week_day_yandex_5.setFont(font5)
        self.week_day_yandex_5.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex_5)

        self.week_day_yandex_6 = QLabel(self.week_days_yandex_3)
        self.week_day_yandex_6.setObjectName(u"week_day_yandex_6")
        self.week_day_yandex_6.setFont(font5)
        self.week_day_yandex_6.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex_6)

        self.week_day_yandex_7 = QLabel(self.week_days_yandex_3)
        self.week_day_yandex_7.setObjectName(u"week_day_yandex_7")
        self.week_day_yandex_7.setFont(font5)
        self.week_day_yandex_7.setAlignment(Qt.AlignCenter)

        self.week_days_yandex_2.addWidget(self.week_day_yandex_7)

        self.week_detail_back = QLabel(self.week_detail_block)
        self.week_detail_back.setObjectName(u"week_detail_back")
        self.week_detail_back.setGeometry(QRect(180, 70, 761, 171))
        self.week_detail_back.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #75D6FF, stop:1 #E3FF36);\n"
"border-radius: 20px;\n"
"")
        self.week_detail_back.raise_()
        self.week_days_mailru_3.raise_()
        self.mailru_week_title.raise_()
        self.yandex_week_title.raise_()
        self.week_days_3.raise_()
        self.mailru_week_logo.raise_()
        self.yandex_week_logo.raise_()
        self.week_days_yandex_3.raise_()
        self.week_detail_block.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()

        self.retranslateUi(weather)

        QMetaObject.connectSlotsByName(weather)
    # setupUi

    def retranslateUi(self, weather):
        weather.setWindowTitle(QCoreApplication.translate("weather", u"Form", None))
        self.groupBox_2.setTitle("")
        self.weather_detail_block.setTitle("")
        self.yandex_week_logo_2.setText("")
        self.mailru_week_logo_2.setText("")
        self.weather_mailru.setText(QCoreApplication.translate("weather", u"Mailru:", None))
        self.weather_mailru_data.setText(QCoreApplication.translate("weather", u"?", None))
        self.weather_yandex.setText(QCoreApplication.translate("weather", u"Yandex:", None))
        self.weather_yandex_data.setText(QCoreApplication.translate("weather", u"?", None))
        self.label_2.setText("")
        self.groupBox.setTitle("")
        self.weather_today.setText(QCoreApplication.translate("weather", u"?", None))
        self.refresh_weather_today.setText(QCoreApplication.translate("weather", u"\u0423\u0437\u043d\u0430\u0442\u044c \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0443", None))
        self.label.setText(QCoreApplication.translate("weather", u"\u0423\u0441\u0440\u0435\u0434\u043d\u0451\u043d\u043d\u0430\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0438\u0437 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u043e\u0432 \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f:", None))
        self.weather_detail_btn.setText(QCoreApplication.translate("weather", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.weather_week_detail_btn.setText(QCoreApplication.translate("weather", u"\u041f\u043e\u0433\u043e\u0434\u0430 \u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.week_detail_block.setTitle("")
        self.week_day_mailru.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_mailru_2.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_mailru_3.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_mailru_4.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_mailru_5.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_mailru_6.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_mailru_7.setText(QCoreApplication.translate("weather", u"?", None))
        self.mailru_week_title.setText(QCoreApplication.translate("weather", u"Mailru", None))
        self.yandex_week_title.setText(QCoreApplication.translate("weather", u"Yandex", None))
        self.week_day.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.week_day_2.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.week_day_3.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.week_day_4.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.week_day_5.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.week_day_6.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.week_day_7.setText(QCoreApplication.translate("weather", u"week_day", None))
        self.mailru_week_logo.setText("")
        self.yandex_week_logo.setText("")
        self.week_day_yandex.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_yandex_2.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_yandex_3.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_yandex_4.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_yandex_5.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_yandex_6.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_day_yandex_7.setText(QCoreApplication.translate("weather", u"?", None))
        self.week_detail_back.setText("")
    # retranslateUi

