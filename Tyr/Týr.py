# #################################################################
# File name:    Týr.py
# Author:       Need4Swede
# Company:      N/A
# Contact:      need4swede@gmail.com
# Description:  Omniscient Database for Inventory Notation
# #################################################################

## LIBRARY IMPORTS ################################################
import darkdetect
import os, sqlite3, sys, platform, string, os.path, webbrowser, shutil, csv, simpleaudio, getpass, qdarktheme
import pandas as pd
from fpdf import FPDF
from PyQt6 import *
from csv import reader
from datetime import date
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
## USER DIRECTORY IMPORTS #########################################
global root_dir
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
    user = getpass.getuser()
    documentation_dir = (root_dir + "/Documentation")
    mimir_dir = (root_dir + "/Mimir")
    mimisbrunnr_dir = (root_dir + "/Mimisbrunnr")
    mimisbrunnr_export_dir = (mimisbrunnr_dir + "/exports/")
    tyr_dir = (root_dir + "/Tyr")
    tyr_log_dir = (tyr_dir + "/logs/")
    tyr_log = (tyr_log_dir + "log.txt")
    tyr_log_tutorial = (tyr_log_dir + "tutorial.txt")
    freya_dir = (root_dir + "/Freya")
    sounds_dir = (freya_dir + "/sounds/")
    if not os.path.isdir(mimir_dir):
        os.makedirs(mimir_dir)
    if os.path.isdir(documentation_dir):
        if os.path.isdir(mimir_dir + "/Documentation"):
            shutil.rmtree(mimir_dir + "/Documentation")
        shutil.copytree(documentation_dir, mimir_dir + "/Documentation")
        shutil.rmtree(documentation_dir) 
    if not os.path.isdir(tyr_log_dir):
        os.makedirs(tyr_log_dir)
    inventory_db = mimir_dir + "/Mimir.db"
    date_today = date.today()
    today = date_today.strftime("%B %d,  %Y")
    clean_dir = True
if clean_dir:
    if os.path.isdir(root_dir + "/__pycache__"):
        shutil.rmtree(root_dir + "/__pycache__")
    if os.path.isdir(freya_dir + "/__pycache__"):
        shutil.rmtree(freya_dir + "/__pycache__")
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
    png_logo = root_dir + "/Tyr/Icons/tyr-icon.png"
    png_db_primary = root_dir + "/Tyr/Icons/tyr-icon.png"
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
    png_logo = root_dir + "/Tyr/Icons/dark/tyr-icon.png"
    png_db_primary = root_dir + "/Tyr/Icons/dark/tyr-icon.png"
## SOUND FILES  ###############
app_sounds = True
if app_sounds:
    freya_speak = simpleaudio.WaveObject.from_wave_file
#### SOUNDS ###########
    confirm_entry = freya_speak(sounds_dir + 'confirm_entry.wav')
    deny_entry = freya_speak(sounds_dir + 'discard_entry.wav')

    ## TUTORIAL ####
    tyr_start = freya_speak(sounds_dir + 'tutorial/Tyr/tyr_start.wav')
    tyr_serial = freya_speak(sounds_dir + 'tutorial/Tyr/tyr_serial.wav')
    tyr_IP = freya_speak(sounds_dir + 'tutorial/Tyr/tyr_ip_address.wav')
    tyr_initialize = freya_speak(sounds_dir + 'tutorial/Tyr/tyr_initialize.wav')
    tyr_entry_added = freya_speak(sounds_dir + 'tutorial/Tyr/tyr_entry_added.wav')
#########################
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
drop_labels = True
if drop_labels:
    lb_default_dropdown = "Choose from List"
    lb_ap = "Access Point"
    lb_colors = "Black", "Blue", "Brown", "Green", "Grey", "Yellow", "White"
    lb_desktop = "Desktop - Windows"
    lb_dvr = "DVR"
    lb_chromebooks = "Laptop - Chromebook"
    lb_winlaptops = "Laptop - Windows"
    lb_locprinters = "Printer - Local"
    lb_netprinters = "Printer - Network"
    lb_server = "Server"
    lb_switch = "Switch"
    lb_toner = "Printer - Toner"
    lb_aesir = "Aesir"
    lb_vanir = "Vanir"
    lb_midgard = "Midgard"
    lb_locations_vanir = ["Choose a Realm"]
    lb_locations_aesir = ["Choose a Realm"]
    alpha = string.ascii_uppercase
def list_vanir_locations():
    for x in range(1,25):
        lb_locations_vanir.append("Realm " + str(x))
def list_aesir_locations():
    lb_locations_aesir.append("Asgard") 
    lb_locations_aesir.append("-----------")
    for x in range(0, 26):
        lb_locations_aesir.append("Realm " + alpha[x])   
list_aesir_locations()
list_vanir_locations()
###############################
## DROP-SUB LABELS  ###########
drop_sub_labels = True
if drop_sub_labels:
    lb_brands_dvr = "LTS Security", "Generic"
    lb_brands_desktops = "Dell", "Custom", "HP", "Lenovo"
    lb_brands_chromebook = "Dell", "HP", "Lenovo"
    lb_brands_laptop = "Dell", "HP", "Lenovo", "Surface"
    lb_brands_printer = "Brother", "Canon", "HP"
    lb_tbd = "TBD"
