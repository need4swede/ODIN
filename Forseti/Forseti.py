# #################################################################
# File name:    Forseti.py
# Author:       Need4Swede
# Contact:      theneed4swede@gmail.com
# Description:  Crafting Tool for ODIN's Týr Module
# #################################################################

import darkdetect
import os, sys, platform, string, os.path, shutil
from PyQt6 import *
from datetime import date
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
app_modules = True
global root_dir
if app_modules:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path_parent = os.path.dirname(os.getcwd())
    root_dir = path_parent + "/ODIN"
    sys.path.append('../ODIN')
    from Tyr.clear_term import clear_term
    clear_term()

Forseti = False
if Forseti:
    with open('Tyr/Týr.py', 'r') as file:
        data = file.readlines()

    print("Options: \n1. main_labels \n2. drop_labels \n3. drop_sub_labels" 
        + "\n")
    mainChangeWhat = input("What would you like to change: ")
    if '1' in mainChangeWhat:
        clear_term()
        print("Options: \n0. Reset to Default \n1. lb_site \n2.lb_location \n3.lb_product \n4.lb_make" 
        + "\n")
        changeWhatMainLabel = input("What 'main_label' would you like to change: ")
        if '0' in changeWhatMainLabel:
            chosen_change = 'main_labels'
            print()
            confirm_change = input(f"Set {chosen_change} to Týr default - y / n?: ")
            if 'y' or 'Y' in confirm_change:
                try:
                    data[99] = f'    lb_id = "ID #:"\n'
                    data[100] = f'    lb_site = "Site:"\n'
                    data[101] = f'    lb_location = "Location:"\n'
                    data[102] = f'    lb_product = "Selection:"\n'
                    data[103] = f'    lb_make = "Make:"\n'
                finally:
                    clear_term()
                    print(f"\nReset Complete")
        elif '1' in changeWhatMainLabel:
            newSite = input("Change 'Site' to: ")
            print()
            confirm_change = input(f"Changing 'lb_site' from 'Site' to '{newSite}' - y / n?: ")
            if 'y' or 'Y' in confirm_change:
                data[100] = f'    lb_site = "{newSite}:"\n'
                print("\nLabel changed successfully!")
        elif '4' in changeWhatMainLabel:
            newMake = input("Change 'Make' to: ")
            print()
            confirm_change = input(f"Changing 'lb_make' from 'Make' to '{newMake}' - y / n?: ")
            if 'y' or 'Y' in confirm_change:
                data[103] = f'    lb_make = "{newMake}:"\n'
                print("\nLabel changed successfully!")

    with open('Tyr/Týr.py', 'w') as file:
        file.writelines(data)

# #################################################################
# File name:    Týr.py
# Author:       Need4Swede
# Description:  Omniscient Database for Inventory Notation
# #################################################################

## LIBRARY IMPORTS ################################################
import darkdetect
import os, sqlite3, sys, platform, string, os.path, webbrowser, shutil, csv
import pandas as pd
from fpdf import FPDF
from PyQt6 import *
from csv import reader
from datetime import date
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
## USER DIRECTORY IMPORTS #########################################
app_modules = True
if app_modules:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path_parent = os.path.dirname(os.getcwd())
    root_dir = path_parent + "/ODIN"
    sys.path.append('../ODIN')
    import Mimisbrunnr.Mimisbrunnr_1 as Mimisbrunnr_1 
    import Mimisbrunnr.Mimisbrunnr_2 as Mimisbrunnr_2
    from Tyr.clear_term import clear_term                        
    with open(root_dir + "/Tyr/users.csv", 'r') as read_obj:
        csv_reader = reader(read_obj)
        ad_users = list(csv_reader)
        length = len(ad_users)
        user_list = ["Assign To...", "To Realm"]
        for x in range(length):
            user_list = user_list + ad_users[x]
###################################################################
## DIRECTORIES ####################################################
global inventory_db
app_dir = True
if app_dir:
    documentation_dir = (root_dir + "/Documentation")
    mimir_dir = (root_dir + "/Mimir")
    forseti_dir = (root_dir + "/Forseti")
    forseti_mimir_dir = (forseti_dir + "/Mimir")
    forseti_mimir = (forseti_mimir_dir + "/Mimir.db")
    mimisbrunnr_dir = (root_dir + "/Mimisbrunnr")
    mimisbrunnr_export_dir = (mimisbrunnr_dir + "/exports/")
    tyr_dir = (root_dir + "/Tyr")
    if not os.path.isdir(mimir_dir):
        os.makedirs(mimir_dir)
    if os.path.isdir(documentation_dir):
        if os.path.isdir(mimir_dir + "/Documentation"):
            shutil.rmtree(mimir_dir + "/Documentation")
        shutil.copytree(documentation_dir, mimir_dir + "/Documentation")
        shutil.rmtree(documentation_dir) 
    inventory_db = mimir_dir + "/Mimir.db"
    date_today = date.today()
    today = date_today.strftime("%B %d,  %Y")
    clean_dir = True
if clean_dir:
    if os.path.isdir(root_dir + "/__pycache__"):
        shutil.rmtree(root_dir + "/__pycache__")
    shutil.rmtree(mimisbrunnr_dir + "/__pycache__")
    shutil.rmtree(tyr_dir + "/__pycache__")
