import csv
from PyQt5.QtWidgets import QFileDialog


class Model:
    pois = []

    def __init__(self):
        pass

    def read_file(self, fileName):
        with open(fileName, 'r', encoding="utf-8") as file:
            item = csv.reader(file, delimiter='|')
            for row in item:
                self.pois.append(row)

        print(self.pois)

    def get_pois(self):
        return self.pois

    def set_pois(self, pois):
        self.pois = pois