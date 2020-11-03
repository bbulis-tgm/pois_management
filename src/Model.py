import csv
from POI import POI
from PyQt5 import QtWidgets

class Model:
    pois_objects = []

    def __init__(self):
        pass


    def read_file_content(self, fileName):
        with open(fileName, "r", encoding="utf-8") as file:
            content = csv.reader(file, delimiter='|')
            for row in content:
                self.transform_file_content_to_poi_object(row)

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