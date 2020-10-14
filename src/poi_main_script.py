from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from Model import Model
from POI import POI
import os
import sys
import csv


class PoiMainWindow(QtWidgets.QMainWindow):
    model = None
    pois_list = []
    pois_objects = []

    def __init__(self):
        super(PoiMainWindow, self).__init__()
        self.form = uic.loadUi("main_window.ui", self)
        self.model = Model()
        self.pushButton_main_load.clicked.connect(self.read_in_file)


    def read_in_file(self):
        current_dir = os.getcwd()
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", current_dir, "POI File (*.upoi)")
        self.readFile(self.fileName[0])

    def readFile(self, fileName):
        with open(fileName, 'r', encoding="utf-8") as file:
            item = csv.reader(file, delimiter='|')
            for row in item:
                self.pois_list.append(row)
        for line in self.pois_list:
            self.trans_list_to_object(line)
        self.print_to_table()

    def trans_list_to_object(self, item):
        id = QTableWidgetItem(item[0])
        category = QTableWidgetItem(item[1])
        name = QTableWidgetItem(item[2])
        icon = QTableWidgetItem(item[3])
        lati = QTableWidgetItem(item[4])
        long = QTableWidgetItem(item[5])
        countrycode = QTableWidgetItem(item[6])
        postalcode = QTableWidgetItem(item[10])
        city = QTableWidgetItem(item[11])
        street = QTableWidgetItem(item[12])
        housenumber = QTableWidgetItem(item[13])
        info = QTableWidgetItem(item[14])
        phone = QTableWidgetItem(item[15])
        poi = POI(id, category, name, icon, lati, long, countrycode, postalcode, city, street, housenumber, info, phone)
        self.pois_objects.append(poi)

    def print_to_table(self):
        for idx, val in enumerate(self.pois_objects):
            self.table_main_table.insertRow(idx)
            self.table_main_table.setItem(idx, 0,val.get_name())
            self.table_main_table.setItem(idx, 1, val.get_category())
            self.table_main_table.setItem(idx, 2, val.get_lati())
            self.table_main_table.setItem(idx, 3, val.get_long())
            self.table_main_table.setItem(idx, 4, val.get_street())
            self.table_main_table.setItem(idx, 5, val.get_housenumber())
            self.table_main_table.setItem(idx, 6, val.get_city())
            self.table_main_table.setItem(idx, 7, val.get_postalcode())
            self.table_main_table.setItem(idx, 8, val.get_countrycode())
            self.table_main_table.setItem(idx, 9, val.get_phone())
            self.table_main_table.setItem(idx, 10, val.get_info())

    def save_in_file(self):
        rows = self.table_main_table.rowCount()
        columns = self.table_main_table.columnCount()
        idCount = rows + 1

        with open(self.fileName[0], 'w', newline='') as spamfile:
            writer = csv.writer(spamfile, delimiter='|')
            rowCount = 0
            while rowCount < rows:
                columnCount = 0
                while columnCount < 0:
                    pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PoiMainWindow()
    window.show()
    app.exec()
