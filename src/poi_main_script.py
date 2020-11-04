from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
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
        objects_list = self.model.get_pois()
        for idx, val in enumerate(objects_list):
            self.table_main_table.insertRow(idx)
            self.table_main_table.setItem(idx, 0,QTableWidgetItem(val.get_name()))
            self.table_main_table.setItem(idx, 1, QTableWidgetItem(val.get_category()))
            self.table_main_table.setItem(idx, 2, QTableWidgetItem(val.get_lati()))
            self.table_main_table.setItem(idx, 3, QTableWidgetItem(val.get_long()))
            self.table_main_table.setItem(idx, 4, QTableWidgetItem(val.get_street()))
            self.table_main_table.setItem(idx, 5, QTableWidgetItem(val.get_housenumber()))
            self.table_main_table.setItem(idx, 6, QTableWidgetItem(val.get_city()))
            self.table_main_table.setItem(idx, 7, QTableWidgetItem(val.get_postalcode()))
            self.table_main_table.setItem(idx, 8, QTableWidgetItem(val.get_countrycode()))
            self.table_main_table.setItem(idx, 9, QTableWidgetItem(val.get_phone()))
            self.table_main_table.setItem(idx, 10, QTableWidgetItem(val.get_info()))
            self.table_main_table.setItem(idx, 11, QTableWidgetItem(val.get_icon()))

    def save_table_content_to_file(self):
        table = self.table_main_table
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "POI File (*.upoi)")[0]
        if filename:
            self.model.save_table_content_to_file(filename, table)

    # model = None
    # pois_list = []
    # pois_objects = []
    #
    # def __init__(self):
    #     super(PoiMainWindow, self).__init__()
    #     self.form = uic.loadUi("main_window.ui", self)
    #     self.model = Model()
    #     self.pushButton_main_load.clicked.connect(self.read_in_file)
    #
    #
    # def read_in_file(self):
    #     current_dir = os.getcwd()
    #     self.fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", current_dir, "POI File (*.upoi)")
    #     self.readFile(self.fileName[0])
    #
    # def readFile(self, fileName):
    #     with open(fileName, 'r', encoding="utf-8") as file:
    #         item = csv.reader(file, delimiter='|')
    #         for row in item:
    #             self.pois_list.append(row)
    #     for line in self.pois_list:
    #         self.trans_list_to_object(line)
    #     self.print_to_table()
    #
    # def trans_list_to_object(self, item):
    #     id = QTableWidgetItem(item[0])
    #     category = QTableWidgetItem(item[1])
    #     name = QTableWidgetItem(item[2])
    #     icon = QTableWidgetItem(item[3])
    #     lati = QTableWidgetItem(item[4])
    #     long = QTableWidgetItem(item[5])
    #     countrycode = QTableWidgetItem(item[6])
    #     postalcode = QTableWidgetItem(item[10])
    #     city = QTableWidgetItem(item[11])
    #     street = QTableWidgetItem(item[12])
    #     housenumber = QTableWidgetItem(item[13])
    #     info = QTableWidgetItem(item[14])
    #     phone = QTableWidgetItem(item[15])
    #     poi = POI(id, category, name, icon, lati, long, countrycode, postalcode, city, street, housenumber, info, phone)
    #     self.pois_objects.append(poi)
    #
    # def print_to_table(self):
    #     for idx, val in enumerate(self.pois_objects):
    #         self.table_main_table.insertRow(idx)
    #         self.table_main_table.setItem(idx, 0,val.get_name())
    #         self.table_main_table.setItem(idx, 1, val.get_category())
    #         self.table_main_table.setItem(idx, 2, val.get_lati())
    #         self.table_main_table.setItem(idx, 3, val.get_long())
    #         self.table_main_table.setItem(idx, 4, val.get_street())
    #         self.table_main_table.setItem(idx, 5, val.get_housenumber())
    #         self.table_main_table.setItem(idx, 6, val.get_city())
    #         self.table_main_table.setItem(idx, 7, val.get_postalcode())
    #         self.table_main_table.setItem(idx, 8, val.get_countrycode())
    #         self.table_main_table.setItem(idx, 9, val.get_phone())
    #         self.table_main_table.setItem(idx, 10, val.get_info())
    #
    # def save_in_file(self):
    #     rows = self.table_main_table.rowCount()
    #     columns = self.table_main_table.columnCount()
    #     idCount = rows + 1
    #
    #     with open(self.fileName[0], 'w', newline='') as spamfile:
    #         writer = csv.writer(spamfile, delimiter='|')
    #         rowCount = 0
    #         while rowCount < rows:
    #             columnCount = 0
    #             while columnCount < 0:
    #                 pass
    #


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PoiMainWindow()
    window.show()
    app.exec()
