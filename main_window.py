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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(427, 818)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.le_client_id = QLineEdit(self.groupBox)
        self.le_client_id.setObjectName(u"le_client_id")

        self.gridLayout.addWidget(self.le_client_id, 0, 1, 1, 1)

        self.btn_auth = QPushButton(self.groupBox)
        self.btn_auth.setObjectName(u"btn_auth")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_auth.sizePolicy().hasHeightForWidth())
        self.btn_auth.setSizePolicy(sizePolicy)
        self.btn_auth.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btn_auth, 0, 2, 3, 1)

        self.le_client_secret = QLineEdit(self.groupBox)
        self.le_client_secret.setObjectName(u"le_client_secret")

        self.gridLayout.addWidget(self.le_client_secret, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)

        self.tbl_artists = QTableWidget(self.centralwidget)
        if (self.tbl_artists.columnCount() < 3):
            self.tbl_artists.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_artists.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tbl_artists.setObjectName(u"tbl_artists")
        self.tbl_artists.setFrameShape(QFrame.Box)
        self.tbl_artists.setFrameShadow(QFrame.Sunken)
        self.tbl_artists.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_artists.setAlternatingRowColors(True)
        self.tbl_artists.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_artists.setTextElideMode(Qt.ElideMiddle)
        self.tbl_artists.setSortingEnabled(True)
        self.tbl_artists.setWordWrap(True)
        self.tbl_artists.setCornerButtonEnabled(True)
        self.tbl_artists.horizontalHeader().setVisible(True)
        self.tbl_artists.horizontalHeader().setHighlightSections(True)
        self.tbl_artists.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_artists.horizontalHeader().setStretchLastSection(True)
        self.tbl_artists.verticalHeader().setVisible(False)
        self.tbl_artists.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.tbl_artists, 1, 0, 1, 3)

        self.btn_follow_all = QPushButton(self.centralwidget)
        self.btn_follow_all.setObjectName(u"btn_follow_all")

        self.gridLayout_2.addWidget(self.btn_follow_all, 2, 2, 1, 1)

        self.btn_unfollow_all = QPushButton(self.centralwidget)
        self.btn_unfollow_all.setObjectName(u"btn_unfollow_all")

        self.gridLayout_2.addWidget(self.btn_unfollow_all, 2, 1, 1, 1)

        self.btn_select_playlists = QPushButton(self.centralwidget)
        self.btn_select_playlists.setObjectName(u"btn_select_playlists")

        self.gridLayout_2.addWidget(self.btn_select_playlists, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 427, 22))
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setEnabled(True)
        font = QFont()
        font.setBold(True)
        self.status_bar.setFont(font)
        self.status_bar.setStyleSheet(u"background-color: rgb(29, 185, 84);")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spotify Follow Tool", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"API Connection", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Client Secret", None))
        self.btn_auth.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Client ID", None))
        ___qtablewidgetitem = self.tbl_artists.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Following", None));
        ___qtablewidgetitem1 = self.tbl_artists.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Artist", None));
        ___qtablewidgetitem2 = self.tbl_artists.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.btn_follow_all.setText(QCoreApplication.translate("MainWindow", u"Follow All", None))
        self.btn_unfollow_all.setText(QCoreApplication.translate("MainWindow", u"Unfollow All", None))
        self.btn_select_playlists.setText(QCoreApplication.translate("MainWindow", u"Select Playlists", None))
    # retranslateUi

