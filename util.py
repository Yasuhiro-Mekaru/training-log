import logging

import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info({
	'action': 'util.py',
	'status': 'readed'
	})


class My_pandas_data(object):
	def __init__(self, datas):
		self.datas = datas


	def create_data_frame(self):
		df = pd.DataFrame(self.datas)
		df.columns = ['Date', 'Milage', 'Elevation']
		df = df.set_index('Date')
		df.index = df.to_datetime(df.index)

		return df