###############################
## INFORMATION ####################################################
app_info = True
if app_info:
    app_title = "Týr"
    app_version = "(Build: v2.8)"
    info_title = "About"
    app_description = "ODIN's Adaptive Asset Management System"
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
        if platform.system() == "Windows": 
            self.setMinimumSize(1200, 800)
        global tutorial
        if not os.path.isfile(tyr_log) or not os.path.isfile(tyr_log_tutorial):
            with open(tyr_log, 'w') as f:
                f.write('First time starting Tyr!\n')
            with open(tyr_log_tutorial, 'w') as f:
                f.write('Disabled')
            tutorial = QMessageBox.question(self, 'Tutorial', 'Welcome to Týr!\n\nWould you like to use the Tutorial?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
            if tutorial == QMessageBox.StandardButton.Yes:
                tyr_start.play()
        else:
            tutorial = QMessageBox.StandardButton.No
        AppLog('main', 'start', '', '', '')

        # -------------------------------- #
        #       Menubar and Toolbar        #
        # -------------------------------- #
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&About")

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.hide()

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        # ========== Menubar ========== #
        add_item_action = QAction(QIcon(png_add), "Add New", self)
        add_item_action.triggered.connect(self.insert)
        file_menu.addAction(add_item_action)

        search_item_action = QAction(
            QIcon(png_search), "Search", self)
        search_item_action.triggered.connect(self.search)
        file_menu.addAction(search_item_action)

        del_item_action = QAction(QIcon(png_delete), "Delete", self)
        del_item_action.triggered.connect(self.delete)
        file_menu.addAction(del_item_action)

        export_item_action = QAction(QIcon(png_export), "Export", self)
        export_item_action.triggered.connect(self.export)
        file_menu.addAction(export_item_action)

        file_menu.addSeparator()

        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(self.quit)
        file_menu.addAction(quit_action)

        about_action = QAction(QIcon(png_info), "Info",
                               self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        # ========== Toolbar ========== #
        # Set toolbar spacing
        toolbar.setStyleSheet("QToolBar{spacing:10px;}")

        btn_add_item = QAction(QIcon(png_add), "Add New",
                               self)
        btn_add_item.triggered.connect(self.insert)
        btn_add_item.setStatusTip("Add new item")
        toolbar.addAction(btn_add_item)

        btn_view_all = QAction(QIcon(png_view), "View All",
                               self)
        btn_view_all.triggered.connect(self.load_data)
        btn_view_all.setStatusTip("View all")
        toolbar.addAction(btn_view_all)

        btn_search_item = QAction(QIcon(png_search), "Search",
                                  self)
        btn_search_item.triggered.connect(self.search_item)
        btn_search_item.setStatusTip("Search")
        toolbar.addAction(btn_search_item)

        btn_delete_item = QAction(
            QIcon(png_delete), "Delete", self)
        btn_delete_item.triggered.connect(self.delete)
        btn_delete_item.setStatusTip("Delete")
        toolbar.addAction(btn_delete_item)

        btn_export = QAction(QIcon(png_export), "Export to CSV", self)
        btn_export.triggered.connect(self.export)
        btn_export.setStatusTip("Export to CSV")
        toolbar.addAction(btn_export)

        # ========== Button Widgets ========== #
        global btn_add
        btn_add = QPushButton("Add", self)
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

        btn_refresh = QPushButton("Refresh", self)
        btn_refresh.clicked.connect(self.refresh)
        btn_refresh.setIcon(QIcon(png_refresh))
        btn_refresh.setFixedWidth(100)
        btn_refresh.setFixedHeight(35)
        
        global btn_clear
        btn_clear = QPushButton("Clear", self)
        btn_clear.clicked.connect(self.clear)
        btn_clear.setIcon(QIcon(png_clear))
        btn_clear.hide()
        btn_clear.setFixedWidth(100)
        btn_clear.setFixedHeight(35)

        global search_bar
        self.search_box = QLineEdit()
        search_bar = self.search_box
        self.search_box.setPlaceholderText("ID #...")
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
        self.search_box_asset_tag.setPlaceholderText("Asset Tag...")
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
        self.search_box_general.setPlaceholderText("Console...")
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
        btn_delete.clicked.connect(self.delete)
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

        self.key = self.item_info_window.pageCombo.activated.connect(
            self.select_table)

        self.table_title = QLabel("Collection List")
        self.table_title.setFont(QFont("Arial", 14))

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

        empty_widget = QLabel()
        empty_widget.setFixedSize(100, 55)
        # layout_buttons.addWidget(btn_move)
        layout_sub_buttons = QVBoxLayout()
        layout_sub_buttons.addWidget(self.search_box)
        layout_sub_buttons.addWidget(btn_search)
        layout_sub_buttons.addWidget(self.search_box_asset_tag)
        layout_sub_buttons.addWidget(btn_search_asset_tag)
        layout_sub_buttons.addWidget(self.search_box_general)
        layout_sub_buttons.addWidget(btn_search_general)
        layout_sub_buttons.addWidget(empty_widget)
        layout_sub_buttons.addWidget(btn_add)
        layout_sub_buttons.addWidget(btn_refresh)
        layout_sub_buttons.addWidget(btn_clear)
        layout_sub_buttons.addWidget(btn_delete)
        layout_sub_buttons.addWidget(btn_update)
        layout_buttons.addLayout(layout_sub_buttons)

        layout.addWidget(self.item_info_window, 0, 0, 1, 3)
        layout.addLayout(layout_buttons, 0, 3)
        layout.addWidget(self.table_title, 1, 0)
        layout.addWidget(self.tableWidget, 2, 0, 1, 4)

        self.setCentralWidget(self.main_window_widget)

        # ------------------------------- #
        #       Keyboard Shortcuts        #
        # ------------------------------- #
        self.shortcut_asset_tag = QShortcut(QKeySequence('Ctrl+Return'), self)
        self.shortcut_asset_tag.activated.connect(btn_add.click)
        self.shortcut_asset_tag = QShortcut(QKeySequence('Ctrl+e'), self)
        self.shortcut_asset_tag.activated.connect(self.export)
        self.shortcut_asset_tag = QShortcut(QKeySequence('Ctrl+t'), self)
        self.shortcut_asset_tag.activated.connect(self.search_box_asset_tag.setFocus)
        self.shortcut_delete = QShortcut(QKeySequence('Ctrl+d'), self)
        self.shortcut_delete.activated.connect(btn_delete.click)
        self.shortcut_search_id = QShortcut(QKeySequence('Ctrl+i'), self)
        self.shortcut_search_id.activated.connect(self.search_box.setFocus)
        self.shortcut_run = QShortcut(QKeySequence('Ctrl+r'), self)
        self.shortcut_run.activated.connect(self.search_box_general.setFocus)
        self.shortcut_refresh = QShortcut(QKeySequence('Alt+r'), self)
        self.shortcut_refresh.activated.connect(btn_refresh.click)
        self.shortcut_clear = QShortcut(QKeySequence('Alt+c'), self)
        self.shortcut_clear.activated.connect(btn_clear.click)
        self.shortcut_wipe_mimir = QShortcut(QKeySequence('Alt+Backspace'), self)
        self.shortcut_wipe_mimir.activated.connect(self.wipe_mimir)
        self.shortcut_csv2pdf = QShortcut(QKeySequence('Alt+p'), self)
        self.shortcut_csv2pdf.activated.connect(self.update_pdf)
        ## SEE 1293 FOR SEARCH SHORTCUT
        

        # ------------------------------- #
        #      Variables & Functions      #
        # ------------------------------- #
        self.conn = sqlite3.connect(inventory_db)
        self.result = []

    def load_data(self):
        if self.key == db_primary:
            self.result = Mimisbrunnr_1.show_table()
        elif self.key == db_secondary:
            #self.tableWidget.setColumnCount(9)
            self.result = Mimisbrunnr_2.show_table()
        self.display()
    
    def load_data_2(self):
        if self.key == db_primary:
            self.result = Mimisbrunnr_2.show_table()
        elif self.key == db_secondary:
            #self.tableWidget.setColumnCount(9)
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
        elif self.key == db_secondary:
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
            description = self.item_info_window.assettag_db1.text().upper()
            location = self.item_info_window.location_db1.currentText()
            product = self.item_info_window.product_db1.itemText(
                self.item_info_window.product_db1.currentIndex())
            package = self.item_info_window.package_db1.text().upper() # PACKAGE = SERIAL NUMBER
            try:
                insert_Serial = str(package).split(": ")
                serial_no_length = len(insert_Serial[1])
            except Exception:
                pass
            assigned = self.item_info_window.assigned_db1.currentText()
            manufacturer = self.item_info_window.manufacturer_db1.itemText(
                self.item_info_window.manufacturer_db1.currentIndex())
            try:
                if serial_no_length == 7:
                    manufacturer = 'Dell'
                elif serial_no_length == 8:
                    manufacturer = 'Lenovo'
            except Exception:
                pass
            status = self.item_info_window.status_db1.itemText(
                self.item_info_window.status_db1.currentIndex())
            dates = self.item_info_window.dates_db1.text()
            notes = self.item_info_window.notes_db1.text()
            user = self.item_info_window.site_db1.currentText()
            for row_count in range(1, 9999):
                try:
                    if "None" in Mimisbrunnr_1.search_row(row_count):
                        break
                    if description in Mimisbrunnr_1.search_row(row_count):
                        if description == "":
                            pass
                        else:
                            identical_AT = QMessageBox.question(self, 'Warning', 'An item with that Asset Tag already exists in your database\n\nWould you like add it anyway?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
                            if identical_AT == QMessageBox.StandardButton.No:
                                return
                    if package in Mimisbrunnr_1.search_row(row_count):
                        QMessageBox.information(
                            QMessageBox(), "Warning", "This item's serial number matches that of an existing item in your database\n\nMatched Item ID Number: {}".format(row_count))
                        self.search_box.setText(str(row_count))
                        return
                except Exception:
                    pass
            Mimisbrunnr_1.add_row(user, location, product, manufacturer, description, package,
                assigned, status, dates, notes)
        elif self.key == db_secondary:
            description = self.item_info_window.description_db2.text()
            location = self.item_info_window.location_db2.text()
            product = self.item_info_window.product_db2.itemText(
                self.item_info_window.product_db2.currentIndex())
            package = self.item_info_window.package_db2.text()
            assigned = self.item_info_window.assigned_db2.text()
            manufacturer = self.item_info_window.manufacturer_db2.itemText(
                self.item_info_window.manufacturer_db2.currentIndex())
            status = self.item_info_window.status_db2.text()
            dates = self.item_info_window.dates_db2.text()
            notes = self.item_info_window.notes_db2.text()
            Mimisbrunnr_2.add_row(location, description, package, product,
                manufacturer, assigned, status, dates, notes)

        self.load_data()
        tool_Scan_Mode.show()
        global_Asset_Tag.clear()
        global_Serial_Number.clear()
        if "SN:" in package:
            global_Serial_Number.setText('SN: ')
        if r"//" in package:
            global_Serial_Number.setText('//192.168.')
        global_Serial_Number.setFocus()
        if tutorial == QMessageBox.StandardButton.Yes:
            simpleaudio.stop_all()
            tyr_entry_added.play()
        ## APPLICATION LOG ##############################################
        try:
            AppLog('main', product, manufacturer, description, package)
        except Exception:
            pass

    def refresh(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def clear(self):
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

        elif self.key == db_secondary:
            self.item_info_window.item_db2_id_label.setText(lb_id)
            self.item_info_window.description_db2.clear()
            self.item_info_window.location_db2.clear()
            self.item_info_window.package_db2.clear()
            self.item_info_window.assigned_db2.clear()
            self.item_info_window.status_db2.clear()
            self.item_info_window.dates_db2.clear()
            self.item_info_window.notes_db2.clear()
        
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

        elif self.key == db_secondary:
            description = self.item_info_window.description_db2.text()
            location = self.item_info_window.location_db2.text()
            product = self.item_info_window.product_db2.itemText(
                self.item_info_window.product_db2.currentIndex())
            status = self.item_info_window.status_db2.text()
            dates = self.item_info_window.dates_db2.text()
            notes = self.item_info_window.notes_db2.text()
            self.result = Mimisbrunnr_2.search_rows(
                description, location, product, status, dates, notes)

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
                if lb_aesir in str(first_matched_item[1]):
                    self.item_info_window.location_db1.addItems(lb_locations_aesir)
                elif lb_vanir in str(first_matched_item[1]):
                    self.item_info_window.location_db1.addItems(lb_locations_vanir)
                self.item_info_window.product_db1.clear()
                self.item_info_window.product_db1.addItem(
                    first_matched_item[3])
                self.item_info_window.manufacturer_db1.clear()
                self.item_info_window.manufacturer_db1.addItem(
                    first_matched_item[4])
                if lb_chromebooks in str(first_matched_item[3]):
                    self.item_info_window.manufacturer_db1.addItems(lb_brands_chromebook)
                elif lb_dvr in str(first_matched_item[3]):
                    self.item_info_window.manufacturer_db1.addItems(lb_brands_dvr)
                elif lb_netprinters in str(first_matched_item[3]) or lb_locprinters in str(first_matched_item[3]) or lb_toner in str(first_matched_item[3]):
                    self.item_info_window.manufacturer_db1.addItems(lb_brands_printer)
                elif lb_winlaptops in str(first_matched_item[3]):
                    self.item_info_window.manufacturer_db1.addItems(lb_brands_laptop)
                self.item_info_window.assettag_db1.setText(
                    str(first_matched_item[5]))
                self.item_info_window.package_db1.setText(
                    str(first_matched_item[6]))
                self.item_info_window.assigned_db1.clear()
                self.item_info_window.assigned_db1.addItem(
                    str(first_matched_item[7]))
                self.item_info_window.assigned_db1.addItems(user_list)
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
            elif self.key == db_secondary:
                first_matched_item = Mimisbrunnr_2.search_row(id)
                self.item_info_window.item_db2_id_label.setText(
                    "ID #:{:>35}".format(id))
                self.item_info_window.location_db2.setText(
                    str(first_matched_item[1]))
                self.item_info_window.description_db2.setText(
                    str(first_matched_item[2]))
                self.item_info_window.product_db2.setCurrentText(
                    first_matched_item[4])
                self.item_info_window.package_db2.setText(
                    str(first_matched_item[3]))
                self.item_info_window.assigned_db2.setText(
                    str(first_matched_item[6]))
                self.item_info_window.manufacturer_db2.setCurrentText(
                    first_matched_item[5])
                self.item_info_window.status_db2.setText(
                    str(first_matched_item[7]))
                self.item_info_window.dates_db2.setText(
                    str(first_matched_item[8]))
                self.item_info_window.notes_db2.setText(
                    str(first_matched_item[9]))
            if isinstance(id, int):
                print("int")
            if isinstance(id, str):
                print("string")
            print(str(first_matched_item[5]))
        except Exception:
            if self.key == db_primary:
                self.item_info_window.item_db1_id_label.setText("ID:")
            elif self.key == db_secondary:
                self.item_info_window.item_db2_id_label.setText("ID:")
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
                    for row_count in range(1,9999):
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
                                    if lb_aesir in str(first_matched_item[1]):
                                        self.item_info_window.location_db1.addItems(lb_locations_aesir)
                                    elif lb_vanir in str(first_matched_item[1]):
                                        self.item_info_window.location_db1.addItems(lb_locations_vanir)
                                    self.item_info_window.product_db1.clear()
                                    self.item_info_window.product_db1.addItem(
                                        first_matched_item[3])
                                    self.item_info_window.manufacturer_db1.clear()
                                    self.item_info_window.manufacturer_db1.addItem(
                                        first_matched_item[4])
                                    if lb_chromebooks in str(first_matched_item[3]):
                                        self.item_info_window.manufacturer_db1.addItems(lb_brands_chromebook)
                                    elif lb_dvr in str(first_matched_item[3]):
                                        self.item_info_window.manufacturer_db1.addItems(lb_brands_dvr)
                                    elif lb_netprinters in str(first_matched_item[3]) or lb_locprinters in str(first_matched_item[3]) or lb_toner in str(first_matched_item[3]):
                                        self.item_info_window.manufacturer_db1.addItems(lb_brands_printer)
                                    elif lb_winlaptops in str(first_matched_item[3]):
                                        self.item_info_window.manufacturer_db1.addItems(lb_brands_laptop)    
                                    self.item_info_window.assettag_db1.setText(
                                        str(first_matched_item[5]))
                                    self.item_info_window.package_db1.setText(
                                        str(first_matched_item[6]))
                                    self.item_info_window.assigned_db1.clear()
                                    self.item_info_window.assigned_db1.addItem(
                                        str(first_matched_item[7]))
                                    self.item_info_window.assigned_db1.addItems(user_list)
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
                elif help_requested[1] == "TUTORIAL":
                    os.remove(tyr_log_tutorial)
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
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
                run_search = True
                print("Searching by: Serial Number")
                arg_serial_no = general_input.split(":")
                serial_no = arg_serial_no[1]
                if serial_no[0] == " ":
                    serial_no = serial_no.strip()
                serial_no_length = len(serial_no)
                search_bar_general.clear()
                if serial_no_length < 1:
                    run_search == False
                elif serial_no_length == 7:
                    print("Serial Number Match: Dell")
                elif serial_no_length == 8:
                    print("Serial Number Match: Lenovo")
                print("Serial No:", serial_no)
                try:
                    try:
                        if self.key == db_primary:
                            for row_count in range(1,9999):
                                # clear_term()
                                ## list_row lists all the values in the given row using .search_row
                                list_row = Mimisbrunnr_1.search_row(row_count)
                                ## item_asset_tag equals the fifth element in the row, which is the asset tag
                                try:
                                    item_serial_num = list_row[6]
                                except Exception:
                                    for x in range(1,1):
                                        pass
                                ## If the tag that you searched for shows up in the above query
                                ## Populate the forms
                                try:
                                    item_serial_num = list_row[6]
                                except Exception:
                                    for x in range(1,1):
                                        pass
                                ## If the tag that you searched for shows up in the above query
                                ## Populate the forms
                                try:
                                    if serial_no in item_serial_num:
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
                                            if lb_aesir in str(first_matched_item[1]):
                                                self.item_info_window.location_db1.addItems(lb_locations_aesir)
                                            elif lb_vanir in str(first_matched_item[1]):
                                                self.item_info_window.location_db1.addItems(lb_locations_vanir)
                                            self.item_info_window.product_db1.clear()
                                            self.item_info_window.product_db1.addItem(
                                                first_matched_item[3])
                                            self.item_info_window.manufacturer_db1.clear()
                                            self.item_info_window.manufacturer_db1.addItem(
                                                first_matched_item[4])
                                            if lb_chromebooks in str(first_matched_item[3]):
                                                self.item_info_window.manufacturer_db1.addItems(lb_brands_chromebook)
                                            elif lb_dvr in str(first_matched_item[3]):
                                                self.item_info_window.manufacturer_db1.addItems(lb_brands_dvr)
                                            elif lb_netprinters in str(first_matched_item[3]) or lb_locprinters in str(first_matched_item[3]) or lb_toner in str(first_matched_item[3]):
                                                self.item_info_window.manufacturer_db1.addItems(lb_brands_printer)
                                            elif lb_winlaptops in str(first_matched_item[3]):
                                                self.item_info_window.manufacturer_db1.addItems(lb_brands_laptop)    
                                            self.item_info_window.assettag_db1.setText(
                                                str(first_matched_item[5]))
                                            self.item_info_window.package_db1.setText(
                                                str(first_matched_item[6]))
                                            self.item_info_window.assigned_db1.clear()
                                            self.item_info_window.assigned_db1.addItem(
                                                str(first_matched_item[7]))
                                            self.item_info_window.assigned_db1.addItems(user_list)
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
                    except Exception:
                        pass
                except Exception:
                    pass
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
            # Mimisbrunnr_1.update_row(id, location, product, asset_tag, manufacturer, package,
            #                       assigned, status, dates, notes)

        elif self.key == db_secondary:
            description = self.item_info_window.description_db2.text()
            location = self.item_info_window.location_db2.text()
            product = self.item_info_window.product_db2.itemText(
                self.item_info_window.product_db2.currentIndex())
            package = self.item_info_window.package_db2.text()
            assigned = self.item_info_window.assigned_db2.text()
            manufacturer = self.item_info_window.manufacturer_db2.itemText(
                self.item_info_window.manufacturer_db2.currentIndex())
            status = self.item_info_window.status_db2.text()
            dates = self.item_info_window.dates_db2.text()
            notes = self.item_info_window.notes_db2.text()
            Mimisbrunnr_2.update_row(id, description, location, product,
                                   package, assigned, manufacturer, status, dates, notes)

        QMessageBox.information(
            QMessageBox(), "Update", "Item has been updated.")
        self.load_data()

    def clear_contents(self):
        self.tableWidget.clearContents()

    def delete(self):
        id = self.search_box.text()
        self.msgSearch = QMessageBox()
        try:
            if self.key == db_primary:
                row = Mimisbrunnr_1.search_row(id)
                search_result = lb_id+"    "+str(row[0])+"\n"+lb_location+"     "+str(row[1])+"\n"+lb_product+"     "+str(row[2])+"\n"   \
                                + lb_make+"     "+str(row[3])+"\n"+lb_asset+"     "+str(row[4])+"\n"+lb_reference+"     "+str(row[5])+"\n"+lb_assigned+"     " + str(row[6])+"\n" \
                                + lb_status+"     " + \
                    str(row[7])+"\n"+lb_date+"     " + \
                    str(row[8])+"\n"+lb_info+"   "+str(row[9])
            elif self.key == db_secondary:
                row = Mimisbrunnr_2.search_row(id)
                search_result = lb_id+"    "+str(row[0])+"\n"+lb_location+"     "+str(row[1])+"\n"+lb_product+"     "+str(row[2])+"\n"   \
                                + lb_make+"     "+str(row[3])+"\n"+lb_asset+"     "+str(row[4])+"\n"+lb_reference+"     "+str(row[5])+"\n"+lb_assigned+"     " + str(row[6])+"\n" \
                                + lb_status+"     " + \
                    str(row[7])+"\n"+lb_date+"     " + \
                    str(row[8])+"\n"+lb_info+"   "+str(row[9])
            self.msgSearch.setText(search_result)
            self.msgSearch.setInformativeText(
                "Do you want to remove this item?")
            self.msgSearch.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            self.msgSearch.setDefaultButton(QMessageBox.StandardButton.Yes)
            self.msgSearch.setWindowTitle("Remove item?")
            ret = self.msgSearch.exec()
            if ret == QMessageBox.StandardButton.Yes:
                if self.key == db_primary:
                    Mimisbrunnr_1.delete_row(id)
                    self.item_info_window.item_db1_id_label.setText(lb_id)
                    self.item_info_window.site_db1.clear()
                    self.item_info_window.product_db1.clear()
                    self.item_info_window.manufacturer_db1.clear()
                    self.item_info_window.assettag_db1.clear()
                    self.item_info_window.location_db1.clear()
                    self.item_info_window.package_db1.clear()
                    self.item_info_window.assigned_db1.clear()
                    self.item_info_window.status_db1.clear()
                    self.item_info_window.dates_db1.clear()
                    self.item_info_window.notes_db1.clear()
                elif self.key == db_secondary:
                    Mimisbrunnr_2.delete_row(id)
                    self.item_info_window.item_db2_id_label.setText(lb_id)
                    self.item_info_window.description_db2.clear()
                    self.item_info_window.location_db2.clear()
                    self.item_info_window.package_db2.clear()
                    self.item_info_window.assigned_db2.clear()
                    #self.item_info_window.status_db2.clear()
                    self.item_info_window.dates_db2.clear()
                    self.item_info_window.notes_db2.clear()
            elif ret == QMessageBox.StandardButton.No:
                pass
        except Exception:
            # QMessageBox.warning(QMessageBox(), "Error",
            #                     "Could not remove the item")
            pass
        finally:
            self.load_data()

    def delete_move(self):
        id = self.search_box.text()
        self.msgSearch = QMessageBox()
        try:
            if self.key == db_primary:
                row = Mimisbrunnr_1.search_row(id)
                search_result = lb_id+"    "+str(row[0])+"\n"+lb_location+"     "+str(row[1])+"\n"+lb_product+"     "+str(row[2])+"\n"   \
                                + lb_make+"     "+str(row[3])+"\n"+lb_asset+"     "+str(row[4])+"\n"+lb_reference+"     "+str(row[5])+"\n"+lb_assigned+"     " + str(row[6])+"\n" \
                                + lb_status+"     " + \
                    str(row[7])+"\n"+lb_date+"     " + \
                    str(row[8])+"\n"+lb_info+"   "+str(row[9])
            elif self.key == db_secondary:
                row = Mimisbrunnr_2.search_row(id)
                search_result = lb_id+"    "+str(row[0])+"\n"+lb_location+"     "+str(row[1])+"\n"+lb_product+"     "+str(row[2])+"\n"   \
                                + lb_make+"     "+str(row[3])+"\n"+lb_asset+"     "+str(row[4])+"\n"+lb_reference+"     "+str(row[5])+"\n"+lb_assigned+"     " + str(row[6])+"\n" \
                                + lb_status+"     " + \
                    str(row[7])+"\n"+lb_date+"     " + \
                    str(row[8])+"\n"+lb_info+"   "+str(row[9])
            self.msgSearch.setText(search_result)
            self.msgSearch.setInformativeText(
                "Do you want to move this item?")
            self.msgSearch.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            self.msgSearch.setWindowTitle("Move item?")
            ret = self.msgSearch.exec()
            if ret == QMessageBox.StandardButton.Yes:
                if self.key == db_primary:
                    Mimisbrunnr_1.delete_row(id)
                    self.item_info_window.item_db1_id_label.setText(lb_id)
                    self.item_info_window.assettag_db1.clear()
                    self.item_info_window.location_db1.clear()
                    self.item_info_window.package_db1.clear()
                    self.item_info_window.assigned_db1.clear()
                    self.item_info_window.status_db1.clear()
                    self.item_info_window.dates_db1.clear()
                    self.item_info_window.notes_db1.clear()
                elif self.key == db_secondary:
                    Mimisbrunnr_2.delete_row(id)
                    self.item_info_window.item_db2_id_label.setText(lb_id)
                    self.item_info_window.description_db2.clear()
                    self.item_info_window.location_db2.clear()
                    self.item_info_window.package_db2.clear()
                    self.item_info_window.assigned_db2.clear()
                    self.item_info_window.status_db2.clear()
                    self.item_info_window.dates_db2.clear()
                    self.item_info_window.notes_db2.clear()
            elif ret == QMessageBox.StandardButton.No:
                pass
        except Exception:
            QMessageBox.warning(QMessageBox(), "Error",
                                "Could not move the item")
        finally:
            self.load_data()

    def move(self):
        if self.key == db_primary:
            description = self.item_info_window.assettag_db1.text()
            location = self.item_info_window.location_db1.currentText()
            product = self.item_info_window.product_db1.itemText(
                self.item_info_window.product_db1.currentIndex())
            package = self.item_info_window.package_db1.text()
            assigned = self.item_info_window.assigned_db1.text()
            manufacturer = self.item_info_window.manufacturer_db1.itemText(
                self.item_info_window.manufacturer_db1.currentIndex())
            status = self.item_info_window.status_db1.text()
            dates = self.item_info_window.dates_db1.text()
            notes = self.item_info_window.notes_db1.text()
            Mimisbrunnr_2.add_row(location, description, package, product,
                                 manufacturer, assigned, status, dates, notes)
        elif self.key == db_secondary:
            description = self.item_info_window.description_db2.text()
            location = self.item_info_window.location_db2.text()
            product = self.item_info_window.product_db2.itemText(
                self.item_info_window.product_db2.currentIndex())
            package = self.item_info_window.package_db2.text()
            assigned = self.item_info_window.assigned_db2.text()
            manufacturer = self.item_info_window.manufacturer_db2.itemText(
                self.item_info_window.manufacturer_db2.currentIndex())
            status = self.item_info_window.status_db2.text()
            dates = self.item_info_window.dates_db2.text()
            notes = self.item_info_window.notes_db2.text()
            Mimisbrunnr_1.add_row(location, description, package, product,
                                 manufacturer, assigned, status, dates, notes)

        self.delete_move()
        self.load_data()

    def export(self):
        export_dir = True
        if export_dir:
            mimisbrunnr_export_csv_1 = (mimisbrunnr_export_dir + "CSV/" + "Mimisbrunnr_1.csv")
            mimisbrunnr_export_html_1 = (mimisbrunnr_export_dir + "HTML/" + "Mimisbrunnr_1.html")
            mimisbrunnr_export_pdf_1 = (mimisbrunnr_export_dir + "PDF/" + "Mimisbrunnr_1.pdf")
            mimisbrunnr_export_csv_2 = (mimisbrunnr_export_dir + "CSV/Mimisbrunnr_2.csv")
        try:
            if self.key == db_primary:
                Mimisbrunnr_1.to_csv()
                loaded_export = pd.read_csv(mimisbrunnr_export_csv_1)
                loaded_export.to_html(mimisbrunnr_export_html_1)
                with open(mimisbrunnr_export_csv_1, newline='') as f:
                    reader = csv.reader(f)
                    pdf = FPDF()
                    pdf.add_page(orientation = 'L')
                    page_width = pdf.w - 8 * pdf.l_margin
                    pdf.set_font('Times','B',14.0) 
                    pdf.cell(page_width, 0.0, 'Mimisbrunnr Export')
                    pdf.ln(6)
                    pdf.set_font('Times','',10.0)
                    pdf.cell(page_width, 0.0, f'Date: {date_today}')
                    pdf.ln(10)                  
                    pdf.set_font('Courier', '', 6.5)
                    col_width = page_width/6.4
                    pdf.ln(1)
                    th = pdf.font_size * 2
                    bold = True
                    for row in reader:
                        if bold:
                            pdf.set_font('Helvetica', 'B', 9.5)
                            bold = not bold
                        else:
                            pdf.set_font('Times', '', 8.5)
                        pdf.cell(col_width, th, str(row[0]), border=1, align='C')
                        pdf.cell(col_width, th, row[1], border=1, align='C')
                        pdf.cell(col_width, th, row[2], border=1, align='C')
                        pdf.cell(col_width, th, row[3], border=1, align='C')
                        pdf.cell(col_width, th, row[4], border=1, align='C')
                        pdf.cell(col_width, th, row[5], border=1, align='C')
                        pdf.cell(col_width, th, row[6], border=1, align='C')
                        pdf.cell(col_width, th, row[9], border=1, align='C')
                        pdf.ln(th)
                    pdf.ln(10)
                    pdf.set_font('Times','',10.0)
                    pdf.cell(page_width, 0.0, '- end of report -')

                    pdf.output(mimisbrunnr_export_pdf_1, 'F')
            elif self.key == db_secondary:
                Mimisbrunnr_2.to_csv()
            QMessageBox.information(
                QMessageBox(), "File export", "Mimir: Exporting...\n\nCSV: Done\n\nHTML: Done\n\nPDF: Done\n\nMimir: Export Complete!")
        except Exception:
            QMessageBox.warning(QMessageBox(), "Error",
                                "Could not export to csv")
        finally:
            pass

    def wipe_mimir(self):
        reply = QMessageBox.question(self, 'Wipe Mimir', 'Delete all Entries?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
        if reply == QMessageBox.StandardButton.Yes:
            if os.path.isfile(inventory_db):
                os.remove(inventory_db)
                self.refresh()
        else:
            pass

    def update_pdf(self):
        export_dir = True
        if export_dir:
            mimisbrunnr_export_csv_1 = (mimisbrunnr_export_dir + "CSV/" + "Mimisbrunnr_1.csv")
            mimisbrunnr_export_html_1 = (mimisbrunnr_export_dir + "HTML/" + "Mimisbrunnr_1.html")
            mimisbrunnr_export_pdf_1 = (mimisbrunnr_export_dir + "PDF/" + "Mimisbrunnr_1.pdf")
            mimisbrunnr_export_csv_2 = (mimisbrunnr_export_dir + "CSV/Mimisbrunnr_2.csv")
        try:
            if self.key == db_primary:
                loaded_export = pd.read_csv(mimisbrunnr_export_csv_1)
                loaded_export.to_html(mimisbrunnr_export_html_1)
                with open(mimisbrunnr_export_csv_1, newline='') as f:
                    reader = csv.reader(f)
                    pdf = FPDF()
                    pdf.add_page(orientation = 'L')
                    page_width = pdf.w - 8 * pdf.l_margin
                    pdf.set_font('Times','B',14.0) 
                    pdf.cell(page_width, 0.0, 'Mimisbrunnr Export')
                    pdf.ln(6)
                    pdf.set_font('Times','',10.0)
                    pdf.cell(page_width, 0.0, f'Date: {date_today}')
                    pdf.ln(10)                  
                    pdf.set_font('Courier', '', 6.5)
                    col_width = page_width/6.4
                    pdf.ln(1)
                    th = pdf.font_size * 2
                    bold = True
                    for row in reader:
                        if bold:
                            pdf.set_font('Helvetica', 'B', 9.5)
                            bold = not bold
                        else:
                            pdf.set_font('Times', '', 8.5)
                        pdf.cell(col_width, th, str(row[0]), border=1, align='C')
                        pdf.cell(col_width, th, row[1], border=1, align='C')
                        pdf.cell(col_width, th, row[2], border=1, align='C')
                        pdf.cell(col_width, th, row[3], border=1, align='C')
                        pdf.cell(col_width, th, row[4], border=1, align='C')
                        pdf.cell(col_width, th, row[5], border=1, align='C')
                        pdf.cell(col_width, th, row[6], border=1, align='C')
                        pdf.cell(col_width, th, row[9], border=1, align='C')
                        pdf.ln(th)
                    pdf.ln(10)
                    pdf.set_font('Times','',10.0)
                    pdf.cell(page_width, 0.0, '- end of report -')

                    pdf.output(mimisbrunnr_export_pdf_1, 'F')
            elif self.key == db_secondary:
                Mimisbrunnr_2.to_csv()
            QMessageBox.information(
                QMessageBox(), "File export", "Mimir: Exporting...\n\nHTML: Done\n\nPDF: Done\n\nMimir: Export Complete!")
        except Exception:
            QMessageBox.warning(QMessageBox(), "Error",
                                "Could not export to csv")
        finally:
            pass

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
        self.Mimisbrunnr_label.setFont(QFont("Arial", 14))
        self.Mimisbrunnr_label.setFixedSize(100, 30)
        self.Mimisbrunnr_label.hide()
        self.item_label_db1 = QLabel("Item Information")
        self.item_label_db1.setFont(QFont("Arial", 14))
        self.item_label_db1.setFixedSize(250, 40)
        self.item_label_db1.hide()
        self.item_label_db2 = QLabel("Item Information")
        self.item_label_db2.setFont(QFont("Arial", 14))
        self.item_label_db2.setFixedSize(250, 40)
        self.item_label_db2.hide()

        self.picLabel = QLabel()
        self.pixmap = QPixmap(png_db_primary)
        self.pixmap = self.pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.FastTransformation)
        # self.pixmap = self.pixmap.scaled(300, 200, QtCore.Qt.AspectRatioMode)
        # ERRORMESSAGE
        # self.pixmap = self.pixmap.scaledToWidth(300)
        self.picLabel.setPixmap(self.pixmap)
        # self.picLabel.setFixedSize(300, 150)
        # self.picLabel.setFixedHeight(300)
        

        # Create and connect the combo box to switch between different inventory Mimisbrunnr
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(
            [db_primary, db_secondary, db_tertiary])
        self.pageCombo.hide()
        self.pageCombo.activated.connect(self.switchPage)

        # Layouts
        self.stackedLayout = QStackedLayout()
        sub_layout.addWidget(self.Mimisbrunnr_label)
        sub_layout.addWidget(self.pageCombo)
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
        self.item_db1_id_label = QLabel(f"Týr - {app_version}" + self.item_db1_id)
        self.page_db1_layout.addWidget(self.item_label_db1)
        self.page_db1_layout.addWidget(self.item_db1_id_label)
        
        self.site_db1 = QComboBox()
        self.site_db1.addItem(lb_aesir)
        self.site_db1.addItem(lb_vanir)
        self.site_db1.addItem(lb_midgard)
        self.form_layout_db1.addRow(lb_site, self.site_db1)

        global product_selection
        global search_selection
        search_selection = "Search..."
        self.product_db1 = QComboBox()
        self.product_db1.addItem(lb_default_dropdown)
        self.product_db1.addItem(search_selection)  
        self.product_db1.addItem("")
        self.product_db1.addItem(lb_desktop, (lb_brands_desktops))
        self.product_db1.addItem(lb_dvr, (lb_brands_dvr))
        self.product_db1.addItem(lb_chromebooks, (lb_brands_chromebook))
        self.product_db1.addItem(lb_winlaptops, (lb_brands_laptop))
        self.product_db1.addItem(lb_locprinters, (lb_brands_printer))
        self.product_db1.addItem(lb_netprinters, (lb_brands_printer))
        self.product_db1.addItem(lb_toner, (lb_brands_printer))

        self.product_db1.currentIndexChanged.connect(self.updatemanufacturerInput)
        self.form_layout_db1.addRow(lb_product, self.product_db1)
        product_selection = self.product_db1
        product_selection.activated.connect(self.pass_Net_Adap) # Passes active selection
        global starting_page
        starting_page = True
        if starting_page:
            starting_page = not starting_page
            self.shortcut_search = QShortcut(QKeySequence('Ctrl+s'), self)
            self.shortcut_search.activated.connect(self.pass_Net_Adap)
        
        self.manufacturer_db1 = QComboBox()
        
        self.assettag_db1 = QLineEdit()

        self.package_db1 = QLineEdit()
        

        self.page_db1_layout.addLayout(self.form_layout_db1)

        self.page_db1.setLayout(self.page_db1_layout)
        self.stackedLayout.addWidget(self.page_db1)

        # -------------------------- #
        #     Secondary Mimisbrunnr     #
        # -------------------------- #
        self.page_db2 = QWidget()
        self.page_db2_layout = QVBoxLayout()
        self.form_layout_db2 = QFormLayout()

        self.item_db2_id = ""
        self.item_db2_id_label = QLabel(lb_id+"  " + self.item_db2_id)
        self.page_db2_layout.addWidget(self.item_label_db2)
        self.page_db2_layout.addWidget(self.item_db2_id_label)

        self.description_db2 = QLineEdit()
        self.form_layout_db2.addRow(lb_product, self.description_db2)
        
        self.package_db2 = QLineEdit()
        self.form_layout_db2.addRow(lb_make, self.package_db2)

        self.location_db2 = QLineEdit()
        self.form_layout_db2.addRow(
            lb_location, self.location_db2)

        self.product_db2 = QComboBox()
        self.product_db2.addItem(lb_default_dropdown)
        self.product_db2.addItem(lb_desktop, ["Black", "Blue", "Brown", "Green", "Grey", "Yellow", "White"])
        self.product_db2.addItem(lb_dvr, ["Black", "Blue", "Brown", "Green", "Grey", "Yellow", "White"])
        self.product_db2.currentIndexChanged.connect(self.updatemanufacturerInput_2)
        self.form_layout_db2.addRow(lb_asset, self.product_db2)
        
        self.manufacturer_db2 = QComboBox()
        self.manufacturer_db2.addItems([lb_default_dropdown])
        self.form_layout_db2.addRow(lb_reference, self.manufacturer_db2)

        self.assigned_db2 = QLineEdit()
        self.form_layout_db2.addRow(lb_assigned, self.assigned_db2)

        self.status_db2 = QLineEdit()
        self.form_layout_db2.addRow(lb_status, self.status_db2)

        self.dates_db2 = QLineEdit()
        self.form_layout_db2.addRow(lb_date, self.dates_db2)

        self.notes_db2 = QLineEdit()
        self.form_layout_db2.addRow(lb_info, self.notes_db2)

        self.page_db2_layout.addLayout(self.form_layout_db2)

        self.page_db2.setLayout(self.page_db2_layout)
        self.stackedLayout.addWidget(self.page_db2)

        self.db_id = 0

        ## FLOATING TOOLS
        global tool_Scan_Mode
        tool_Scan_Mode = QCheckBox('Scan Mode', self)
        tool_Scan_Mode.move(80, 10)
        tool_Scan_Mode.hide()
        tool_Scan_Mode.stateChanged.connect(self.enable_Auto_Tag)
    
    def focus_AT(self):
        # global_Serial_Number.clearFocus()
        try:
            global_Asset_Tag.disconnect()
            global_Asset_Tag.setFocus()
            global_Asset_Tag.returnPressed.connect(btn_add.click)
        except:
            global_Asset_Tag.setFocus()
            global_Asset_Tag.returnPressed.connect(btn_add.click)

    def enable_Auto_Tag(self, state):
        if state == Qt.CheckState.Checked.value:
            global_Serial_Number.setFocus()
            global_Serial_Number.returnPressed.connect(self.focus_AT)
        else:
            try:
                global_Asset_Tag.disconnect()
                global_Serial_Number.disconnect()
            except:
                pass

    # When called, takes the input and checks which lb_drop# was selected
    # and launches a unique follow-up window if additional information is required
    def pass_Net_Adap(self):
        if starting_page == False:
            self.shortcut_search = QShortcut(QKeySequence('Ctrl+s'), self)
            self.shortcut_search.activated.connect(btn_search.click)
        if search_selection in (str(product_selection.currentText())):
            self.manufacturer_db1.clear()
            self.assettag_db1.clear()
            self.manufacturer_db1.addItem(search_selection)
            # calling method
            self.UiComponents()
  
            # showing all the widgets
            self.show()
            pass
        elif lb_dvr in (str(product_selection.currentText())):
            super().__init__()
  
            # setting title
            self.setWindowTitle("Python ")
  
            # setting geometry
            self.setGeometry(500, 350, 225, 90)
  
            # calling method
            self.UiComponents()
  
            # showing all the widgets
            self.show()
            pass
        elif lb_chromebooks or lb_winlaptops or lb_desktop in (str(product_selection.currentText())):
            super().__init__()
  
            # setting title
            self.setWindowTitle("Python ")
  
            # setting geometry
            self.setGeometry(500, 350, 250, 90)
  
            # calling method
            self.UiComponents()
  
            # showing all the widgets
            self.show()
            pass
        elif lb_locprinters in (str(product_selection.currentText())):
            pass
        elif lb_netprinters in (str(product_selection.currentText())):
            super().__init__()
  
            # setting title
            self.setWindowTitle("Python ")
  
            # setting geometry
            self.setGeometry(500, 350, 225, 90)
  
            # calling method
            self.UiComponents()
  
            # showing all the widgets
            self.show()
            pass
        elif lb_toner in (str(product_selection.currentText())):
            print(lb_netprinters)
            
            super().__init__()
  
            # setting title
            self.setWindowTitle("Python ")
  
            # setting geometry
            self.setGeometry(500, 350, 225, 90)
  
            # calling method
            self.UiComponents()
  
            # showing all the widgets
            self.show()
            pass
        else:
            pass

    # The follow-up window, unique to each selection
    def UiComponents(self):
        # creating a combo box widget
        self.line = QLineEdit(self)
        self.nameLabel = QLabel(self)
        if search_selection in (str(product_selection.currentText())):
            print("UI Element")
            self.find()
            pass
        elif lb_dvr in (str(product_selection.currentText())):
            self.setWindowTitle("Enter IP Address")
            self.nameLabel.setText('192.168.')
            self.nameLabel.move(25, 25)
            # setting geometry of combo box
            self.line.setGeometry(85, 18, 120, 30)
            # creating label to 
            self.label = QLabel(self)
            # setting geometry of the label
            self.label.setGeometry(25, 50, 200, 30)
        elif lb_netprinters in (str(product_selection.currentText())):
            self.setWindowTitle("Enter IP Address")
            self.nameLabel.setText('192.168.')
            self.nameLabel.move(25, 25)
            # setting geometry of combo box
            self.line.setGeometry(85, 18, 120, 30)
            # creating label to 
            self.label = QLabel(self)
            # setting geometry of the label
            self.label.setGeometry(25, 50, 200, 30)
        elif lb_locprinters in (str(product_selection.currentText())):
            self.setWindowTitle("Enter Printer Purpose")
            self.nameLabel.setText('Purpose: ')
            self.nameLabel.move(20, 25)
            # setting geometry of combo box
            self.line.setGeometry(85, 18, 120, 30)
            # creating label to 
            self.label = QLabel(self)
            # setting geometry of the label
            self.label.setGeometry(25, 50, 200, 30)
        elif lb_toner in (str(product_selection.currentText())):
            self.setWindowTitle("Enter Toner Type")
            self.nameLabel.setText("Toner Type:")
            self.nameLabel.move(5, 25)
            self.line.setGeometry(85, 18, 150, 30)
            # creating label to 
            self.label = QLabel(self)
            # setting geometry of the label
            self.label.setGeometry(25, 50, 200, 30)
        elif lb_chromebooks or lb_winlaptops or lb_desktop in (str(product_selection.currentText())):
            self.setWindowTitle("Enter Service Tag")
            self.nameLabel.setText("Service Tag:")
            self.nameLabel.move(5, 25)
            self.line.setGeometry(85, 18, 150, 30)
            # creating label to 
            self.label = QLabel(self)
            # setting geometry of the label
            self.label.setGeometry(25, 50, 200, 30)
        if tutorial == QMessageBox.StandardButton.Yes:
            simpleaudio.stop_all()
            if lb_netprinters in (str(product_selection.currentText())) or lb_dvr in (str(product_selection.currentText())):
                tyr_IP.play()
            else:
                tyr_serial.play()
        self.line.returnPressed.connect(self.find)
  
    # Inserts the information from the previous window, into our main window
    def find(self):
        # finding the content of current item in combo box
        product_selection.disconnect()
        btn_add.show()
        search_bar.show()
        btn_search.show()
        search_bar_asset_tag.show()
        btn_search_asset_tag.show()
        search_bar_general.show()
        btn_search_general.show()
        btn_delete.show()
        btn_clear.show()
        btn_update.show()
        self.manufacturer_db1.addItems([lb_default_dropdown])
        self.form_layout_db1.addRow(lb_make, self.manufacturer_db1)
        selected_product = (str(product_selection.currentText()))
        
        user_text_input = self.line.text()
        self.package_db1.close()
        
        
        self.form_layout_db1.addRow(lb_asset, self.assettag_db1)
        global global_Asset_Tag
        global_Asset_Tag = self.assettag_db1
        self.package_db1 = QLineEdit()
        global global_Serial_Number
        global_Serial_Number = self.package_db1
        self.assigned_db1 = QComboBox()
        if lb_dvr or lb_netprinters or lb_locprinters in selected_product:
            self.assigned_db1.addItem("To Realm")
            self.assigned_db1.addItems(user_list)
        else:
            self.assigned_db1.addItems(user_list)
        self.form_layout_db1.addRow(lb_assigned, self.assigned_db1)
        self.location_db1 = QComboBox()
        if lb_aesir in str(self.site_db1.currentText()):
            self.location_db1.addItems(lb_locations_aesir)
        elif lb_vanir in str(self.site_db1.currentText()):
            self.location_db1.addItems(lb_locations_vanir)
        elif lb_aesir not in str(self.site_db1.currentText()) and lb_vanir not in str(self.site_db1.currentText()):
            self.location_db1.addItem("Midgard")
        self.form_layout_db1.addRow(lb_location, self.location_db1)
        
        self.status_db1 = QComboBox()
        #self.status_db1.addItems([lb_default_dropdown])
        self.status_db1.addItem(lb_deployed)
        self.status_db1.addItem(lb_instock)
        self.status_db1.addItem(lb_onorder)
        self.status_db1.addItem(lb_oos_repair)
        self.status_db1.addItem(lb_oos_obsolete)
        self.form_layout_db1.addRow(lb_status, self.status_db1)
        
        if lb_dvr in selected_product:
            # showing content on the screen though label
            self.label.setText("IP Address : " + "192.168." + user_text_input)
            self.form_layout_db1.addRow("IP Address:", self.package_db1)
            self.package_db1.insert("//192.168."+ user_text_input)
        elif lb_netprinters in selected_product:
            # showing content on the screen though label
            self.label.setText("IP Address : " + "192.168." + user_text_input)
            self.form_layout_db1.addRow("IP Address:", self.package_db1)
            self.package_db1.insert("//192.168."+ user_text_input)
        elif lb_locprinters in selected_product:
            self.label.setText("Printer Purpose:" + user_text_input)
            self.form_layout_db1.addRow("Purpose:", self.package_db1)
            self.package_db1.insert("* "+ user_text_input)
        elif lb_toner in selected_product:
            GPR_37 = ["GPR-37", "GPR37", "37"]
            GPR_38 = ["GPR-38", "GPR38", "38"]
            if any(x in user_text_input.upper() for x in GPR_37):
                user_text_input = "GPR-37"
            elif any(x in user_text_input.upper() for x in GPR_38):
                user_text_input = "GPR-38"
            else:
                pass
            self.label.setText("Type: " + user_text_input)
            self.form_layout_db1.addRow("Model of Toner:", self.package_db1)
            self.package_db1.insert("Type: "+ user_text_input)
        elif lb_chromebooks or lb_winlaptops or lb_desktop in selected_product:
            # showing content on the screen though label
            user_text_input = user_text_input.upper()
            self.label.setText("Service Tag : " + user_text_input)
            self.form_layout_db1.addRow("Service Tag:", self.package_db1)
            self.package_db1.insert("SN: " + user_text_input)
        
        self.notes_db1 = QLineEdit()
        global global_Info
        global_Info = self.notes_db1
        if "GPR" in user_text_input:
            self.manufacturer_db1.clear()
            self.manufacturer_db1.addItem("Canon")
            self.assettag_db1.insert("N/A")
            self.status_db1.clear()
            for x in range(1, 10):
                self.status_db1.addItem("Quantity: " + str(x))
            if "GPR-37" in user_text_input:
                self.notes_db1.insert("Compatibility: 8085 / 8095 / 8105")
            elif "GPR-38" in user_text_input:
                self.notes_db1.insert("Compatibility: 6075 / 6265 / 6025")
        self.form_layout_db1.addRow(lb_info, self.notes_db1)
        
        self.dates_db1 = QLineEdit()
        self.dates_db1.insert(today)
        self.form_layout_db1.addRow(lb_date, self.dates_db1)
        
        self.notes_db1.returnPressed.connect(btn_add.click)
        self.close()
        # SETS ASSET TAG LINE IN FOCUS
        self.assettag_db1.setFocus()

        if tutorial == QMessageBox.StandardButton.Yes:
            simpleaudio.stop_all()
            tyr_initialize.play()

    def updatemanufacturerInput(self, index):
        self.manufacturer_db1.clear()
        categories = self.product_db1.itemData(index)
        if categories:
            self.manufacturer_db1.addItems(categories)
    
    def updatemanufacturerInput_2(self, index):
        self.manufacturer_db2.clear()
        categories = self.product_db2.itemData(index)
        if categories:
            self.manufacturer_db2.addItems(categories)

    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())
        self.db_id = self.pageCombo.currentIndex()
        return self.db_id
## TYR SYSTEM LOG #################################################
def AppLog(log, type, make, asset, serial):
    if log == "main":
        with open(tyr_log, 'a') as f:
            if type == "start":
                f.write(f'{user} started Tyr ::: {today}\n')
            else:
                f.write(f'{user} added a {type} ::: {today}\n')
                f.write(f":: {make} - ")
                f.write(f"{asset} - ")
                f.write(f"{serial}\n")
## MIMIR IMPORT ###################################################
class mainWin(QMainWindow):
    def __init__(self, parent = None):
        super(mainWin, self).__init__(parent)
        self.setupUI()
        
    def setupUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setContentsMargins(10, 5, 10, 5)
        self.lb = QTableWidget()
        self.setCentralWidget(self.lb)
        # self.create_toolbar()
        self.csv_file = ""
        self.csv_file_name = ""
             
    def open_file(self):
        fname,_ = QFileDialog.getOpenFileName(self, 'Open file', '', 
                                              "CSV Files (*.csv *.tsv *.txt);;All Files (*.*)")
        if fname:
            self.csv_file = fname
            self.load_csv(self.csv_file)
            self.statusbar.showMessage(f"{fname} loaded")
            
    def save_file(self):
        if self.lb.rowCount() < 1:
            return
        if self.csv_file != "":
            file_name = self.csv_file
        else:
            file_name = "*.csv"
            
        fname,_ = QFileDialog.getSaveFileName(self, 'Save file', file_name, 
                                              "CSV Files (*.csv *.tsv *.txt);;All Files (*.*)")
        if fname:
            self.save_csv(fname)
            self.csv_file = fname
            
    def save_csv(self, filename):
        rowtext = ""
        for row in range(self.lb.rowCount()-1):
            
            for column in range(self.lb.columnCount()-1):
                celltext = self.lb.item(row, column).text()
                rowtext += f"{celltext}\t"
                # ERROR MESSAGE
            rowtext = rowtext.rstrip("\t")
            rowtext += "\n"
        with open(filename, "w") as f:
            f.write(rowtext)

    def load_csv(self, filename):
        self.csv_text = open(filename, "r").read()
        ### count tab / comma
        tab_counter = self.csv_text.splitlines()[0].count("\t")
        comma_counter = self.csv_text.splitlines()[0].count(",")
        if tab_counter > comma_counter:
            self.lb.setColumnCount(tab_counter + 1)
            delimiter = "\t"
        else:
            self.lb.setColumnCount(comma_counter + 1)
            delimiter = ","
        
        row = 0
        for listrow in self.csv_text.splitlines():
            self.lb.insertRow(row)
            rowtext = listrow.split(delimiter)
            column = 0
            for cell in rowtext:
                celltext = QTableWidgetItem(cell)
                self.lb.setItem(row, column, celltext)
                column += 1
            row += 1
## MIMISBRUNNR ####################################################
if __name__ == "__main__":
    mimir_exists = os.path.isfile(inventory_db)

    if mimir_exists:
        open(inventory_db, "r+")
    else:
        open(inventory_db, "w")
        Mimisbrunnr_1.create_table_db1()
        Mimisbrunnr_2.create_table_db2()

    app = QApplication(sys.argv)
    if platform.system() == "Windows":
        app.setStyleSheet(qdarktheme.load_stylesheet())
    if QDialog.accepted:
        window = MainWindow()
        window.show()
        window.key = db_primary     # Default Mimisbrunnr to load
        window.load_data()
    # NEW
    win = mainWin()
    win.setWindowTitle("CSV Example")
    #win.show()
    # /NEW
    sys.exit(app.exec())
