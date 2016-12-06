#!/usr/bin/python

"""Initialize SQLite database"""

import os
import sqlite3
import argparse

script_name = os.path.join(os.path.dirname(__file__), 'create-tables.sql')

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('database', help="SQLite database file")
args = parser.parse_args()

con = sqlite3.connect(args.database)
cur = con.cursor()

with open(script_name, 'r') as f:
    cur.executescript(f.read())

con.commit()
cur.close()
con.close()
