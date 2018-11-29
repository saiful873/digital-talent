import pymysql
import pandas
from sqlalchemy import create_engine

host = 'localhost'
port = '3306'
username = 'root'
password = ''
database = 'classicmodels'

#create connection to database

engine = create_engine('mysql+pymysql://'+username+':'+password+'@'+host+':'+port+'/'+database)'''engine = create_engine('mysql+pymysql://root: @localhost:3306/academic')'''

def run(sql):
	df = pd.read_sql_query(sql, engine)
	return df