import sqlite3

conn = sqlite3.connect("C:\\Users\\jackhsu\\Documents\\Unisoon\\規格\\程式_python_測試\\datafile.db")
cursor = conn.cursor()

try:
    cursor.execute(
        """create table cash (transaction_id integer primary key, taiwanese_dollars integer, us_dollars real, note varchar(30), date_info date)""")
    cursor.execute(
        """create table stock (transaction_id integer primary key, stock_id varchar(10), stock_num integer, stock_price real, processing_fee integer, tax integer, date_info date)""")
    conn.commit()
except Exception as e:
    print(f"Err happen: {str(e)}")

'''
cursor.execute("delete from cash")
conn.commit()
cursor.execute("insert into cash(taiwanese_dollars, us_dollars, note, date_info) values(100, 21.01, \"test str\", \"2024/01/30\")")
cursor.execute("insert into cash(taiwanese_dollars, us_dollars, note, date_info) values(200, 91.01, \"test str2\", \"2024/012/30\")")
conn.commit()
cursor.execute("select * from cash")
rows = cursor.fetchall()
c = 0
for row in rows:
    c = c+1
    print(f"row{c}: {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
'''

conn.close()
