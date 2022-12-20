import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QWidget, QGraphicsColorizeEffect, \
    QGraphicsOpacityEffect
from weather import Ui_weather
from weather_parser import WeatherBase

class Window(QDialog, Ui_weather):
    """Main window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.refresh_weather_today.clicked.connect(self.on_weather_btn_clicked)
        self.refresh_weather_today.pressed.connect(self.on_weather_btn_pressed)
        self.refresh_weather_today.released.connect(self.on_weather_btn_released)
        self.weather_detail_btn.toggled.connect(self.on_weather_detail_btn_toggled)
        self.weather_week_detail_btn.toggled.connect(self.on_weather_week_detail_btn_toggled)

    def btn_opacity_anim_press(self, child):
        self.child = child
        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0.85)
        self.anim.setDuration(150)
        self.anim.start()

    def btn_opacity_anim_release(self, child):
        self.child = child
        effect = QGraphicsOpacityEffect(self.child)
        self.child.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setStartValue(0.85)
        self.anim.setEndValue(1)
        self.anim.setDuration(450)
        self.anim.start()

    def on_weather_btn_clicked(self):
        self.weather = WeatherBase()
        self.weather.yandex_weather_report, self.weather.days = self.weather.yandex_weather_parser()
        self.weather.yandex_weather_report_cleaned = self.weather.yandex_weather_data_cleaner(self.weather.yandex_weather_report)
        self.weather.mailru_weather_report_cleaned = self.weather.mailru_weather_parser(self.weather.days)
        self.weather.medium_weather = self.weather.weather_mediator(self.weather.days, self.weather.yandex_weather_report_cleaned,
                                                          self.weather.mailru_weather_report_cleaned)
        self.weather_today.setText(str(self.weather.medium_weather['сегодня']) + '°')
        self.weather_yandex_data.setText(str(self.weather.yandex_weather_report_cleaned['сегодня']) + '°')
        self.weather_mailru_data.setText(str(self.weather.mailru_weather_report_cleaned['сегодня']) + '°')
        week = [self.week_day, self.week_day_2, self.week_day_3, self.week_day_4, self.week_day_5, self.week_day_6, self.week_day_7]
        week_yandex = [self.week_day_yandex, self.week_day_yandex_2, self.week_day_yandex_3, self.week_day_yandex_4, self.week_day_yandex_5, self.week_day_yandex_6, self.week_day_yandex_7]
        week_mail_ru = [self.week_day_mailru, self.week_day_mailru_2, self.week_day_mailru_3, self.week_day_mailru_4, self.week_day_mailru_5, self.week_day_mailru_6, self.week_day_mailru_7]
        for i in range(len(week)):
            week[i].setText(self.weather.days[i])
            week_yandex[i].setText(str(self.weather.yandex_weather_report_cleaned[self.weather.days[i]]) + '°')
            week_mail_ru[i].setText(str(self.weather.mailru_weather_report_cleaned[self.weather.days[i]]) + '°')
        self.weather_detail_btn.setEnabled(True)
        self.weather_week_detail_btn.setEnabled(True)

    def on_weather_btn_pressed(self):
        self.btn_opacity_anim_press(self.refresh_weather_today)

    def on_weather_btn_released(self):
        self.btn_opacity_anim_release(self.refresh_weather_today)

    def on_weather_detail_btn_toggled(self):
        self.child = self.weather_detail_block
        self.child2 = self.weather_detail_btn
        self.anim = QPropertyAnimation(self.child, b'pos')
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        effect = QGraphicsOpacityEffect(self.child2)
        self.child2.setGraphicsEffect(effect)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")

        self.anim_2.setDuration(500)
        print(self.child.pos())
        if self.weather_detail_btn.isChecked():
            self.anim.setEndValue(QPoint(self.child.pos().x() + 170, self.child.pos().y()))
            self.anim_2.setStartValue(1)
            self.anim_2.setEndValue(0.7)
        else:
            self.anim.setEndValue(QPoint(self.child.pos().x() - 170, self.child.pos().y()))
            self.anim_2.setStartValue(0.7)
            self.anim_2.setEndValue(1)
        self.anim.setDuration(1000)
        self.anim.start()
        self.anim_2.start()

    def on_weather_week_detail_btn_toggled(self):
        self.child = self.week_detail_block
        self.child2 = self.weather_week_detail_btn
        self.child3 = w
        self.anim = QPropertyAnimation(self.child, b'pos')
        effect = QGraphicsOpacityEffect(self.child2)
        self.child2.setGraphicsEffect(effect)
        self.anim.setDuration(2000)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setDuration(500)
        self.anim_3 = QPropertyAnimation(self.child3, b'size')
        self.anim_3.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim_3.setDuration(1000)
        effect2 = QGraphicsOpacityEffect(self.child2)
        self.child.setGraphicsEffect(effect2)
        self.anim_4 = QPropertyAnimation(effect2, b'opacity')
        print(self.child.pos())
        if self.weather_week_detail_btn.isChecked():
            self.anim.setEndValue(QPoint(self.child.pos().x(), self.child.pos().y()+250))
            self.anim.setEasingCurve(QEasingCurve.OutBounce)
            self.anim.setDuration(2000)
            self.anim_2.setStartValue(1)
            self.anim_2.setEndValue(0.7)
            self.anim_4.setStartValue(0)
            self.anim_4.setEndValue(1)
            print(self.child3.size())
            self.anim_3.setEndValue(QSize(self.child3.size().width(), self.child3.size().height()+280))
            self.anim_4.setDuration(500)
            # w.setGeometry(w.pos().x(), w.pos().y())
        else:
            self.anim.setEndValue(QPoint(self.child.pos().x(), self.child.pos().y()-250))
            self.anim.setEasingCurve(QEasingCurve.InOutCubic)
            self.anim.setDuration(1000)
            self.anim_2.setStartValue(0.7)
            self.anim_2.setEndValue(1)
            self.anim_4.setStartValue(1)
            self.anim_4.setEndValue(0)
            self.anim_3.setEndValue(QSize(self.child3.size().width(), self.child3.size().height() - 280))
            self.anim_4.setDuration(1000)
        self.anim.start()
        self.anim_2.start()
        self.anim_3.start()
        self.anim_4.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.setWindowTitle('weather')
    w.show()
    app.exec()
