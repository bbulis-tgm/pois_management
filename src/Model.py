import csv
from POI import POI
from PyQt5.QtWidgets import QTableWidgetItem

class Model:
    pois_objects = []

    def __init__(self):
        pass

    def read_file_content(self, fileName):
        with open(fileName, "r", encoding="utf-8") as file:
            content = csv.reader(file, delimiter='|')
            for row in content:
                self.transform_file_content_to_poi_object(row)

    def save_table_content_to_file(self, filename, table):
        rowCount = table.rowCount()
        rowCounter = 0

        with open(filename, "w", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_NONE)
            while rowCounter < rowCount:
                category = table.item(rowCounter, 1).text()
                name = table.item(rowCounter, 0).text()
                icon = table.item(rowCounter, 11).text()
                lati = table.item(rowCounter, 2).text()
                long = table.item(rowCounter, 3).text()
                countrycode = table.item(rowCounter, 8).text()
                postalcode = table.item(rowCounter, 7).text()
                city = table.item(rowCounter, 6).text()
                street = table.item(rowCounter, 4).text()
                housenumber = table.item(rowCounter, 5).text()
                info = table.item(rowCounter, 10).text()
                phonenumber = table.item(rowCounter, 9).text()
                writer.writerow([rowCounter + 1,
                                 category,
                                 name,
                                 icon,
                                 lati,
                                 long,
                                 countrycode,
                                 '',
                                 '',
                                 '',
                                 postalcode,
                                 city,
                                 street,
                                 housenumber,
                                 info,
                                 phonenumber])
                rowCounter = rowCounter + 1

    def print_content_from_list_to_table(self, table):
        for idx, val in enumerate(self.pois_objects):
            table.insertRow(idx)
            table.setItem(idx, 0,QTableWidgetItem(val.get_name()))
            table.setItem(idx, 1, QTableWidgetItem(val.get_category()))
            table.setItem(idx, 2, QTableWidgetItem(val.get_lati()))
            table.setItem(idx, 3, QTableWidgetItem(val.get_long()))
            table.setItem(idx, 4, QTableWidgetItem(val.get_street()))
            table.setItem(idx, 5, QTableWidgetItem(val.get_housenumber()))
            table.setItem(idx, 6, QTableWidgetItem(val.get_city()))
            table.setItem(idx, 7, QTableWidgetItem(val.get_postalcode()))
            table.setItem(idx, 8, QTableWidgetItem(val.get_countrycode()))
            table.setItem(idx, 9, QTableWidgetItem(val.get_phone()))
            table.setItem(idx, 10, QTableWidgetItem(val.get_info()))
            table.setItem(idx, 11, QTableWidgetItem(val.get_icon()))

    def transform_file_content_to_poi_object(self, item):
        id = item[0]
        category = item[1]
        name = item[2]
        icon = item[3]
        lati = item[4]
        long = item[5]
        countrycode = item[6]
        postalcode = item[10]
        city = item[11]
        street = item[12]
        housenumber = item[13]
        info = item[14]
        phone = item[15]
        poi = POI(id, category, name, icon, lati, long, countrycode, postalcode, city, street, housenumber, info, phone)
        self.pois_objects.append(poi)

    def get_pois(self):
        return self.pois_objects

    def print_pois(self):
        for item in self.pois_objects:
            print(item.to_string())