## ICONS/IMAGES  ##############
app_icons = True
if app_icons:
    png_lab = root_dir + "/Tyr/Icons/lab.png"
    png_add = root_dir + "/Tyr/Icons/add.png"
    png_delete = root_dir + "/Tyr/Icons/delete.png"
    png_search = root_dir + "/Tyr/Icons/search.png"
    png_run = root_dir + "/Tyr/Icons/run.png"
    png_info = root_dir + "/Tyr/Icons/information.png"
    png_view = root_dir + "/Tyr/Icons/view.png"
    png_export = root_dir + "/Tyr/Icons/export.png"
    png_clear = root_dir + "/Tyr/Icons/clear.png"
    png_refresh = root_dir + "/Tyr/Icons/refresh.png"
    png_update = root_dir + "/Tyr/Icons/update.png"
    png_move = root_dir + "/Tyr/Icons/move.png"
    png_logo = root_dir + "/Tyr/Icons/forseti-icon.png"
    png_db_primary = root_dir + "/Tyr/Icons/forseti-icon.png"
if darkdetect.isDark():
    png_lab = root_dir + "/Tyr/Icons/dark/lab.png"
    png_add = root_dir + "/Tyr/Icons/dark/add.png"
    png_delete = root_dir + "/Tyr/Icons/dark/delete.png"
    png_search = root_dir + "/Tyr/Icons/dark/search.png"
    png_run = root_dir + "/Tyr/Icons/dark/run.png"
    png_info = root_dir + "/Tyr/Icons/dark/information.png"
    png_view = root_dir + "/Tyr/Icons/dark/view.png"
    png_export = root_dir + "/Tyr/Icons/dark/export.png"
    png_clear = root_dir + "/Tyr/Icons/dark/clear.png"
    png_refresh = root_dir + "/Tyr/Icons/dark/refresh.png"
    png_update = root_dir + "/Tyr/Icons/dark/update.png"
    png_move = root_dir + "/Tyr/Icons/dark/move.png"
    png_logo = root_dir + "/Tyr/Icons/dark/forseti-icon.png"
    png_db_primary = root_dir + "/Tyr/Icons/dark/forseti-icon.png"
## INPUT LABELS ###################################################
## MAIN LABELS  ###############
main_labels = True
if main_labels:
    lb_id = "ID #"
    lb_site = "Site:"
    lb_location = "Location:"
    lb_product = "Selection:"
    lb_make = "Make:"
    lb_asset = "Asset Tag:"
    lb_reference = "Reference:"
    lb_assigned = "Assigned:"
    lb_status = "Status:"
    lb_date = "Date:"
    lb_info = "Info:"
    lb_deployed = "Deployed"
    lb_instock = "In Stock"
    lb_onorder = "On Order"
    lb_oos_repair = "Out of Service - Needs Repair"
    lb_oos_obsolete = "Out of Service - Obsolete"
###############################
## DROP LABELS  ###############
lb_default_dropdown = "Choose from List"
###############################
## INFORMATION ####################################################
app_info = True
if app_info:
    app_title = "Forseti"
    app_version = "(Build: 1.0)"
    info_title = "About"
    app_description = "Crafting Toolkit for Týr"
    app_framework = "Python 3.9 / PyQt6 / SQLite3"
    app_contact = "Contact: Need4Swede | theneed4swede@gmail.com"
## MIMISBRUNNR LIST ###############################################
app_Mimisbrunnr = True
if app_Mimisbrunnr:
    db_primary = "Mimisbrunnr 1"
    db_secondary = "Mimisbrunnr 2"
    db_tertiary = "Mimisbrunnr 3"
