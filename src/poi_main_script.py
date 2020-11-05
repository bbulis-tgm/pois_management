from PyQt5 import QtWidgets, uic
from Model import Model
import sys


class PoiMainWindow(QtWidgets.QMainWindow):
    model = None
    file_name = "Test"

    def __init__(self):
        super(PoiMainWindow, self).__init__()
        self.form = uic.loadUi("main_window.ui", self)
        self.model = Model()
        self.pushButton_main_load.clicked.connect(self.file_open_dialog)
        self.pushButton_main_save.clicked.connect(self.save_table_content_to_file)

    def file_open_dialog(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("POI File (*.upoi)")
        if file_dialog.exec_():
            self.file_name = file_dialog.selectedFiles()[0]
            self.model.read_file_content(self.file_name)
            self.print_to_table_in_form()

    def print_to_table_in_form(self):
        table = self.table_main_table
        self.model.print_content_from_list_to_table(table)

    def save_table_content_to_file(self):
        table = self.table_main_table
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Speichern", "", "POI File (*.upoi)")[0]
        if filename:
            self.model.save_table_content_to_file(filename, table)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PoiMainWindow()
    window.show()
    app.exec()
