# -*- coding: utf-8 -*-

# AutoGrow_Averages implementation generated from reading ui file 'Desktop/auto_grow_ui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from datetime import datetime, timedelta
from typing import Union

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QTimer

import database


class Ui_AutoGrow_Averages(object):
    def setupUi(self, AutoGrow_Averages):
        AutoGrow_Averages.setObjectName("Auto-Grow Averages")
        AutoGrow_Averages.resize(400, 310)
        AutoGrow_Averages.setMinimumSize(QtCore.QSize(400, 310))
        AutoGrow_Averages.setMaximumSize(QtCore.QSize(400, 310))
        self.frame = QtWidgets.QFrame(AutoGrow_Averages)
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
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 181, 224))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 70)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, -1, -1, 20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.state_indicator_label_4x4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.state_indicator_label_4x4.setFont(font)
        self.state_indicator_label_4x4.setObjectName("state_indicator_label_4x4")
        self.verticalLayout_13.addWidget(self.state_indicator_label_4x4)
        self.state_indicator_label_4x8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.state_indicator_label_4x8.setFont(font)
        self.state_indicator_label_4x8.setObjectName("state_indicator_label_4x8")
        self.verticalLayout_13.addWidget(self.state_indicator_label_4x8)
        self.state_indicator_label_blower = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.state_indicator_label_blower.setFont(font)
        self.state_indicator_label_blower.setObjectName("state_indicator_label_blower")
        self.verticalLayout_13.addWidget(self.state_indicator_label_blower)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_13.addWidget(self.label_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(-1, 2, -1, 2)
        self.verticalLayout_15.setSpacing(11)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.state_indicator_4x4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.state_indicator_4x4.setMinimumSize(QtCore.QSize(0, 6))
        self.state_indicator_4x4.setStyleSheet("background-color:rgb(252, 0, 9);border-radius: 4px;")
        self.state_indicator_4x4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.state_indicator_4x4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.state_indicator_4x4.setObjectName("state_indicator_4x4")
        self.verticalLayout_15.addWidget(self.state_indicator_4x4)
        self.state_indicator_4x8 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.state_indicator_4x8.setMinimumSize(QtCore.QSize(0, 6))
        self.state_indicator_4x8.setStyleSheet("background-color:rgb(252, 0, 9);border-radius: 4px;")
        self.state_indicator_4x8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.state_indicator_4x8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.state_indicator_4x8.setObjectName("state_indicator_4x8")
        self.verticalLayout_15.addWidget(self.state_indicator_4x8)
        self.state_indicator_blower = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.state_indicator_blower.setMinimumSize(QtCore.QSize(0, 6))
        self.state_indicator_blower.setStyleSheet("background-color:rgb(252, 0, 9);border-radius: 4px;")
        self.state_indicator_blower.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.state_indicator_blower.setFrameShadow(QtWidgets.QFrame.Raised)
        self.state_indicator_blower.setObjectName("state_indicator_blower")
        self.verticalLayout_15.addWidget(self.state_indicator_blower)
        self.state_indicator_co2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.state_indicator_co2.setMinimumSize(QtCore.QSize(0, 6))
        self.state_indicator_co2.setStyleSheet("background-color:rgb(252, 0, 9);border-radius: 4px;")
        self.state_indicator_co2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.state_indicator_co2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.state_indicator_co2.setObjectName("state_indicator_co2")
        self.verticalLayout_15.addWidget(self.state_indicator_co2)
        self.state_indicator_heater = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.state_indicator_heater.setMinimumSize(QtCore.QSize(0, 6))
        self.state_indicator_heater.setStyleSheet("background-color:rgb(252, 0, 9);border-radius: 4px;")
        self.state_indicator_heater.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.state_indicator_heater.setFrameShadow(QtWidgets.QFrame.Raised)
        self.state_indicator_heater.setObjectName("state_indicator_heater")
        self.verticalLayout_15.addWidget(self.state_indicator_heater)
        self.horizontalLayout_6.addLayout(self.verticalLayout_15)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(AutoGrow_Averages)
        QtCore.QMetaObject.connectSlotsByName(AutoGrow_Averages)
        self._timer_painter = QTimer(AutoGrow_Averages)
        self._timer_painter.start(5000)
        self._timer_painter.timeout.connect(self.update_values)

    def retranslateUi(self, AutoGrow_Averages):
        _translate = QtCore.QCoreApplication.translate
        AutoGrow_Averages.setWindowTitle(_translate("AutoGrow Averages", "AutoGrow Averages"))
        self.temperature_main_label.setText(_translate("AutoGrow_Averages", "Temperature"))
        self.temperature_current_label.setText(_translate("AutoGrow_Averages", "Current:"))
        self.temperature_6hour_label.setText(_translate("AutoGrow_Averages", "6 hr avg:"))
        self.temperature_12hour_label.setText(_translate("AutoGrow_Averages", "12 hr avg:"))
        self.temperature_24hour_label.setText(_translate("AutoGrow_Averages", "24 hr avg:"))
        self.temperature_current.setText(_translate("AutoGrow_Averages", "0"))
        self.temperature_6hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.temperature_12hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.temperature_24hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.humidity_main_label.setText(_translate("AutoGrow_Averages", "Humidity"))
        self.humidity_current_label.setText(_translate("AutoGrow_Averages", "Current:"))
        self.humidity_6hour_label.setText(_translate("AutoGrow_Averages", "6 hr avg:"))
        self.humidity_12hour_label.setText(_translate("AutoGrow_Averages", "12 hr avg:"))
        self.humidity_24hour_label.setText(_translate("AutoGrow_Averages", "24 hr avg:"))
        self.humidity_current.setText(_translate("AutoGrow_Averages", "0"))
        self.humidity_6hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.humidity_12hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.humidity_24hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.co2_main_label.setText(_translate("AutoGrow_Averages", "CO2"))
        self.co2_current_label.setText(_translate("AutoGrow_Averages", "Current:"))
        self.co2_6hour_label.setText(_translate("AutoGrow_Averages", "6 hr avg:"))
        self.co2_12hour_label.setText(_translate("AutoGrow_Averages", "12 hr avg:"))
        self.co2_24hour_label.setText(_translate("AutoGrow_Averages", "24 hr avg:"))
        self.co2_current.setText(_translate("AutoGrow_Averages", "0"))
        self.co2_6hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.co2_12hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.co2_24hour_avg.setText(_translate("AutoGrow_Averages", "0"))
        self.label.setText(_translate("AutoGrow_Averages", "Other States"))
        self.state_indicator_label_4x4.setText(_translate("AutoGrow_Averages", "4x4*"))
        self.state_indicator_label_4x8.setText(_translate("AutoGrow_Averages", "4x8"))
        self.state_indicator_label_blower.setText(_translate("AutoGrow_Averages", "Blower"))
        self.label_2.setText(_translate("AutoGrow_Averages", "CO2"))
        self.label_3.setText(_translate("AutoGrow_Averages", "Heater"))

    def update_values(self):

        self.update_temperature()
        self.update_humidity()
        self.update_co2()
        self.update_output_states()

    # Updating temperature values
    def update_temperature(self):

        self.update_temperature_current()
        self.update_temperature_6hour()
        self.update_temperature_12hour()
        self.update_temperature_24hour()

    def validate_sensor_value(self, query_result):

        if query_result is not None:
            timestamp = query_result[0]
            sensor_value = query_result[1]

        else:
            return "Invalid"

        reading_timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        now = datetime.now()

        time_since_last_reading = now - reading_timestamp
        if sensor_value is not None and time_since_last_reading.days == 0 and \
                time_since_last_reading.seconds <= 30:

            result = round(sensor_value, 2)

        else:

            result = "Invalid"

        return result

    def update_temperature_current(self):

        db_entry = database.get_most_recent_value("temperature")
        self.update_text(self.temperature_current, self.validate_sensor_value(db_entry))

    def update_temperature_6hour(self):

        value = database.get_average_value("temperature", 6)
        self.update_text(self.temperature_6hour_avg, value)

    def update_temperature_12hour(self):

        value = database.get_average_value("temperature", 12)
        self.update_text(self.temperature_12hour_avg, value)

    def update_temperature_24hour(self):

        value = database.get_average_value("temperature", 24)
        self.update_text(self.temperature_24hour_avg, value)


    # Updating humidity values
    def update_humidity(self):

        self.update_humidity_current()
        self.update_humidity_6hour()
        self.update_humidity_12hour()
        self.update_humidity_24hour()

    def update_humidity_current(self):

        query_result = database.get_most_recent_value("humidity")
        self.update_text(self.humidity_current, self.validate_sensor_value(query_result))

    def update_humidity_6hour(self):

        value = database.get_average_value("humidity", 6)
        self.update_text(self.humidity_6hour_avg, value)

    def update_humidity_12hour(self):

        value = database.get_average_value("humidity", 12)
        self.update_text(self.humidity_12hour_avg, value)

    def update_humidity_24hour(self):

        value = database.get_average_value("humidity", 24)
        self.update_text(self.humidity_24hour_avg, value)


    # Updating co2 values
    def update_co2(self):

        self.update_co2_current()
        self.update_co2_6hour()
        self.update_co2_12hour()
        self.update_co2_24hour()

    def update_co2_current(self):

        query_result = database.get_most_recent_value("co2")
        self.update_text(self.co2_current, self.validate_sensor_value(query_result))

    def update_co2_6hour(self):

        value = database.get_average_value("co2", 6)
        self.update_text(self.co2_6hour_avg, value)

    def update_co2_12hour(self):

        value = database.get_average_value("co2", 12)
        self.update_text(self.co2_12hour_avg, value)

    def update_co2_24hour(self):

        value = database.get_average_value("co2", 24)
        self.update_text(self.co2_24hour_avg, value)

    @staticmethod
    def update_text(ui_component, value: Union[int, float, str]):

        if value is not None and type(value) is not str:
            value = round(value, 2)
        else:
            value = "Invalid"

        ui_component.setText(str(value))

    def update_output_states(self):

        self.update_lights_4x4_state()
        self.update_lights_4x8_state()
        self.update_exhaust_state()
        self.update_co2_state()
        self.update_heater_state()

    def update_lights_4x4_state(self):

        query_result = database.get_output_state("lights_4x4")
        if query_result is not None:
            state = query_result[1]
            timestamp = query_result[0]

            now = datetime.now()
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
            time_diff = now - timestamp

            if time_diff.days >= 0 and time_diff.seconds > 30:
                self.state_indicator_4x4.setStyleSheet("background-color:black;border-radius:4px;")

            elif state == "True":
                self.state_indicator_4x4.setStyleSheet("background-color:rgb(76, 255, 35);border-radius:4px;")

            else:
                self.state_indicator_4x4.setStyleSheet("background-color:rgb(252, 0, 9);border-radius:4px;")

        else:
            self.state_indicator_4x4.setStyleSheet("background-color:rgb(255, 246, 18);border-radius:4px;")

    def update_lights_4x8_state(self):

        query_result = database.get_output_state("lights_4x8")
        if query_result is not None:
            state = query_result[1]
            timestamp = query_result[0]

            now = datetime.now()
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
            time_diff = now - timestamp

            if time_diff.days >= 0 and time_diff.seconds > 30:
                self.state_indicator_4x8.setStyleSheet("background-color:black;border-radius:4px;")

            elif state == "True":
                self.state_indicator_4x8.setStyleSheet("background-color:rgb(76, 255, 35);border-radius:4px;")

            else:
                self.state_indicator_4x8.setStyleSheet("background-color:rgb(252, 0, 9);border-radius:4px;")

        else:
            self.state_indicator_4x8.setStyleSheet("background-color:rgb(255, 246, 18);border-radius:4px;")

    def update_exhaust_state(self):

        query_result = database.get_output_state("exhaust_fan")
        if query_result is not None:
            state = query_result[1]
            timestamp = query_result[0]

            now = datetime.now()
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
            time_diff = now - timestamp

            if time_diff.days >= 0 and time_diff.seconds > 30:
                self.state_indicator_blower.setStyleSheet("background-color:black;border-radius:4px;")
            elif state == "True":
                self.state_indicator_blower.setStyleSheet("background-color:rgb(76, 255, 35);border-radius:4px;")

            else:
                self.state_indicator_blower.setStyleSheet("background-color:rgb(252, 0, 9);border-radius:4px;")

        else:
            self.state_indicator_blower.setStyleSheet("background-color:rgb(255, 246, 18);border-radius:4px;")

    def update_heater_state(self):

        query_result = database.get_output_state("heater")
        if query_result is not None:
            state = query_result[1]
            timestamp = query_result[0]

            now = datetime.now()
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
            time_diff = now - timestamp

            if time_diff.days >= 0 and time_diff.seconds > 30:
                self.state_indicator_heater.setStyleSheet("background-color:black;border-radius:4px;")
            elif state == "True":
                self.state_indicator_heater.setStyleSheet("background-color:rgb(76, 255, 35);border-radius:4px;")

            else:
                self.state_indicator_heater.setStyleSheet("background-color:rgb(252, 0, 9);border-radius:4px;")

        else:
            self.state_indicator_heater.setStyleSheet("background-color:rgb(255, 246, 18);border-radius:4px;")

    def update_co2_state(self):

        query_result = database.get_output_state("co2")
        if query_result is not None:

            state = query_result[1]
            timestamp = query_result[0]

            now = datetime.now()
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
            time_diff = now - timestamp

            if time_diff.days >= 0 and time_diff.seconds > 30:
                self.state_indicator_co2.setStyleSheet("background-color:black;border-radius:4px;")
            elif state == "True":
                self.state_indicator_co2.setStyleSheet("background-color:rgb(76, 255, 35);border-radius:4px;")

            else:
                self.state_indicator_co2.setStyleSheet("background-color:rgb(252, 0, 9);border-radius:4px;")

        else:
            self.state_indicator_co2.setStyleSheet("background-color:rgb(255, 246, 18);border-radius:4px;")

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoGrow_Averages = QtWidgets.QWidget()
    ui = Ui_AutoGrow_Averages()
    ui.setupUi(AutoGrow_Averages)
    AutoGrow_Averages.show()
    sys.exit(app.exec_())
