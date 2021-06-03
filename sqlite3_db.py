import csv, sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute("CREATE TABLE bulk (Date, Symbol);") # use your column names here

with open('bulk.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Date'], i['Symbol']) for i in dr]

cur.executemany("INSERT INTO bulk (Date, Symbol) VALUES (?, ?);", to_db)
conn.commit()
conn.close()
