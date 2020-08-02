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

		logger.info({
	        'action': 'insert_data'
	        'self.date': self.date
	    })
	    
		# Insert するテーブルによって処理を分岐する
		if self.data['table'] == 'milage_log':
			# 引数のdataから各データを取り出す処理
			date = self.data['date']
			milage = self.data['milage']
			elevation = self.data['elevation']
			weather_id = self.data['weather_id']
			target_id = self.data['target_id']

			logger.info({
		        'action': 'insert_data: milage_log',
		        'date': date,
		        'milage': milage
	        })

			#MySQLにコネクトし Insert文を実行
			conn = mysql.connector.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATABASE, 
				ssl_disabled=True)
			cursor = conn.cursor()
			cursor.execute('Insert into milage_log(date, milage, elevation, weather_id, target_id) '
				'Values("{}", "{}", "{}", "{}", "{}")'.format(date, milage, elevation, weather_id, target_id))
			conn.commit()
			cursor.close()
			conn.close()

			logger.info({
		        'action': 'insert_data: milage_log',
		        'status': 'connection close'
	        })

			return 'Connected'


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
		        'status': 'connection close'
	        })

			return 'Connected'




