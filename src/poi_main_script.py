from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Model import Model
import sys


class PoiMainWindow(QtWidgets.QMainWindow):
    """
    Programm um Points of interest zu verwalten

    Klasse welche alle Funktionen miteinander verbindet und die Kommunikation
    mit dem Frontend übernimmmt
    """
    model = None    # Referenz auf das Model
    file_name = "Test"  # Das file welches am Anfang eingelesen wird

    def __init__(self):
        """
        Klasse welche das User-Interface startet und die Knöpfe des Interfaces
        mit den Funktionen der Klasse verbindet
        """
        super(PoiMainWindow, self).__init__()
        self.form = uic.loadUi("main_window.ui", self)  # Referenz auf das File, welches das User-Interfaces beinhaltet
        self.model = Model()
        self.pushButton_main_load.clicked.connect(self.file_open_dialog)
        self.pushButton_main_save.clicked.connect(self.save_table_content_to_file)
        self.pushButton_main_create.clicked.connect(self.add_element_to_table)
        self.action_create_main.triggered.connect(self.add_element_to_table)
        self.action_delete_main.triggered.connect(self.delete_row_from_table)
        self.action_delete_all_main.triggered.connect(self.delete_every_row_from_table)
        self.action_main_close.triggered.connect(self.close)
        self.action_main_save_file.triggered.connect(self.save_table_content_to_file)
        self.action_main_load_file.triggered.connect(self.file_open_dialog)

    def closeEvent(self, event):
        """
        Funktion welche vor dem Beenden des Programms aufgerufen wird
        Benutzer wird gefragt ob dieser das Programm wirklich beenden will
        :param event: das Event welches beim schließen übergeben wird
        :return:
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warnung")
        msg_box.setText("Wollen Sie wirklich schließen?\n Daten, welche nicht gespeichert wurden, gehen verloren")
        msg_box.setDetailedText("Wenn Sie das Programm ohne zu speichern beenden, können Sie nicht mehr auf die verlorenen Daten zugreifen. Versichern Sie sich, dass wichtige Daten abgesichert wurden.")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return_value = msg_box.exec()
        if return_value == QMessageBox.Yes: # überprüfung was der Benutzer angeklicket hat
            event.accept()
        else:
            event.ignore()

    def file_open_dialog(self):
        """
        Funktion welche aufgerufen wird, wenn der Benutzer ein File einlesen möchte
        :return:
        """
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("POI File (*.upoi)")  # setzen der Dateiendung nach welcher gefiltert wird
        if file_dialog.exec_():
            self.file_name = file_dialog.selectedFiles()[0]
            self.model.read_file_content(self.file_name)
            self.print_to_table_in_form()

    def print_to_table_in_form(self):
        """
        Funktion welche die Daten auf die Tabelle ausgibt
        :return:
        """
        table = self.table_main_table
        self.model.print_content_from_list_to_table(table)

    def save_table_content_to_file(self):
        """
        Funktion welche alle Daten der Tabelle in ein File speichert welches der Benutzer angibt
        :return:
        """
        table = self.table_main_table
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Speichern", "", "POI File (*.upoi)")[0]
        if filename:
            self.model.save_table_content_to_file(filename, table)

    def delete_every_row_from_table(self):
        """
        Funktion welche die Tabelle komplett leert
        :return:
        """
        table = self.table_main_table
        self.model.delete_every_poi_from_table(table)

    def add_element_to_table(self):
        table = self.table_main_table
        self.model.add_new_element_to_table(table)

    def delete_row_from_table(self):
        """
        Funktion um eine Reihe aus der Tabelle zu löschen
        :return:
        """
        items = self.table_main_table.selectedItems()
        if len(items) != 1:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Fehler")
            msg_box.setText("Es muss ein Objekt ausgewählt werden")
            msg_box.setDetailedText("Dieser Fehler tritt auf, wenn keine oder zu viele Objekte ausgewählt wurden. Zur richtigen Verwendung nur ein Objekt auswählen")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
            return 0
        item = items[0]
        row_number = self.table_main_table.row(item)
        self.table_main_table.removeRow(row_number)

if __name__ == "__main__":
    # Funktion welche das ganze Programm startet
    app = QtWidgets.QApplication(sys.argv)
    window = PoiMainWindow()
    window.show()
    app.exec()
