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

		date_changed_datas = []
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

		

