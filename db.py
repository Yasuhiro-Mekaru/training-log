import os

import mysql.connector


DB_HOST = 'us-cdbr-east-02.cleardb.com'
DB_USERNAME = 'b57547af749fe1'
DB_PASSWORD = '74315ba5'
DB_DATABASE = 'heroku_d2e365081e3ffbe'

SSL_CA = '/app/cleardb-ca.pem'
SSL_CERT = '/app/cert.pem'
SSL_KEY = '/app/unlock-key.pem'


class My_log_database(object):

	def insert_data(self):
		# conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
		# 	ssl_ca=SSL_CA, ssl_cert=SSL_CERT, ssl_key=SSL_KEY, ssl_verify_cert=True)
		conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
			ssl_disabled=True)
		# re = conn.is_connected()
		# cursor = conn.cursor()
		# # cursor.execute('INSERT INTO test values(2, 200)')

		# cursor.execute('CREATE TABLE milage_log('
  #              'id int NOT NULL AUTO_INCREMENT,'
  #              'date datetime NOT NULL,'
  #              'milage int NOT NULL,'
  #              'elevation int NOT NULL,'
  #              'weather_id int NOT NULL,'
  #              'target_id int NOT NULL,'
  #              'PRIMARY KEY(id))'
  #              )

		# conn.commit()
		# cursor.close()
		conn.close()

		return 'Connected'


