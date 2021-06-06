from mongodb_connection import my_collection
from mysql_connection import connection, billionaires_table, engine
import sqlalchemy as mysql_db
import pandas as pd

# df = pd.DataFrame(list(my_collection.find()))

# Filter => Persons who has NetWorth bigger than 100 billions
df = pd.DataFrame(list(my_collection.find({'NetWorth' : {'$gt': 100}})))

# Converting the column data types for mysql
df = df.convert_dtypes()
df = df.astype({"NetWorth": 'float'})

# Drop _id column
df = df.drop('_id', 1)

# First way => Use existing table to insert data with sqlalchemy
query = df.to_dict(orient='records')
connection.execute(billionaires_table.insert(), query)

# => Example for one row     
# query = billionaires_table.insert().values(['Elon Musk', 151.0,
#        'United States', 'Tesla, SpaceX', 2, 49, 'Austin, Texas',
#        'Bachelor of Arts/Science, University of Pennsylvania', True])
# connection.execute(query)

# Second way => Creates table from dataframe and adds values, without id
df.to_sql(name="billionaires", con=engine, if_exists='replace', index=False,
            dtype={'Name':  mysql_db.types.VARCHAR(length=100),
                   'NetWorth': mysql_db.types.Float(precision=3, asdecimal=True),
                   'Country': mysql_db.types.VARCHAR(length=100),
                   'Source': mysql_db.types.VARCHAR(length=255),
                   'Rank': mysql_db.types.INTEGER(),
                   'Age': mysql_db.types.INTEGER(),
                   'Residence': mysql_db.types.VARCHAR(length=255),
                   'Citizenship': mysql_db.types.VARCHAR(length=100),
                   'Status': mysql_db.types.VARCHAR(length=50),
                   'Children': mysql_db.types.INTEGER(),
                   'Education': mysql_db.types.VARCHAR(length=255),
                   'Self_made': mysql_db.types.Boolean})


# mongo to dataframe convert
# https://stackoverflow.com/questions/16249736/how-to-import-data-from-mongodb-to-pandas

# dataframe convert data types
# https://stackoverflow.com/questions/15891038/change-column-type-in-pandas

# dataframe column drop
# https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe

# dataframe to mysql
# https://www.opentechguides.com/how-to/article/pandas/195/pandas-to-mysql.html

# adding multiple rows from dataframe by sqlalchemy
# https://stackoverflow.com/questions/31997859/bulk-insert-a-pandas-dataframe-using-sqlalchemy