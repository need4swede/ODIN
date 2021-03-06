# #################################################################
# File name:    Mimisbrunnr_1.py
# Author:       Need4Swede
# Description:  Mimir's Database File for ODIN
# #################################################################
import sqlite3, os, sys
from sqlite3 import Error
from sqlite3.dbapi2 import Date
import pandas as pd
## DIRECTORY ######################################################
root_dir = os.path.dirname(os.path.abspath(__file__))
path_parent = os.path.dirname(os.getcwd())
mimir_dir = (path_parent + "/ODIN/Mimir")
if not os.path.isdir(mimir_dir):
    os.makedirs(mimir_dir)
inventory_db = mimir_dir + "/Mimir.db"
csv_name = '/Mimisbrunnr_1.csv'
## INPUT LABELS ###################################################
lb_id = "ID #"
lb_1 = "Site:"
lb_2 = "Location:"
lb_3 = "Product:"
lb_4 = "Make:"
lb_5 = "Asset_Tag:"
lb_6 = "Reference:"
lb_7b = "Buyer:"
lb_7s = "Assigned:"
lb_8 = "Status:"
lb_9 = "Link/Date:"
###################################################################

def create_table_db1():
    # Connect to a Mimisbrunnr
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    # Create a table
    c.execute("""CREATE TABLE IF NOT EXISTS Mimisbrunnr_1 (
                                Site text,
                                Location text,
                                Product text,
                                Make text,
                                Asset_Tag text,
                                Reference text,
                                Assigned text,
                                Status text,
                                Date text,
                                Info text     
                )""")
    # Commit command
    conn.commit()
    # Close connection
    conn.close()


def add_row(Site="", Location="", Product="", Make="", Asset_Tag="", Reference="", Assigned="", Status="", Date="", Info=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    c.execute("INSERT INTO Mimisbrunnr_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (Site, Location, Product, Make, Asset_Tag, Reference, Assigned, Status, Date, Info))
    conn.commit()
    conn.close()


def add_rows(information):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    c.executemany(
        "INSERT INTO Mimisbrunnr_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", information)
    conn.commit()
    conn.close()


def search_row(id=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    if not id:
        id = "some words"
    try:
        c.execute("SELECT rowid, * from Mimisbrunnr_1 WHERE rowid=?", (id,))
    except Error as e:
        print(e)
    row = c.fetchone()
    conn.commit()
    conn.close()
    return row


def search_rows(Site="", Location="", Product="", Make="", Asset_Tag="", Reference="", Assigned="", Status="", Date="", Info=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()

    if not Site:
        Site = "some words"
    if not Location:
        Location = "some words"
    if not Product:
        Product = "some words"
    if not Make:
        Make = "some words"
    if not Reference:
        Reference = "some words"
    if not Asset_Tag:
        Asset_Tag = "some words"
    if not Status:
        Status = "some words"
    if not Assigned:
        Assigned = "some words"
    if not Date:
        Date = "some words"
    if not Info:
        Info = "some words"

    try:
        c.execute("""SELECT rowid, * FROM Mimisbrunnr_1 WHERE 
                    Site=? OR Location=? OR Product=? OR
                    Make=? OR Asset_Tag=? OR Reference=? OR Assigned=? OR
                    Status=? OR Date=? OR Info=?""",
                  (Site, Location, Product, Make, Asset_Tag, Reference, Assigned, Status, Date, Info))
        rows = c.fetchall()
        # for row in rows:
        #     print(row)
        conn.commit()
        conn.close()
        return rows

    except Error as e:
        print(e)
    conn.commit()
    conn.close()


def delete_row(id=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    if not id:
        id = "some words"
    c.execute("DELETE FROM Mimisbrunnr_1 WHERE rowid=?", (id,))
    conn.commit()
    conn.close()


def update_row(id="", Site="", Location="", Product="", Make="", Asset_Tag="", Reference="", Assigned="", Status="", Date="", Info=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    c.execute("""UPDATE Mimisbrunnr_1 SET Site=?, Location=?, Product=?, Make=?, Asset_Tag=?, Reference=?, Assigned=?, Status=?, Date=?, Info=? WHERE rowid=?""",
              (Site, Location, Product, Make, Asset_Tag, Reference, Assigned, Status, Date, Info, int(id)))
    conn.commit()
    conn.close()


def show_table():
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    # if name == "Mimisbrunnr_1":
    c.execute("SELECT rowid, * FROM Mimisbrunnr_1")
    # elif name == "Mimisbrunnr_1":
    # c.execute("SELECT rowid, * FROM Mimisbrunnr_1")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()
    conn.commit()
    conn.close()
    return rows


def to_csv():
    export_dir = (root_dir + "/exports")
    conn = sqlite3.connect(inventory_db, detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM Mimisbrunnr_1", conn)
    sorted_df = db_df.sort_values(by=["Product"], ascending=True)
    if not os.path.isdir(export_dir):
        os.makedirs(export_dir)
    if not os.path.isdir(export_dir + "/CSV"):
        os.makedirs(export_dir + "/CSV")
    if not os.path.isdir(export_dir + "/HTML"):
        os.makedirs(export_dir + "/HTML")
    if not os.path.isdir(export_dir + "/PDF"):
        os.makedirs(export_dir + "/PDF")
    sorted_df.to_csv(export_dir + "/CSV/" + csv_name, index=False)


def main():
    pass


if __name__ == "__main__":
    main()