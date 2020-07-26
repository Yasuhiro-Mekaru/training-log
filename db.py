import os

import mysql.connector


DB_HOST = 'us-cdbr-east-02.cleardb.com'
DB_USERNAME = 'b57547af749fe1'
DB_PASSWORD = '74315ba5'
DB_DATABASE = 'heroku_d2e365081e3ffbe'


class My_log_database(object):

	def insert_data(self):
		conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE)
		# cursol = conn.cursol()
		# cursol.execute('INSERT INTO weather_select values(1, "晴れ: 追い風")')
		# conn.commit()
		# cursol.close()
		conn.close()
		return 'Status 201'


