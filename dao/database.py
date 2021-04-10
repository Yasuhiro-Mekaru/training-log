""" Databaseクラスを記述するモジュール """

import mysql.connector

DB_HOST = 'us-cdbr-east-02.cleardb.com'
DB_USERNAME = 'b57547af749fe1'
DB_PASSWORD = '74315ba5'
DB_DATABASE = 'heroku_d2e365081e3ffbe'
DB_PORT = 3306


class Database(object):
	""" 各Tableクラスの親クラス """
	def __init__(self, table=None):
		self.database = DB_DATABASE
		self.host = DB_HOST
		self.port = DB_PORT
		self.user = DB_USERNAME
		self.password = DB_PASSWORD,
		self.ssl_disabled = True
		self.kwargs = {
			'host': self.host,
			# 'port': self.port,
			'database': self.database,
			'user': self.user,
			'password': self.password,
			'ssl_disabled': self.ssl_disabled
		}
		self.table = table


	def exec_select(self, query_str, kwags):
		print('database.py exec_select is celled')
		conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
								ssl_disabled=True)
		cursor = conn.cursor()
		datas = []
		cursor.execute(query_str.format(**kwags))
		for row in cursor:
			datas.append(row)
		conn.commit()
		cursor.close()
		conn.close()
		return datas


	def exec_insert(self, query_str, kwags):
		conn = mysql.connector.connect(**self.kwargs)
		cursor = conn.cursor()
		cursor.execute(query_str.format(**kwags))
		conn.commit()
		cursor.close()
		conn.close()


class Category_table(Database):
	""" account_categoryテーブルのクラス """
	def __init__(self, table):
		super().__init__()
		self.table = table
		
















