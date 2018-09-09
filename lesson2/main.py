import sys
from ui_load import AgeWidget
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)
    menus = AgeWidget()
    sys.exit(app.exec_())