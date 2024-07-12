from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow
from path import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from display import Display
from buttons import Buttom, ButtonsGrid
from info import Info

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)



    window.adjustFixedSize()
    window.show()
    app.exec()
    