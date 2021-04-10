from dao import database


def select_from_table(table):
	if table == 'category':
		query_str = 'SELECT * from "{table}"'
		kwags = {
			'table': table
		}

		# Account_categoryインスタンスを生成
		category_table = database.Category_table(table=table)
		category_datas = category_table.exec_select(query_str=query_str, kwags=kwags)
		print('controller select_from_table category_datas: ', category_datas)
		print(category_datas)