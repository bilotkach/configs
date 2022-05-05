import resourses as res
import values as v
import sys
import pandas as pd
import matplotlib.pyplot as plt
import dbres as db

# Test
"""
boss = pd.read_csv('out.csv', index_col = 0)
for i in boss.index:
    print(boss.loc[i])
"""



# Get data abouts bosses
bosses = pd.DataFrame()
for boss_url in res.get_bosses_urls():
    bosses = pd.concat([bosses, res.get_boss_data(f'{v.url}{boss_url}')])


# Create conn with server, create db and table
conn = db.create_connection('localhost', 'py', 'pass')
db.execute_query(conn, v.create_db)
db.execute_query(conn, 'USE hollow_knight')
db.execute_query(conn, v.create_table)

# Create insert query with data we got earlier
insert_data = """
INSERT INTO
    bosses(name, hp_nail_lvl0, hp_nail_lvl1, hp_nail_lvl2, hp_nail_lvl3, hp_nail_lvl4)
VALUES """
for name in bosses.index:
   insert_data += f'\n(\'{name}\''
   for val in bosses.loc[name].values:
       insert_data += f',{val}'
   insert_data += '),'
insert_data = insert_data[:-1] + ';'

# Insert data to db
db.execute_query(conn, insert_data)


# bosses.to_csv('out.csv')
# print(bosses)
