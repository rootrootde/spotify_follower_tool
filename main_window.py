# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(518, 657)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.group_box_api = QGroupBox(self.centralwidget)
        self.group_box_api.setObjectName(u"group_box_api")
        self.gridLayout = QGridLayout(self.group_box_api)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_settings = QPushButton(self.group_box_api)
        self.btn_settings.setObjectName(u"btn_settings")

        self.gridLayout.addWidget(self.btn_settings, 1, 0, 1, 1)

        self.btn_auth = QPushButton(self.group_box_api)
        self.btn_auth.setObjectName(u"btn_auth")
        self.btn_auth.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_auth.sizePolicy().hasHeightForWidth())
        self.btn_auth.setSizePolicy(sizePolicy1)
        self.btn_auth.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btn_auth, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.group_box_api, 0, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tbl_artists = QTableWidget(self.centralwidget)
        if (self.tbl_artists.columnCount() < 4):
            self.tbl_artists.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_artists.setObjectName(u"tbl_artists")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tbl_artists.sizePolicy().hasHeightForWidth())
        self.tbl_artists.setSizePolicy(sizePolicy2)
        self.tbl_artists.setMinimumSize(QSize(450, 0))
        font = QFont()
        font.setPointSize(12)
        self.tbl_artists.setFont(font)
        self.tbl_artists.setFrameShape(QFrame.Box)
        self.tbl_artists.setFrameShadow(QFrame.Sunken)
        self.tbl_artists.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbl_artists.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_artists.setAlternatingRowColors(True)
        self.tbl_artists.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_artists.setShowGrid(False)
        self.tbl_artists.setSortingEnabled(True)
        self.tbl_artists.setCornerButtonEnabled(True)
        self.tbl_artists.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_artists.horizontalHeader().setMinimumSectionSize(0)
        self.tbl_artists.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_artists.horizontalHeader().setStretchLastSection(True)
        self.tbl_artists.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tbl_artists, 0, 0, 1, 2)

        self.btn_select_playlists = QPushButton(self.centralwidget)
        self.btn_group = QButtonGroup(MainWindow)
        self.btn_group.setObjectName(u"btn_group")
        self.btn_group.addButton(self.btn_select_playlists)
        self.btn_select_playlists.setObjectName(u"btn_select_playlists")

        self.gridLayout_3.addWidget(self.btn_select_playlists, 1, 0, 1, 1)

        self.btn_unfollow_all = QPushButton(self.centralwidget)
        self.btn_group.addButton(self.btn_unfollow_all)
        self.btn_unfollow_all.setObjectName(u"btn_unfollow_all")

        self.gridLayout_3.addWidget(self.btn_unfollow_all, 2, 1, 1, 1)

        self.btn_clear_list = QPushButton(self.centralwidget)
        self.btn_group.addButton(self.btn_clear_list)
        self.btn_clear_list.setObjectName(u"btn_clear_list")

        self.gridLayout_3.addWidget(self.btn_clear_list, 2, 0, 1, 1)

        self.btn_follow_all = QPushButton(self.centralwidget)
        self.btn_group.addButton(self.btn_follow_all)
        self.btn_follow_all.setObjectName(u"btn_follow_all")

        self.gridLayout_3.addWidget(self.btn_follow_all, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 518, 22))
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setEnabled(True)
        font1 = QFont()
        font1.setBold(False)
        self.status_bar.setFont(font1)
        self.status_bar.setAutoFillBackground(False)
        self.status_bar.setStyleSheet(u"background-color: rgba(29, 185, 84, 192)")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spotify Follow Tool", None))
        self.group_box_api.setTitle(QCoreApplication.translate("MainWindow", u"API Connection", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_auth.setText(QCoreApplication.translate("MainWindow", u"Login as...", None))
        ___qtablewidgetitem = self.tbl_artists.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Following", None));
        ___qtablewidgetitem1 = self.tbl_artists.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Link", None));
        ___qtablewidgetitem2 = self.tbl_artists.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Artist", None));
        ___qtablewidgetitem3 = self.tbl_artists.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.btn_select_playlists.setText(QCoreApplication.translate("MainWindow", u"Select Playlists", None))
        self.btn_unfollow_all.setText(QCoreApplication.translate("MainWindow", u"Unfollow All", None))
        self.btn_clear_list.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.btn_follow_all.setText(QCoreApplication.translate("MainWindow", u"Follow All", None))
    # retranslateUi

