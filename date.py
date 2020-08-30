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
		logger.info({
			'action': 'date.py',
			'self.datas': self.datas
			})

		date_format = '%Y-%m-%d %H:%M:%S'
		changed_date_format = '%Y-%m-%d'

		for data in self.datas:
			datetime_instance = datetime.datetime.strptime(data[0], date_format)
			changed_to_date = datetime_instance.date()
			changed_to_str = changed_to_date.strftime(changed_date_format)
			data[0] = changed_to_str

		logger.info({
			'action': 'date.py',
			'changed_datas': self.datas,
			'change_data type': type(self.datas[0][0])
			})

		return self.datas


	def set_datas(self, datas):

		logger.info({
			'action': 'date.py',
			'datas': datas,
			'datas type': type(datas[0][0])
			})

		changed_datas = []
		i = 0
		for data in datas:
			if i == 0:
				changed_datas.append(data)
				i = i + 1
			else:
				for change_data in changed_datas:
					if data[0] == change_data[0]:
						change_data[1] = data[1] + change_data[1]
						change_data[2] = data[2] + change_data[2]
					else:
						changed_datas.append(data)

		logger.info({
			'action': 'date.py',
			'changed_datas': changed_datas,
			'changed_datas type': type(changed_datas)
			})

		return changed_datas



		

		

