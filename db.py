import logging

import mysql.connector


DB_HOST = 'us-cdbr-east-02.cleardb.com'
DB_USERNAME = 'b57547af749fe1'
DB_PASSWORD = '74315ba5'
DB_DATABASE = 'heroku_d2e365081e3ffbe'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class My_log_database(object):

	def __init__(self, data):
		self.data = data



	def insert_data(self):
		# Insert するテーブルによって処理を分岐する
		if self.data['table'] == 'milage_log':
			# 引数のdataから各データを取り出す処理
			table = self.data['table']
			date = self.data['date']
			milage = self.data['milage']
			elevation = self.data['elevation']
			weather_id = self.data['weather_id']
			target_id = self.data['target_id']

			logger.info({
		        'action': 'insert_data: milage_log',
		        'table': table,
		        'date': date,
		        'milage': milage,
		        'elevation': elevation,
		        'weather_id': weather_id,
		        'target_id': target_id
	        })

			#MySQLにコネクトし Insert文を実行
			conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
				ssl_disabled=True)
			cursor = conn.cursor()
			cursor.execute('Insert into milage_log(date, milage, elevation, weather_id, target_id) '
				'Values("{date}", "{milage}", "{elevation}", "{weather_id}", "{target_id}")'.format(
					date=date, milage=milage, elevation=elevation, weather_id=weather_id, target_id=target_id))
			logger.info({
				'action': 'insert_data: milage_log',
				'cursor': cursor
				})
			conn.commit()
			cursor.close()
			conn.close()

			logger.info({
		        'action': 'insert_data: milage_log',
		        'status': 'connection closed'
	        })


		elif self.data['table'] == 'weather':
			content = self.data['content']

			logger.info({
		        'action': 'insert_data: weather',
		        'content': content
	        })

	        #MySQLにコネクトし Insert文を実行
			conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
				ssl_disabled=True)
			cursor = conn.cursor()
			cursor.execute('Insert into weather(content) Values("{}")'.format(content))
			conn.commit()
			cursor.close()
			conn.close()

			logger.info({
		        'action': 'insert_data: weather',
		        'status': 'connection closed'
	        })

		elif self.data['table'] == 'target_distance':
			month = self.data['month']
			monthly_value = self.data['monthly_value']
			dayly_value = self.data['dayly_value']
			logger.info({
		        'action': 'insert_data: target_distance',
		        'month': month,
		        'monthly_value': monthly_value
	        })
	        #MySQLにコネクトし Insert文を実行
			conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
				ssl_disabled=True)
			cursor = conn.cursor()
			cursor.execute('INSERT INTO target_distance(month, monthly_value, dayly_value) '
				'VALUES("{}", "{}", "{}")'.format(month, monthly_value, dayly_value))
			conn.commit()
			cursor.close()
			conn.close()

		return 'Success'



	def delete_data(self):

		if self.data['table'] == 'milage_log':
			table = self.data['table']
			key = self.data['key']
			value = self.data['value']
			logger.info({
				'action': 'delete_data: milage_log',
				'key': key,
				'value': value
				})
			# MySQL にコネクトし Delete文を実行
			conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
				ssl_disabled=True)
			cursor = conn.cursor()
			cursor.execute('DELETE from {table} where {key}={value}'.format(table=table, key=key, value=value))
			conn.commit()
			cursor.close()
			conn.close()
			logger.info({
				'action': 'delete_data: milage_log',
				'status': 'connection closed'
				})

		elif self.data['table'] == 'target_distance':
			table = self.data['table']
			key = self.data['key']
			value = self.data['value']
			logger.info({
				'action': 'delete_data: target_distance',
				'key': key,
				'value': value
				})
			# MySQL にコネクトし Delete文を実行
			conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
				ssl_disabled=True)
			cursor = conn.cursor()
			cursor.execute('DELETE from {table} where {key}={value}'.format(table=table, key=key, value=value))
			conn.commit()
			cursor.close()
			conn.close()
			logger.info({
				'action': 'delete_data: target_distance',
				'status': 'connection closed'
				})

		elif self.data['table'] == 'weather':
			pass




