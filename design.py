from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.setWindowModality(Qt.WindowModality.WindowModal)
        main_window.resize(896, 594)
        main_window.setMouseTracking(False)
        main_window.setWindowOpacity(1.000000000000000)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet(u"background-color: #212529;")
        main_window.setDocumentMode(False)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.right_bar = QFrame(self.centralwidget)
        self.right_bar.setObjectName(u"right_bar")
        self.right_bar.setGeometry(QRect(610, 0, 281, 601))
        self.right_bar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.right_bar.setStyleSheet(u"background-color: #272b2f;\n"
"border-radius: 35px;\n"
"")
        self.right_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.username = QLabel(self.right_bar)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(10, 130, 171, 91))
        self.username.setStyleSheet(u"font-family: 'Inter', sans-serif;\n"
"font-size: 20px;\n"
"font-weight: 600;\n"
"color: #FFFFFF;\n"
"background-color: none;\n"
"")
        self.username.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 591, 311))
        self.bottom_bar = QFrame(self.centralwidget)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setGeometry(QRect(10, 330, 591, 261))
        self.bottom_bar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.bottom_bar.setStyleSheet(u"background-color: #272b2f;\n"
"border-radius: 35px;\n"
"")
        self.bottom_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottom_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.subtitle = QLabel(self.bottom_bar)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(0, 0, 591, 41))
        self.subtitle.setStyleSheet(u"font-family: 'Inter', sans-serif;\n"
"font-size: 20px;\n"
"font-weight: 600;\n"
"color: #FFFFFF;\n"
"background-color: none;\n"
"")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableWidget = QTableWidget(self.bottom_bar)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 571, 201))
        self.tableWidget.setStyleSheet('''
    QScrollBar:vertical {
        border: none;
        background: #212529; /* Fundo da barra de rolagem */
        width: 10px; /* Largura da barra */
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:vertical {
        background: #495057; /* Cor do controle deslizante */
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;
        height: 0px;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        border: none;
        background: #212529; /* Fundo da barra de rolagem */
        height: 10px; /* Altura da barra */
        margin: 0px 0px 0px 0px;
    }
    QScrollBar::handle:horizontal {
        background: #495057; /* Cor do controle deslizante */
        min-width: 20px;
        border-radius: 5px;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        background: none;
        width: 0px;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }
    QTableWidget {
        background-color: #272b2f; /* Fundo escuro */
        color: white; /* Texto branco */
        border: none;
        gridline-color: #444; /* Cor das linhas da grade */
      
    }
    QTableWidget::item:selected {
        background-color: #495057; /* Fundo do item selecionado */
        color: white; /* Cor do texto do item selecionado */
    }
    QHeaderView::section {
        background-color: #272b2f; /* Fundo dos cabeçalhos */
        color: white; /* Texto dos cabeçalhos */
        border: none;
    }
    QTableCornerButton::section {
        background-color: #272b2f; /* Cor escura para combinar com a tabela */
        border: none;
    }
''')

        self.tableWidget.setShowGrid(True)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Investpy", None))
        self.username.setText(QCoreApplication.translate("main_window", u"Pedro\n"
"Sanzio", None))
        self.subtitle.setText(QCoreApplication.translate("main_window", u"Ativos", None))
    # retranslateUi