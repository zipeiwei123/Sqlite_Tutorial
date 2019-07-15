import pandas as pd
import sqlite3

#directory
database = "/Users/ironmanzpw/Desktop/sqlite/survey.db"
connection = sqlite3.connect(database)
cursor = connection.cursor()
#insert item using python
cursor.execute('INSERT INTO stores VALUES(?, ?, ?)', (5,4,'lamer'))
connection.commit()

#import database into pandas dataframe
df = pd.read_sql_query("select * from stores", connection)
print(df)