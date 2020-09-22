import calendar
import logging

import pandas as pd

import date


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info({
	'action': 'util.py',
	'status': 'readed'
	})


class My_pandas_data(object):
	def __init__(self, datas=None, target_distance=None, today=None):
		self.datas = datas
		self.target_distance = target_distance
		self.df = None
		self.today = None


	def create_data_frame(self):
		df = pd.DataFrame(self.datas)
		df.columns = ['Date', 'Milage', 'Elevation']
		df = df.set_index('Date')
		df.index = pd.to_datetime(df.index)

		length = len(self.datas)

		# milage_dataを合計していく処理
		added_milage_data = []
		for i in range(length):
			if i == 0:
				added_milage_data.append(self.datas[i][1])
			else:
				self.datas[i][1] = self.datas[i][1] + self.datas[i-1][1]
				added_milage_data.append(self.datas[i][1])

		# elevation_dataを合計していく処理
		added_elevation_data = []
		for i in range(length):
			if i == 0:
				added_elevation_data.append(self.datas[i][2])
			else:
				self.datas[i][2] = self.datas[i][2] + self.datas[i-1][2]
				added_elevation_data.append(self.datas[i][2])

		#dfのカラムに追加
		df['Sum_milage'] = added_milage_data
		df['Sum_elevation'] = added_elevation_data

		# calendarモジュールで当該月の日数を取得し、日割りの目標値を取得する処理
		counts_in_month = calendar.monthrange(2020, 8)
		average_in_month = self.target_distance / counts_in_month[1]
		daily_target = round(average_in_month)

		daily_list = []
		for _ in range(length):
			daily_list.append(daily_target)

		added_daily_target_data = []
		for i in range(length):
			if i == 0:
				added_daily_target_data.append(daily_list[i])
			else:
				daily_list[i] = daily_list[i] + daily_list[i-1]
				added_daily_target_data.append(daily_list[i])

		#dfのカラムに追加
		df['Daily_target'] = daily_list
		df['Sum_target'] = added_daily_target_data

		df['Daily_diff'] = df['Milage'] - df['Daily_target']
		df['Sum_diff'] = df['Sum_milage'] - df['Sum_target']
		df['Target_diff'] = self.target_distance - df['Sum_milage']

		self.df = df

		return df


	def get_sum_diff(self):
		logger.info({
			'action': 'get_sum_diff',
			'self.df': self.df
			})
		result = self.df.iloc[-1]['Sum_diff']
		logger.info({
			'action': 'get_sum_diff',
			'result': result
			})

		return result


	def get_daily_diff(self, today):
		self.today = today
		logger.info({
			'action': 'get_daily_diff',
			'self.today': self.today
			})
		today_df = self.df.query('Date == @self.today')

		if not today_df.empty:
			result = today_df['Daily_diff']
			logger.info({
				'action': 'get_daily_diff',
				'today_df': today_df,
				'result': result
				})
			return result
		else:
			return 0



