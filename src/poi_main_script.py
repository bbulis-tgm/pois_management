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
        self.action_delete_main.triggered.connect(self.delete_row_from_table)
        self.action_delete_all_main.triggered.connect(self.delete_every_row_from_table)

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

    def delete_every_row_from_table(self):
        table = self.table_main_table
        self.model.delete_every_poi_from_table(table)

    def delete_row_from_table(self):
        items = self.table_main_table.selectedItems()
        if len(items) is not 1:
            return 0
        item = items[0]
        row_number = self.table_main_table.row(item)
        self.table_main_table.removeRow(row_number)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PoiMainWindow()
    window.show()
    app.exec()
