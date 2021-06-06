from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, Float,MetaData

engine = create_engine('mysql+mysqldb://root:admin@localhost:3306/santsg_mysql_db')

connection = engine.connect()
meta = MetaData()

billionaires_table = Table(
  'forbes-billionaires', meta,
  Column('id', Integer, primary_key= True, autoincrement= True),
  Column('Name', String(100)),
  Column('NetWorth', Float),
  Column('Country', String(100)),
  Column('Source', String(255)),
  Column('Rank', Integer),
  Column('Age', Integer),
  Column('Residence', String(255)),
  Column('Citizenship', String(100)),
  Column('Status', String(50)),
  Column('Children', Integer),
  Column('Education', String(255)),
  Column('Self_made', Boolean)
)

meta.create_all(engine)

# import mysql.connector

# my_sql_db = mysql.connector.connect(
#   host="localhost",
#   port= "3306",
#   user="root",
#   password="admin",
#   database= "santsg_mysql_db"
# )

# my_cursor = my_sql_db.cursor()
# my_cursor.execute("CREATE DATABASE santsg_mysql_db")


# initialize mysql server problem
# https://stackoverflow.com/questions/33752407/mysqld-cant-change-dir-to-data-server-doesnt-start

# how to connect sqlalchemy to mysql
# https://docs.sqlalchemy.org/en/14/core/engines.html#mysql

# sqlalchemy query examples
# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91

# create Table with sqlalchemy
# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm
# https://stackoverflow.com/questions/19284012/python-sqlalchemy-query-attributeerror-connection-object-has-no-attribute-c