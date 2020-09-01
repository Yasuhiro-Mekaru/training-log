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
		# logger.info({
		# 	'action': 'date.py',
		# 	'self.datas': self.datas
		# 	})

		date_format = '%Y-%m-%d %H:%M:%S'
		changed_date_format = '%Y-%m-%d'

		for data in self.datas:
			#datetimeのstrptimeメソッドで文字列の日付をdatetimeインスタンスに変更する
			datetime_instance = datetime.datetime.strptime(data[0], date_format)
			#datetimeインスタンスをdateインスタンスに変更する
			changed_to_date = datetime_instance.date()
			# #dateインスタンスをstrftimeメソッドで文字列に変換する
			# changed_to_str = changed_to_date.strftime(changed_date_format)
			#リストに代入
			data[0] = changed_to_date

		logger.info({
			'action': 'date.py',
			'changed_datas': self.datas,
			'change_data type': type(self.datas[0][0])
			})

		return self.datas


	def set_datas(self, datas):

		changed_datas = []
		datas_length = len(datas)

		logger.info({
			'action': 'date.py',
			'set_datas datas': datas,
			'datas_length': datas_length
			})

		for i in range(datas_length):
			changed_datas_length = len(changed_datas)
			logger.info({
				'action': 'date.py for first',
				'datas_length': datas_length,
				'changed_datas_length': changed_datas_length
				})
			if i == 0:
				changed_datas.append(datas[i])
				logger.info({
					'action': 'date.py',
					'for statement 1 if: changed_datas': changed_datas,
					'number i:': i
					})
					
			else:
				for j in range(changed_datas_length):
					if datas[i][0] != changed_datas[j][0]:
						changed_datas.append(datas[i])
						logger.info({
							'action': 'date.py',
							'for statement 2 if: changed_datas': changed_datas,
							'number i:': i,
							'number j:': j
							})
					else:
						milage = datas[i][1] + changed_datas[j][1]
						elevation = datas[i][2] + changed_datas[j][2]

						changed_datas[j][1] = milage
						changed_datas[j][2] = elevation
						logger.info({
							'action': 'date.py',
							'for statement 2 else: changed_datas': changed_datas,
							'number i:': i,
							'number j:': j
							})



		# for data in datas:
		# 	if len(changed_datas) == 0:
		# 		changed_datas.append(data)
		# 		logger.info({
		# 			'action': 'date.py',
		# 			'for statement 1 if: changed_datas': changed_datas
		# 			})
		# 	else:
		# 		for changed_data in changed_datas:
		# 			if data[0] != changed_data[0]:
		# 				changed_datas.append(data)
		# 				logger.info({
		# 					'action': 'date.py',
		# 					'for statement 2 if: changed_datas': changed_datas
		# 					})
						
		# 			else:
		# 				changed_data[1] = data[1] + changed_data[1]
		# 				changed_data[2] = data[2] + changed_data[2]

		# 				logger.info({
		# 					'action': 'date.py',
		# 					'for statement 2 else: changed_datas': changed_datas
		# 					})

		logger.info({
			'action': 'date.py',
			'changed_datas': changed_datas,
			'changed_datas type': type(changed_datas),
			'changed_datas len': len(changed_datas)
			})

		return changed_datas



		

		

