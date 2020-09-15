import logging

import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info({
	'action': 'date.py',
	'status': 'readed'
	})


class My_date(object):
	"""docstring for My_date"""
	def __init__(self, datas=None, today=None):
		self.datas = datas
		self.today = today


	def today_date(self):
		# datetime で今日の日付け情報をdateオブジェクトとして取得
		today = datetime.date.today()
		self.today = today
		# dateオブジェクトを文字列に変更
		date_format = '%Y-%m-%d'
		changed_to_str = today.strftime(date_format)

		logger.info({
			'action': 'date.py today_date',
			'changed_to_str': changed_to_str,
			'changed_to_str type': type(changed_to_str)
			})
		return changed_to_str



	def change_to_date(self):

		date_format = '%Y-%m-%d'
		# date_format = '%Y-%m-%d %H:%M:%S'
		changed_date_format = '%Y-%m-%d'

		for data in self.datas:
			#datetimeのstrptimeメソッドで文字列の日付をdatetimeインスタンスに変更する
			datetime_instance = datetime.datetime.strptime(data[0], date_format)
			#datetimeインスタンスをdateインスタンスに変更する
			changed_to_date = datetime_instance.date()
			# #dateインスタンスをstrftimeメソッドで文字列に変換する
			changed_to_str = changed_to_date.strftime(changed_date_format)
			#リストに代入
			data[0] = changed_to_str

		logger.info({
			'action': 'date.py change_to_date',
			'changed_datas': self.datas,
			'change_data type': type(self.datas[0][0])
			})

		return self.datas


	def get_first_day(self):
		logger.info({
			'action': 'date.py get_first_day',
			'self.today': self.today,
			'self.today type': type(self.today)
			})
		return self.today.replace(day=1)


	

		


		


		

		

