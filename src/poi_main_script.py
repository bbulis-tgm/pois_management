from PyQt5 import QtWidgets, uic
from Model import Model
import os
import sys

class PoiMainWindow (QtWidgets.QMainWindow):

    model = None
    csv_file = None

    def __init__(self):
        super(PoiMainWindow, self).__init__()
        self.form = uic.loadUi("main_window.ui", self)
        self.model = Model()
        self.pushButton_main_load.clicked.connect(self.read_in_file)
        self.model.read_file()

    def read_in_file(self):
        current_dir = os.getcwd()
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, str("Open File"), current_dir, str("POI File (*.ipoi"))
        self.model.read_file(fileName)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PoiMainWindow()
    window.show()
    app.exec()