###################################################################
## CLEAR TERMINAL
clear_term()
## TYR MAIN #######################################################
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon(png_lab))
        self.setWindowTitle(app_title)
        self.showMaximized()
        # self.showFullScreen() 
        # self.setMinimumSize(1200, 800)

        # -------------------------------- #
        #       Menubar and Toolbar        #
        # -------------------------------- #
        help_menu = self.menuBar().addMenu("&About")
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        # ========== Menubar ========== #

        about_action = QAction(QIcon(png_info), "Info",
                               self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        # ========== Button Widgets ========== #
        global btn_add
        btn_add = QPushButton("Build", self)
        btn_add.clicked.connect(self.insert)
        btn_add.setIcon(QIcon(png_add))
        btn_add.hide()
        btn_add.setFixedWidth(100)
        btn_add.setFixedHeight(35)
        
        global btn_move
        btn_move = QPushButton("Move", self)
        btn_move.clicked.connect(self.move)
        btn_move.setIcon(QIcon(png_move))
        btn_move.hide()
        btn_move.setFixedWidth(100)
        btn_move.setFixedHeight(35)

        btn_clear = QPushButton("Refresh", self)
        btn_clear.clicked.connect(self.clear)
        btn_clear.setIcon(QIcon(png_refresh))
        btn_clear.setFixedWidth(100)
        btn_clear.setFixedHeight(35)
        
        global btn_clear_2
        btn_clear_2 = QPushButton("Clear", self)
        btn_clear_2.clicked.connect(self.clear_2)
        btn_clear_2.setIcon(QIcon(png_clear))
        btn_clear_2.hide()
        btn_clear_2.setFixedWidth(100)
        btn_clear_2.setFixedHeight(35)

        global search_bar
        self.search_box = QLineEdit()
        search_bar = self.search_box
        self.search_box.setPlaceholderText("Change To...")
        search_bar.hide()
        search_bar.setFixedWidth(100)
        search_bar.setFixedHeight(20)

        global btn_search
        btn_search = QPushButton("Search ID", self)
        btn_search.clicked.connect(self.search_item)
        self.search_box.returnPressed.connect(btn_search.click)
        btn_search.setIcon(QIcon(png_search))
        btn_search.hide()
        btn_search.setFixedWidth(100)
        btn_search.setFixedHeight(35)

        global search_bar_asset_tag
        self.search_box_asset_tag = QLineEdit()
        search_bar_asset_tag = self.search_box_asset_tag
        self.search_box_asset_tag.setPlaceholderText("Change To...")
        search_bar_asset_tag.hide()
        search_bar_asset_tag.setFixedWidth(100)
        search_bar_asset_tag.setFixedHeight(20)

        global btn_search_asset_tag
        btn_search_asset_tag = QPushButton("Search Tag", self)
        btn_search_asset_tag.clicked.connect(self.search_asset_tag)
        self.search_box_asset_tag.returnPressed.connect(btn_search_asset_tag.click)
        btn_search_asset_tag.setIcon(QIcon(png_search))
        btn_search_asset_tag.hide()
        btn_search_asset_tag.setFixedWidth(100)
        btn_search_asset_tag.setFixedHeight(35)

        global search_bar_general
        self.search_box_general = QLineEdit()
        search_bar_general = self.search_box_general
        self.search_box_general.setPlaceholderText("Cannot Change")
        search_bar_general.hide()
        search_bar_general.setFixedWidth(100)
        search_bar_general.setFixedHeight(20)

        global btn_search_general
        btn_search_general = QPushButton("Run", self)
        btn_search_general.clicked.connect(self.search_general)
        self.search_box_general.returnPressed.connect(btn_search_general.click)
        btn_search_general.setIcon(QIcon(png_run))
        btn_search_general.hide()
        btn_search_general.setFixedWidth(100)
        btn_search_general.setFixedHeight(35)

        global btn_delete
        btn_delete = QPushButton("Delete", self)
        btn_delete.clicked.connect(self.search_general)
        btn_delete.setIcon(QIcon(png_delete))
        btn_delete.hide()
        btn_delete.setFixedWidth(100)
        btn_delete.setFixedHeight(35)

        global btn_update
        btn_update = QPushButton("Update", self)
        btn_update.clicked.connect(self.update)
        btn_update.setIcon(QIcon(png_update))
        btn_update.hide()
        btn_update.setFixedWidth(100)
        btn_update.setFixedHeight(35)

        # ------------------------------- #
        #       Main Window Layout        #
        # ------------------------------- #
        layout = QGridLayout()
        layout_buttons = QVBoxLayout()

        self.main_window_widget = QWidget()
        self.main_window_widget.setLayout(layout)

        self.item_info_window = EntryWindow()

        self.tableWidget = QTableWidget()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(
            (lb_id, lb_site, lb_location, lb_product, lb_make,
             lb_asset, lb_reference, lb_assigned, lb_status, lb_date, lb_info))
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.hide()

        empty_widget = QLabel()
        empty_widget.setFixedSize(100, 55)
        layout_sub_buttons = QVBoxLayout()
        layout_sub_buttons.addWidget(empty_widget)
        layout_sub_buttons.addWidget(empty_widget)
        layout_sub_buttons.addWidget(self.search_box)
        layout_sub_buttons.addWidget(btn_search)
        layout_sub_buttons.addWidget(self.search_box_asset_tag)
        layout_sub_buttons.addWidget(btn_search_asset_tag)
        layout_sub_buttons.addWidget(self.search_box_general)
        layout_sub_buttons.addWidget(btn_search_general)
        layout_sub_buttons.addWidget(empty_widget)
        layout_sub_buttons.addWidget(btn_add)
        layout_sub_buttons.addWidget(btn_clear)
        layout_sub_buttons.addWidget(btn_clear_2)
        layout_sub_buttons.addWidget(btn_delete)
        layout_sub_buttons.addWidget(btn_update)
        layout_buttons.addLayout(layout_sub_buttons)

        layout.addWidget(self.item_info_window, 0, 0, 1, 3)
        layout.addLayout(layout_buttons, 0, 3)
        layout.addWidget(self.tableWidget, 0, 0, 0, 0)
        self.tableWidget.hide()

        self.setCentralWidget(self.main_window_widget)

        # ------------------------------- #
        #       Keyboard Shortcuts        #
        # ------------------------------- #
        self.shortcut_asset_tag = QShortcut(QKeySequence('Ctrl+Return'), self)
        self.shortcut_asset_tag.activated.connect(btn_add.click)
        self.shortcut_asset_tag = QShortcut(QKeySequence('Ctrl+t'), self)
        self.shortcut_asset_tag.activated.connect(self.search_box_asset_tag.setFocus)
        self.shortcut_delete = QShortcut(QKeySequence('Ctrl+d'), self)
        self.shortcut_delete.activated.connect(btn_delete.click)
        self.shortcut_search_id = QShortcut(QKeySequence('Ctrl+i'), self)
        self.shortcut_search_id.activated.connect(self.search_box.setFocus)
        self.shortcut_run = QShortcut(QKeySequence('Ctrl+r'), self)
        self.shortcut_run.activated.connect(self.search_box_general.setFocus)
        self.shortcut_refresh = QShortcut(QKeySequence('Alt+r'), self)
        self.shortcut_refresh.activated.connect(btn_clear.click)
        self.shortcut_clear = QShortcut(QKeySequence('Alt+c'), self)
        self.shortcut_clear.activated.connect(btn_clear_2.click)
        ## SEE 1293 FOR SEARCH SHORTCUT
        

        # ------------------------------- #
        #      Variables & Functions      #
        # ------------------------------- #
        self.conn = sqlite3.connect(inventory_db)
        self.result = []

    def load_data(self):
        if self.key == db_primary:
            self.result = Mimisbrunnr_1.show_table()
        self.display()
    
    def display(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self.result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # format the cell information
                data = str(data)
                if "\n" in data:
                    data = data.replace("\n", "")
                else:
                    pass
                self.tableWidget.setItem(row_number, column_number,
                                         QTableWidgetItem(str(data)))
                self.tableWidget.resizeColumnToContents(0)
                self.tableWidget.resizeColumnToContents(2)
                self.tableWidget.resizeColumnsToContents()

    def select_table(self):
        self.key = self.item_info_window.pageCombo.currentText()
        if self.key == db_primary:
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setHorizontalHeaderLabels(
            (lb_id, lb_site, lb_location, lb_product, lb_make,
             lb_asset, lb_reference, lb_assigned, lb_status, lb_date, lb_info))
        self.load_data()
        return self.key

    def about(self):
        dlg = AboutDialog()
        dlg.exec()

    def insert(self):
        if self.key == db_primary:
            selection = self.item_info_window.selection_db1.text()
            manufacturer = self.item_info_window.manufacturer_db1.text()
            asset_tag = self.item_info_window.assettag_db1.text()
            assigned = self.item_info_window.assigned_db1.text()
            location = self.item_info_window.location_db1.text()
            status = self.item_info_window.status_db1.text()
            notes = self.item_info_window.notes_db1.text()
            package = self.item_info_window.package_db1.text()
            user = self.item_info_window.site_db1.currentText()

            with open('Tyr/Týr.py', 'r') as file:
                data = file.readlines()
            if not selection == "":
                newSelection = selection
                data[100] = f'    lb_product = "{newSelection}:"\n'
            if not manufacturer == "":
                newMake = manufacturer
                data[101] = f'    lb_make = "{newMake}:"\n'
            if not asset_tag == "":
                newAssetTag = asset_tag
                data[102] = f'    lb_asset = "{newAssetTag}:"\n'
            if not assigned == "":
                newAssigned = assigned
                data[104] = f'    lb_assigned = "{newAssigned}:"\n'
            if not location == "":
                newLocation = location
                data[99] = f'    lb_location = "{newLocation}:"\n'
            if not status == "":
                newStatus = status
                data[105] = f'    lb_status = "{newStatus}:"\n'
            if not notes == "":
                newNotes = notes
                data[107] = f'    lb_info = "{newNotes}:"\n'
            with open('Tyr/Týr.py', 'w') as file:
                file.writelines(data)

    def clear(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        if self.key == db_primary: 
            self.item_info_window.item_db1_id_label.setText(lb_id)
            self.item_info_window.site_db1.clear()
            self.item_info_window.location_db1.clear()
            self.item_info_window.assettag_db1.clear()
            self.item_info_window.product_db1.clear()
            self.item_info_window.package_db1.clear()
            self.item_info_window.manufacturer_db1.clear()
            self.item_info_window.assigned_db1.clear()
            self.item_info_window.status_db1.clear()
            self.item_info_window.notes_db1.clear()

    def clear_2(self):
        if self.key == db_primary:
            self.search_box.clear()
            self.search_box_asset_tag.clear() 
            self.search_box_general.clear()
            self.item_info_window.item_db1_id_label.setText(lb_id)
            self.item_info_window.site_db1.clear()
            self.item_info_window.location_db1.clear()
            self.item_info_window.assettag_db1.clear()
            self.item_info_window.product_db1.clear()
            self.item_info_window.package_db1.clear()
            self.item_info_window.manufacturer_db1.clear()
            self.item_info_window.assigned_db1.clear()
            self.item_info_window.status_db1.clear()
            self.item_info_window.notes_db1.clear()
        
    def search(self):
        if self.key == db_primary:
            description = self.item_info_window.assettag_db1.text()
            location = self.item_info_window.location_db1.currentText()
            product = self.item_info_window.product_db1.itemText(
                self.item_info_window.product_db1.currentIndex())
            package = self.item_info_window.package_db1.text()
            assigned = self.item_info_window.assigned_db1.currentIndex()
            manufacturer = self.item_info_window.manufacturer_db1.itemText(
                self.item_info_window.manufacturer_db1.currentIndex())
            status = self.item_info_window.status_db1.itemText(
                self.item_info_window.status_db1.currentText())
            dates = self.item_info_window.dates_db1.text()
            notes = self.item_info_window.notes_db1.text()

            self.result = Mimisbrunnr_1.search_rows(
                description, location, product, package, assigned, manufacturer, status, dates, notes)

        self.display()

    def search_item(self, id):
        id = self.search_box.text()
        ## SEARCH BY ID
        try:
            if self.key == db_primary:
                first_matched_item = Mimisbrunnr_1.search_row(id)
                self.item_info_window.item_db1_id_label.setText(
                    "ID #:{:>35}".format(id))
                self.item_info_window.site_db1.clear()
                self.item_info_window.site_db1.addItem(
                    str(first_matched_item[1]))
                self.item_info_window.location_db1.clear()
                self.item_info_window.location_db1.addItem(
                    str(first_matched_item[2]))
                self.item_info_window.product_db1.clear()
                self.item_info_window.product_db1.addItem(
                    first_matched_item[3])
                self.item_info_window.manufacturer_db1.clear()
                self.item_info_window.manufacturer_db1.addItem(
                    first_matched_item[4])    
                self.item_info_window.assettag_db1.setText(
                    str(first_matched_item[5]))
                self.item_info_window.package_db1.setText(
                    str(first_matched_item[6]))
                self.item_info_window.assigned_db1.clear()
                self.item_info_window.assigned_db1.addItem(
                    str(first_matched_item[7]))
                self.item_info_window.status_db1.clear()
                self.item_info_window.status_db1.addItem(lb_deployed)
                self.item_info_window.status_db1.addItem(lb_instock)
                self.item_info_window.status_db1.addItem(lb_onorder)
                self.item_info_window.status_db1.addItem(lb_oos_repair)
                self.item_info_window.status_db1.addItem(lb_oos_obsolete)
                for x in range(0, 200):
                    self.item_info_window.status_db1.addItem("Quantity: " + str(x))
                self.item_info_window.dates_db1.setText(
                    today)
                self.item_info_window.notes_db1.setText(
                    str(first_matched_item[10]))

            if isinstance(id, int):
                print("int")
            if isinstance(id, str):
                print("string")
            print(str(first_matched_item[5]))
        except Exception:
            if self.key == db_primary:
                self.item_info_window.item_db1_id_label.setText("ID #:")

            QMessageBox.information(
                QMessageBox(), "Search", "Can not find the item")

    def search_asset_tag(self, asset_tag_no):
        global row_count
        ## Make asset_tag_no = whatever value you enter in the search bar in uppercase
        asset_tag_no = self.search_box_asset_tag.text()
        asset_tag_no = asset_tag_no.upper()
        run_search = True
        if asset_tag_no == "0":
            run_search = False
            QMessageBox.information(
                QMessageBox(), "Search Result", "Invalid Asset Tag: 0")
            return
        if asset_tag_no == "":
            run_search = False
            QMessageBox.information(
                QMessageBox(), "Search Result", "Please enter an Asset Tag")
            return
        ## SEARCH BY ASSET TAG
        try:
            try:
                if self.key == db_primary:
                    for row_count in range(1,500):
                        # clear_term()
                        ## list_row lists all the values in the given row using .search_row
                        list_row = Mimisbrunnr_1.search_row(row_count)
                        ## item_asset_tag equals the fifth element in the row, which is the asset tag
                        try:
                            item_asset_tag = list_row[5]
                        except Exception:
                            for x in range(1,1):
                                pass
                        ## If the tag that you searched for shows up in the above query
                        ## Populate the forms
                        try:
                            if asset_tag_no in item_asset_tag:
                                while run_search:
                                    first_matched_item = Mimisbrunnr_1.search_row(row_count)
                                    self.item_info_window.item_db1_id_label.setText(
                                        "ID #:{:>35}".format(row_count))
                                    self.item_info_window.site_db1.clear()
                                    self.item_info_window.site_db1.addItem(
                                        str(first_matched_item[1]))
                                    self.item_info_window.location_db1.clear()
                                    self.item_info_window.location_db1.addItem(
                                        str(first_matched_item[2]))
                                    self.item_info_window.product_db1.clear()
                                    self.item_info_window.product_db1.addItem(
                                        first_matched_item[3])
                                    self.item_info_window.manufacturer_db1.clear()
                                    self.item_info_window.manufacturer_db1.addItem(
                                        first_matched_item[4])    
                                    self.item_info_window.assettag_db1.setText(
                                        str(first_matched_item[5]))
                                    self.item_info_window.package_db1.setText(
                                        str(first_matched_item[6]))
                                    self.item_info_window.assigned_db1.clear()
                                    self.item_info_window.assigned_db1.addItem(
                                        str(first_matched_item[7]))
                                    self.item_info_window.status_db1.clear()
                                    self.item_info_window.status_db1.addItem(lb_deployed)
                                    self.item_info_window.status_db1.addItem(lb_instock)
                                    self.item_info_window.status_db1.addItem(lb_onorder)
                                    self.item_info_window.status_db1.addItem(lb_oos_repair)
                                    self.item_info_window.status_db1.addItem(lb_oos_obsolete)
                                    for x in range(0, 200):
                                        self.item_info_window.status_db1.addItem("Quantity: " + str(x))
                                    self.item_info_window.dates_db1.setText(
                                        today)
                                    self.item_info_window.notes_db1.setText(
                                        str(first_matched_item[10]))
                                    self.search_box.setText(str(row_count))
                                    self.search_box_general.clear()
                                    self.search_box_asset_tag.clear()
                                    break
                                break
                            else:
                                pass
                        except Exception:
                            pass
                            # QMessageBox.information(
                            #     QMessageBox(), "Search Result", "Hmm, I can't find that asset tag :(\nMake sure you entered the information correctly.")
            except Exception:
                QMessageBox.information(
                    QMessageBox(), "Search Result", "Hmm, I can't find that asset tag :(\nMake sure you entered the information correctly.")
                pass
        except Exception:
            QMessageBox.information(
                QMessageBox(), "Search", "Can not find the item")

    def search_general(self, search_input):
        global general_input
        general_input = self.search_box_general.text()
        general_input = general_input.upper()
        ## ARGUMENTS
        help = "HELP"
        arg_is_help = "HELP:"
        arg_is_asset_tag = "AT:"
        arg_is_serial_no = "SN:"
        arg_is_location = "LOC:"
        arg_is_make = "MAKE:"
        arg_is_ip = r"//"
        arg_is_toner = "TONER:"
        arg_is_user = "USER:"
        is_building = "BLD"
        ## SEARCH BY ARGUMENT
        try:
            clear_term()
            if general_input == help: ## HELP TEXT
                print("Help Requested!")
                self.search_box_general.clear()
                try:
                    QMessageBox.information(
                        QMessageBox(), "Help", "Add arguments to your help query to find answers."
                        "\n\n'help:readme' - Opens program documentation"
                        "\n\n'help:tags' - List search query tags"
                        "\n\n'help:shortcuts' - List available keyboard shortcuts")
                except Exception:
                    print("Didn't work")
                    pass
            elif general_input.startswith(arg_is_help): ## HELP : TAGS
                print("Help Requested!")
                help_requested = general_input.split(":")
                help_requested[1] = help_requested[1].upper()
                self.search_box_general.clear()
                if help_requested[1] == "TAGS":
                    QMessageBox.information(
                            QMessageBox(), "Help: Tags", "Search Tags\n\n\nAT: Asset Tag\n\nSN: Serial Number\n\nLOC: Location\n\n"
                            "MAKE: Manufacturer\n\nTONER: Print Toner\n\n'//' for IP Address\n\n*:list to list tag options")
                elif help_requested[1] == "SHORTCUTS":
                    QMessageBox.information(
                            QMessageBox(), "Help: Shortcuts", "Keyboard Shortcuts\n\n\nCTRL+S: Run Search\n\nCTRL+I: ID Search\n\nCTRL+T: Asset Tag Search\n\n"
                            "CTRL+R: Run Console\n\nCTRL+Return: Add Entry\n\nCTRL+D: Delete Entry\n\nCTRL+E: Export to CSV\n\nALT+R: Refresh")
                elif help_requested[1] == "README":
                    online_readme = True
                    if(online_readme):
                        readme = ("https://need4swede.github.io/ODIN/Mimir/Documentation/readme.html")
                    else:
                        readme = (root_dir + "/Mimir/Documentation/readme.html")
                        if platform.system() == "Darwin":
                            print("isMac")
                            readme = ("file:///" + readme)
                    webbrowser.open(readme)
                else:
                    QMessageBox.information(
                        QMessageBox(), "Help", "Add arguments to your help query to find answers."
                        "\n\n'help:howto' - Opens program documentation"
                        "\n\n'help:tags' - List search query tags"
                        "\n\n'help:shortcuts' - List available keyboard shortcuts")
            elif general_input.startswith(arg_is_asset_tag):
                print("Searching by: Asset Tag")
                arg_tag = general_input.split(":")
                print("Asset Tag:", arg_tag[1])
                self.search_box_asset_tag.setText(arg_tag[1])
                btn_search_asset_tag.click()
                self.search_box_asset_tag.clear()
                self.search_box.setText(str(row_count))
            elif general_input.startswith(arg_is_serial_no):
                print("Searching by: Serial Number")
                arg_serial_no = general_input.split(":")
                print("Serial No:", arg_serial_no[1])
            elif general_input.startswith(arg_is_location):
                print("Searching by: Location")
                arg_location = general_input.split(":")
                if is_building in arg_location[1]:
                    print("Location Type: Building")
                    building = arg_location[1]
                    building = building.replace("BLD", "BLD. ")
                    print("Building Location:", building)
                else:
                    print("Location:", arg_location[1])
            elif general_input.startswith(arg_is_make):
                print("Searching by: Make")
                make_list = ["CANON", "DELL", "HP", "LENOVO"]
                arg_make = general_input.split(":")
                make = arg_make[1]
                if any(x in make for x in make_list):
                    if make == "HP":
                        print("Make:", make)
                    else:
                        make = make.capitalize()
                        print("Make:", make)
                else:
                    make_list = [x.capitalize() for x in make_list]  
                    make = make.capitalize()
                    if make == "List":
                        print("List of Manufacturers:", make_list)
                    elif make == "":
                        print("No make listed!")
                        print("List of Manufacturers:", make_list)
                    else:
                        print("Unknown Make!") 
            elif general_input.startswith(arg_is_ip):
                print("Searching by: IP Address")
                arg_ip = general_input.split(r"//")
                if arg_ip[1].startswith("192"):
                    pass
                else:
                    arg_ip[1] = "192.168." + arg_ip[1]
                arg_ip[1] = r"//" + arg_ip[1]
                print("IP Address:", arg_ip[1])
            elif general_input.startswith(arg_is_toner):
                print("Searching by: Toner")
                toner_list_canon = ["GPR-37", "GPR-38"]
                arg_toner = general_input.split(":")
                toner_type = arg_toner[1]
                GPR_37 = ["GPR-37", "GPR37", "37"]
                GPR_38 = ["GPR-38", "GPR38", "38"]  
                if any(x in toner_type for x in GPR_37):
                    print("Toner Make: Canon") 
                    print("Toner Type:", GPR_37[0])
                elif any(x in toner_type for x in GPR_38):
                    print("Toner Make: Canon") 
                    print("Toner Type:", GPR_38[0])
                if toner_type == "GPR":
                    print("Toner Make: Canon")
                    print("Known Types:", toner_list_canon)
            elif general_input.startswith(arg_is_user):
                print("Searching by: User")
                arg_user = general_input.split(":")
                user = arg_user[1]
                user = user.lower()
                f_name = user[0:1]
                f_name = f_name + "."
                l_name = user[1:]
                user_email = user + "@domain.org"
                print("Username:", user)
                try:
                    if any(l_name.capitalize() for x in user_list):
                        indices = [i for i, s in enumerate(user_list) if l_name.capitalize() in s]
                        full_name = user_list[indices[0]]
                        print("Full Name:", full_name)
                        print("Email:", user_email)
                    else:
                        QMessageBox.information(
                            QMessageBox(), "User Search", "Enter the person's name in 'users.csv'\n\nSearch users by entering the first letter of their first initial, and their full lastname\n\nExample: llarsson")
                except Exception:
                    QMessageBox.information(
                        QMessageBox(), "User Search", "User not found!\n\nSearch users by entering the first letter of their first initial, and their full lastname")   
            else:
                if ":" in general_input:
                    QMessageBox.information(
                        QMessageBox(), "Search", "Invalid Run Argument\n\nRun 'help:tags' to view available run arguments")
                else:
                    print("No search argument passed!")
                    print("Insert:", general_input)
                    print("\nType Assumption: Serial Number")
                    print("Argument Probability: Low")
                    print("\nNo Argument passed to Search Query")
                    QMessageBox.information(
                        QMessageBox(), "Search", "No results found\n\nTry using a search argument\n\nRun 'help' for more options")
            pass
        except Exception:
            QMessageBox.information(
                QMessageBox(), "Search", "Unable to process your query!\n\nRun 'help' for more options")

    def update(self):
        clear_term()
        id = self.search_box.text()
        asset_tag_no = self.search_box_asset_tag.text()
        if str(id) == "":
            print("The ID searchbox is empty")
            sys.exit(app.exec())
        if self.key == db_primary:
            asset_tag = self.item_info_window.assettag_db1.text()
            location = self.item_info_window.location_db1.currentText()
            product = self.item_info_window.product_db1.itemText(
                self.item_info_window.product_db1.currentIndex())
            package = self.item_info_window.package_db1.text()
            assigned = self.item_info_window.assigned_db1.currentText()
            manufacturer = self.item_info_window.manufacturer_db1.itemText(
                self.item_info_window.manufacturer_db1.currentIndex())
            # self.item_info_window.status_db1.clear()
            # status = str(self.item_info_window.status_db1.currentText())
            status = self.item_info_window.status_db1.itemText(
                self.item_info_window.status_db1.currentIndex())
            dates = self.item_info_window.dates_db1.text()
            notes = self.item_info_window.notes_db1.text()
            site = self.item_info_window.site_db1.currentText()
            print("\nCurrent Text:", str(self.item_info_window.status_db1.itemText(
                self.item_info_window.status_db1.currentIndex())))
            Mimisbrunnr_1.update_row(id, site, location, product, manufacturer, asset_tag,
                                  package, assigned, status, dates, notes)

        QMessageBox.information(
            QMessageBox(), "Update", "Item has been updated.")
        self.load_data()

    def clear_contents(self):
        self.tableWidget.clearContents()

    def quit(self):
        reply = QMessageBox.question(self, 'Exit', 'Do you want to quit?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            pass
## TYR INFO #######################################################
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(245)

        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle(info_title)
        title = QLabel(app_title)
        font = title.font()
        font.setPointSize(65)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap(png_logo)
        pixmap = pixmap.scaledToWidth(325)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)
        layout.addWidget(QLabel(app_version))
        layout.addWidget(QLabel(app_description))
        layout.addWidget(QLabel(app_framework))
        layout.addWidget(QLabel(app_contact))
        # layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
## TYR INITIALIZE #################################################
class EntryWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        sub_layout = QVBoxLayout()
        self.setLayout(layout)

        # Label
        self.Mimisbrunnr_label = QLabel("Mimisbrunnr")
        self.Mimisbrunnr_label.hide()
        self.item_label_db1 = QLabel("Item Information")
        self.item_label_db1.hide()
        self.item_label_db2 = QLabel("Item Information")
        self.item_label_db2.hide()

        self.picLabel = QLabel()
        self.pixmap = QPixmap(png_db_primary)
        self.pixmap = self.pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        self.picLabel.setPixmap(self.pixmap)
        

        # Layouts
        self.stackedLayout = QStackedLayout()
        sub_layout.addWidget(self.picLabel)
        layout.addLayout(sub_layout)
        layout.addLayout(self.stackedLayout)

        # -------------------------- #
        #      Primary Mimisbrunnr      #
        # -------------------------- #
        self.page_db1 = QWidget()
        self.page_db1_layout = QVBoxLayout()
        self.form_layout_db1 = QFormLayout()

        self.item_db1_id = ""
        self.item_db1_id_label = QLabel(f"Forseti - {app_version}"
        "\n\nThis tool allows you to alter the names of the various entry items in Týr to fit your particular needs. "
        "\nStart by selecting 'Change Layout' and then fill in the new name for each entry you would like changed. "
        "\n\nClick the 'Build' button to apply the changes."
        "\nIf you want to revert back to Týr's default layout, you have the option to do so.")
        self.page_db1_layout.addWidget(self.item_db1_id_label)
        self.site_db1 = QComboBox()
        global product_selection
        global search_selection
        search_selection = "Reset to Default..."
        self.product_db1 = QComboBox()
        self.product_db1.addItem(lb_default_dropdown)
        self.product_db1.addItem(search_selection)  
        self.product_db1.addItem("")
        self.product_db1.addItem("Change Layout")
        self.form_layout_db1.addRow("Options:", self.product_db1)
        product_selection = self.product_db1
        product_selection.activated.connect(self.pass_Net_Adap) # Passes active selection
        global starting_page
        starting_page = True
        if starting_page:
            starting_page = not starting_page
            self.shortcut_search = QShortcut(QKeySequence('Ctrl+s'), self)
            self.shortcut_search.activated.connect(self.pass_Net_Adap)
        self.manufacturer_db1 = QLineEdit()
        self.assettag_db1 = QLineEdit()
        self.package_db1 = QLineEdit()
        self.page_db1_layout.addLayout(self.form_layout_db1)
        self.page_db1.setLayout(self.page_db1_layout)
        self.stackedLayout.addWidget(self.page_db1)
        self.db_id = 0
        

    # When called, takes the input and checks which lb_drop# was selected
    # and launches a unique follow-up window if additional information is required
    def pass_Net_Adap(self):
        if starting_page == False:
            self.shortcut_search = QShortcut(QKeySequence('Ctrl+s'), self)
            self.shortcut_search.activated.connect(btn_search.click)
        self.find()
        self.show()

    # Inserts the information from the previous window, into our main window
    def find(self):
        selected_option = self.product_db1.currentText()
        def confirm_reset():
            reply = QMessageBox.question(self, 'Reset', "Reset all of Týr's values back to default?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
            if reply == QMessageBox.StandardButton.Yes:
                with open('Tyr/Týr.py', 'r') as file:
                    data = file.readlines()
                    data[97] = f'    lb_id = "ID #:"\n'
                    data[98] = f'    lb_site = "Site:"\n'
                    data[99] = f'    lb_location = "Location:"\n'
                    data[100] = f'    lb_product = "Selection:"\n'
                    data[101] = f'    lb_make = "Make:"\n'
                    data[102] = f'    lb_asset = "Asset Tag:"\n'
                    data[103] = f'    lb_reference = "Reference:"\n'
                    data[104] = f'    lb_assigned = "Assigned:"\n'
                    data[105] = f'    lb_status = "Status:"\n'
                    data[106] = f'    lb_date = "Date:"\n'
                    data[107] = f'    lb_info = "Info:"\n'
                    data[108] = f'    lb_deployed = "Deployed:"\n'
                    data[109] = f'    lb_instock = "In Stock:"\n'
                    data[110] = f'    lb_onorder = "On Order:"\n'
                    data[111] = f'    lb_oos_repair = "Out of Service - Needs Repair:"\n'
                    data[112] = f'    lb_oos_obsolete = "Out of Service - Obsolete:"\n'         
                with open('Tyr/Týr.py', 'w') as file:
                    file.writelines(data)
                reply = QMessageBox.question(self, 'Reset', "Týr's values have been reset",
                                     QMessageBox.StandardButton.Ok)
                if reply == QMessageBox.StandardButton.Ok:
                    reply = QMessageBox.question(self, 'Exit', 'Exit Forseti?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
                    if reply == QMessageBox.StandardButton.Yes:
                        sys.exit()
                    else:
                        python = sys.executable
                        os.execl(python, python, * sys.argv)
            else:
                pass
        if "Reset" in selected_option:
            confirm_reset()    
        self.product_db1.hide()
        self.selection_db1 = QLineEdit()
        self.form_layout_db1.addRow(lb_product, self.selection_db1)
        search_bar.show()
        btn_search.show()
        search_bar_asset_tag.show()
        btn_search_asset_tag.show()
        btn_add.show()
        self.form_layout_db1.addRow(lb_make, self.manufacturer_db1)

        self.package_db1.close()
        
        self.form_layout_db1.addRow(lb_asset, self.assettag_db1)
        self.assettag_db1.returnPressed.connect(btn_add.click)
        self.package_db1 = QLineEdit()
        self.assigned_db1 = QLineEdit()
        self.package_db1.returnPressed.connect(btn_add.click)

        self.form_layout_db1.addRow(lb_assigned, self.assigned_db1)
        self.location_db1 = QLineEdit()
        self.form_layout_db1.addRow(lb_location, self.location_db1)
        
        self.status_db1 = QLineEdit()
        self.form_layout_db1.addRow(lb_status, self.status_db1)

        self.notes_db1 = QLineEdit()
        self.form_layout_db1.addRow(lb_info, self.notes_db1)
    
        self.selection_db1.setPlaceholderText("Change To...")
        self.manufacturer_db1.setPlaceholderText("Change To...")
        self.assettag_db1.setPlaceholderText("Change To...")
        self.assigned_db1.setPlaceholderText("Change To...")
        self.location_db1.setPlaceholderText("Change To...")
        self.status_db1.setPlaceholderText("Change To...")
        self.notes_db1.setPlaceholderText("Change To...")
        self.package_db1.setPlaceholderText("Change To...")
        self.notes_db1.returnPressed.connect(btn_add.click)
        self.close()

if __name__ == "__main__":
    mimir_exists = os.path.isfile(inventory_db)

    if mimir_exists:
        open(inventory_db, "r+")
    else:
        open(inventory_db, "w")
        Mimisbrunnr_1.create_table_db1()
        Mimisbrunnr_2.create_table_db2()
    if not os.path.isdir(forseti_mimir_dir):
        os.makedirs(forseti_mimir_dir)
    if not os.path.isfile(forseti_mimir):
        shutil.copy(inventory_db, forseti_mimir)

    app = QApplication(sys.argv)
    if QDialog.accepted:
        window = MainWindow()
        window.show()
        window.key = db_primary     # Default Mimisbrunnr to load
        window.load_data()
    sys.exit(app.exec())
