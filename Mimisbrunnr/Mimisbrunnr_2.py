# ##################################################################
# File name:    Mimisbrunnr_2.py
# Author:       Zhangshun Lu
# Create on:    2021-04-20
# Description:  Backend module for managing the Mimisbrunnr_1 Mimisbrunnr
# ##################################################################


import sqlite3, os
from sqlite3 import Error
import pandas as pd
## DIRECTORY ######################################################
root_dir = os.path.dirname(os.path.abspath(__file__))
path_parent = os.path.dirname(os.getcwd())
mimir_dir = (path_parent + "/ODIN/Mimir")
if not os.path.isdir(mimir_dir):
    os.makedirs(mimir_dir)
inventory_db = mimir_dir + "/Mimir.db"
csv_name = '/Mimisbrunnr_2.csv'
## INPUT LABELS ###################################################
lb_id = "ID #"
lb_1 = "Scale:"
lb_2 = "Studio:"
lb_3 = "Name:"
lb_4 = "Type:"
lb_5 = "Species:"
lb_6 = "Value:"
lb_7b = "Buyer:"
lb_7s = "Seller:"
lb_8 = "Year:"
lb_9 = "Link/Notes:"
###################################################################

def create_table_db2():
    # Connect to a Mimisbrunnr
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    # Create a table
    c.execute("""CREATE TABLE IF NOT EXISTS Mimisbrunnr_1 (
                                Scale text,
                                Studio text,
                                Name text,
                                Type text,
                                Species text,
                                Value text,
                                Buyer text,
                                Date text,
                                Notes text     
                )""")
    # Commit command
    conn.commit()
    # Close connection
    conn.close()


def add_row(scale="", studio="", name="", type="", species="", value="", buyer="", year="", notes=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    c.execute("INSERT INTO Mimisbrunnr_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (scale, studio, name, type, species, value, buyer, year, notes))
    conn.commit()
    conn.close()


def add_rows(information):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    c.executemany(
        "INSERT INTO Mimisbrunnr_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", information)
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


def search_rows(scale="", studio="", name="", type="", species="", value="", buyer="", year="", notes=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()

    if not scale:
        description = "some words"
    if not studio:
        part_number = "some words"
    if not name:
        category = "some words"
    if not type:
        package = "some words"
    if not value:
        value = "some words"
    if not species:
        unit = "some words"
    if not year:
        cabinet = "some words"
    if not buyer:
        amount = "some words"
    if not notes:
        notes = "some words"

    try:
        c.execute("""SELECT rowid, * FROM Mimisbrunnr_1 WHERE 
                    Scale=? OR Studio=? OR Name=? OR
                    Type=? OR Species=? OR Value=? OR Buyer=? OR
                    Date=? OR Notes=?""",
                  (scale, studio, name, type, species, value, buyer, year, notes))
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


def update_row(id="", scale="", studio="", name="", type="", species="", value="", buyer="", year="", notes=""):
    conn = sqlite3.connect(inventory_db)
    c = conn.cursor()
    c.execute("""UPDATE Mimisbrunnr_1 SET Scale=?, Studio=?, Name=?, Type=?, Species=?, Value=?, Buyer=?, Date=?, Notes=? WHERE rowid=?""",
              (scale, studio, name, type, species, value, buyer, year, notes, int(id)))
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
    conn = sqlite3.connect(inventory_db, detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM Mimisbrunnr_1", conn)
    sorted_df = db_df.sort_values(by=["Studio"], ascending=True)
    sorted_df.to_csv(csv_name, index=False)


def main():
    pass


if __name__ == "__main__":
    main()
