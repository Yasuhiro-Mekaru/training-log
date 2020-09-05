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
	def __init__(self, datas):
		self.datas = datas


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
			data[0] = changed_to_date

		logger.info({
			'action': 'date.py change_to_date',
			'changed_datas': self.datas,
			'change_data type': type(self.datas[0][0])
			})

		return self.datas


	def compare_date(self):
		logger.info({
			'action': 'date.py compare_date',
			'self.datas': self.datas,
			'self. type': type(self.datas[0][0])
			})

		result1 = self.datas[0][0] == self.datas[1][0]
		result2 = self.datas[1][0] == self.datas[2][0]
		result3 = self.datas[2][0] == self.datas[3][0]
		result4 = self.datas[3][0] == self.datas[4][0]
		result5 = self.datas[4][0] == self.datas[5][0]

		logger.info({
			'action': 'date.py compare_date',
			'result1': result1,
			'result2': result2,
			'result3': result3,
			'result4': result4,
			'result5': result5
			})

		return (result1, result2, result3, result4, result5)


	def set_datas(self):
		new_lists = []
		lists = []
		for data in self.datas:
			if not new_lists:
				lists.append(data)
				new_lists.append(lists)
			else:
				for new_list in new_lists:
					for l in new_list:
						if data[0] == l[0]:
							lists.append(data)
						else:
							lists = []
							lists.append(data)
							new_lists.append(lists)
		logger.info({
			'action': 'date.py set_datas',
			'new_lists': new_lists 
			})


		


		


		

		

