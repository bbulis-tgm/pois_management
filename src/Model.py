import csv


class Model:
    pois = []

    def __init__(self):
        pass

    def read_file(self, fileName):
        print(self.pois)

    def get_pois(self):
        return self.pois

    def set_pois(self, pois):
        self.pois = pois

    def print_pois(self):
        print(self.pois)