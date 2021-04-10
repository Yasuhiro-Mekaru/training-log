import logging

from dao import database

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def select_from_table(table):
	if table == 'account_category':
		query_str = 'SELECT * from {table}'.format(table)
		logger.info({
			'action': 'controller.py select_from_table category',
			'query_str': query_str,
			'query_str type': type(query_str)
			})
		# kwags = {
		# 	'table': table
		# }

		# Account_categoryインスタンスを生成
		category_table = database.Category_table(table=table)
		category_datas = category_table.exec_select(query_str=query_str)
		logger.info({
			'action': 'controller.py select_from_table category',
			'category_datas': category_datas,
			'category_datas type': type(category_datas)
			})