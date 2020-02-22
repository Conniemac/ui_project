# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/auto_grow_ui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from datetime import datetime, timedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

import database


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 310)
        Form.setMinimumSize(QtCore.QSize(400, 310))
        Form.setMaximumSize(QtCore.QSize(400, 310))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.temperature_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.temperature_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temperature_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temperature_frame.setObjectName("temperature_frame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.temperature_frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 181, 136))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.temperature_main_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.temperature_main_label.setObjectName("temperature_main_label")
        self.verticalLayout_5.addWidget(self.temperature_main_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.temperature_current_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_current_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_current_label.setObjectName("temperature_current_label")
        self.verticalLayout_7.addWidget(self.temperature_current_label)
        self.temperature_6hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_6hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_6hour_label.setObjectName("temperature_6hour_label")
        self.verticalLayout_7.addWidget(self.temperature_6hour_label)
        self.temperature_12hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_12hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_12hour_label.setObjectName("temperature_12hour_label")
        self.verticalLayout_7.addWidget(self.temperature_12hour_label)
        self.temperature_24hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_24hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_24hour_label.setObjectName("temperature_24hour_label")
        self.verticalLayout_7.addWidget(self.temperature_24hour_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.temperature_current = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_current.setObjectName("temperature_current")
        self.verticalLayout_8.addWidget(self.temperature_current)
        self.temperature_6hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_6hour_avg.setObjectName("temperature_6hour_avg")
        self.verticalLayout_8.addWidget(self.temperature_6hour_avg)
        self.temperature_12hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_12hour_avg.setObjectName("temperature_12hour_avg")
        self.verticalLayout_8.addWidget(self.temperature_12hour_avg)
        self.temperature_24hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.temperature_24hour_avg.setObjectName("temperature_24hour_avg")
        self.verticalLayout_8.addWidget(self.temperature_24hour_avg)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.temperature_frame)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.humidity_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.humidity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.humidity_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.humidity_frame.setObjectName("humidity_frame")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.humidity_frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 181, 136))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.humidity_main_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.humidity_main_label.setObjectName("humidity_main_label")
        self.verticalLayout_6.addWidget(self.humidity_main_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.humidity_current_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_current_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity_current_label.setObjectName("humidity_current_label")
        self.verticalLayout_10.addWidget(self.humidity_current_label)
        self.humidity_6hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_6hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity_6hour_label.setObjectName("humidity_6hour_label")
        self.verticalLayout_10.addWidget(self.humidity_6hour_label)
        self.humidity_12hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_12hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity_12hour_label.setObjectName("humidity_12hour_label")
        self.verticalLayout_10.addWidget(self.humidity_12hour_label)
        self.humidity_24hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_24hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity_24hour_label.setObjectName("humidity_24hour_label")
        self.verticalLayout_10.addWidget(self.humidity_24hour_label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.humidity_current = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_current.setObjectName("humidity_current")
        self.verticalLayout_11.addWidget(self.humidity_current)
        self.humidity_6hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_6hour_avg.setObjectName("humidity_6hour_avg")
        self.verticalLayout_11.addWidget(self.humidity_6hour_avg)
        self.humidity_12hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_12hour_avg.setObjectName("humidity_12hour_avg")
        self.verticalLayout_11.addWidget(self.humidity_12hour_avg)
        self.humidity_24hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.humidity_24hour_avg.setObjectName("humidity_24hour_avg")
        self.verticalLayout_11.addWidget(self.humidity_24hour_avg)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.humidity_frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.co2_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.co2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.co2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.co2_frame.setObjectName("co2_frame")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.co2_frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 181, 135))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.co2_main_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_main_label.setMinimumSize(QtCore.QSize(0, 15))
        self.co2_main_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.co2_main_label.setObjectName("co2_main_label")
        self.verticalLayout_9.addWidget(self.co2_main_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.co2_current_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_current_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.co2_current_label.setObjectName("co2_current_label")
        self.verticalLayout_2.addWidget(self.co2_current_label)
        self.co2_6hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_6hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.co2_6hour_label.setObjectName("co2_6hour_label")
        self.verticalLayout_2.addWidget(self.co2_6hour_label)
        self.co2_12hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_12hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.co2_12hour_label.setObjectName("co2_12hour_label")
        self.verticalLayout_2.addWidget(self.co2_12hour_label)
        self.co2_24hour_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_24hour_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.co2_24hour_label.setObjectName("co2_24hour_label")
        self.verticalLayout_2.addWidget(self.co2_24hour_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.co2_current = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_current.setObjectName("co2_current")
        self.verticalLayout_4.addWidget(self.co2_current)
        self.co2_6hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_6hour_avg.setObjectName("co2_6hour_avg")
        self.verticalLayout_4.addWidget(self.co2_6hour_avg)
        self.co2_12hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_12hour_avg.setObjectName("co2_12hour_avg")
        self.verticalLayout_4.addWidget(self.co2_12hour_avg)
        self.co2_24hour_avg = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.co2_24hour_avg.setObjectName("co2_24hour_avg")
        self.verticalLayout_4.addWidget(self.co2_24hour_avg)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.co2_frame)
        self.frame_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(20, 60, 141, 20))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self._timer_painter = QTimer(Form)
        self._timer_painter.start(1000)
        self._timer_painter.timeout.connect(self.update_values)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.temperature_main_label.setText(_translate("Form", "Temperature"))
        self.temperature_current_label.setText(_translate("Form", "Current:"))
        self.temperature_6hour_label.setText(_translate("Form", "6 hr avg:"))
        self.temperature_12hour_label.setText(_translate("Form", "12 hr avg:"))
        self.temperature_24hour_label.setText(_translate("Form", "24 hr avg:"))
        self.temperature_current.setText(_translate("Form", "0"))
        self.temperature_6hour_avg.setText(_translate("Form", "0"))
        self.temperature_12hour_avg.setText(_translate("Form", "0"))
        self.temperature_24hour_avg.setText(_translate("Form", "0"))
        self.humidity_main_label.setText(_translate("Form", "Humidity"))
        self.humidity_current_label.setText(_translate("Form", "Current:"))
        self.humidity_6hour_label.setText(_translate("Form", "6 hr avg:"))
        self.humidity_12hour_label.setText(_translate("Form", "12 hr avg:"))
        self.humidity_24hour_label.setText(_translate("Form", "24 hr avg:"))
        self.humidity_current.setText(_translate("Form", "0"))
        self.humidity_6hour_avg.setText(_translate("Form", "0"))
        self.humidity_12hour_avg.setText(_translate("Form", "0"))
        self.humidity_24hour_avg.setText(_translate("Form", "0"))
        self.co2_main_label.setText(_translate("Form", "CO2"))
        self.co2_current_label.setText(_translate("Form", "Current:"))
        self.co2_6hour_label.setText(_translate("Form", "6 hr avg:"))
        self.co2_12hour_label.setText(_translate("Form", "12 hr avg:"))
        self.co2_24hour_label.setText(_translate("Form", "24 hr avg:"))
        self.co2_current.setText(_translate("Form", "0"))
        self.co2_6hour_avg.setText(_translate("Form", "0"))
        self.co2_12hour_avg.setText(_translate("Form", "0"))
        self.co2_24hour_avg.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Auto-Grow Averages"))

    def update_values(self):

        self.update_temperature()
        self.update_humidity()
        self.update_co2()

    # Updating temperature values
    def update_temperature(self):

        self.update_temperature_current()
        self.update_temperature_6hour()
        self.update_temperature_12hour()
        self.update_temperature_24hour()

    def validate_sensor_value(self, timestamp, sensor_value):

        reading_timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        now = datetime.now()

        time_since_last_reading = now - reading_timestamp
        if sensor_value is not None and time_since_last_reading.days == 0 and \
                time_since_last_reading.seconds <= 30:

            result = str(round(sensor_value, 2))

        else:

            result = "Invalid"

        return result

    def update_temperature_current(self):

        db_entry = database.get_most_recent_value("temperature")
        timestamp = db_entry[0]
        sensor_value = db_entry[1]

        self.temperature_current.setText(self.validate_sensor_value(timestamp, sensor_value))

    def update_temperature_6hour(self):

        value = round(database.get_average_value("temperature", 6), 2)
        self.temperature_6hour_avg.setText(str(value))

    def update_temperature_12hour(self):

        value = round(database.get_average_value("temperature", 12), 2)
        self.temperature_12hour_avg.setText(str(value))

    def update_temperature_24hour(self):

        value = round(database.get_average_value("temperature", 24), 2)
        self.temperature_24hour_avg.setText(str(value))


    # Updating humidity values
    def update_humidity(self):

        self.update_humidity_current()
        self.update_humidity_6hour()
        self.update_humidity_12hour()
        self.update_humidity_24hour()

    def update_humidity_current(self):

        db_entry = database.get_most_recent_value("humidity")
        timestamp = db_entry[0]
        sensor_value = db_entry[1]

        self.humidity_current.setText(self.validate_sensor_value(timestamp, sensor_value))

    def update_humidity_6hour(self):

        value = round(database.get_average_value("humidity", 6), 2)
        self.humidity_6hour_avg.setText(str(value))

    def update_humidity_12hour(self):

        value = round(database.get_average_value("humidity", 12), 2)
        self.humidity_12hour_avg.setText(str(value))

    def update_humidity_24hour(self):

        value = round(database.get_average_value("humidity", 24), 2)
        self.humidity_24hour_avg.setText(str(value))


    # Updating co2 values
    def update_co2(self):

        self.update_co2_current()
        self.update_co2_6hour()
        self.update_co2_12hour()
        self.update_co2_24hour()

    def update_co2_current(self):

        db_entry = database.get_most_recent_value("co2")
        timestamp = db_entry[0]
        sensor_value = db_entry[1]

        self.co2_current.setText(self.validate_sensor_value(timestamp, sensor_value))

    def update_co2_6hour(self):

        value = round(database.get_average_value("co2", 6), 2)
        self.co2_6hour_avg.setText(str(value))

    def update_co2_12hour(self):

        value = round(database.get_average_value("co2", 12), 2)
        self.co2_12hour_avg.setText(str(value))

    def update_co2_24hour(self):

        value = round(database.get_average_value("co2", 24), 2)
        self.co2_24hour_avg.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
