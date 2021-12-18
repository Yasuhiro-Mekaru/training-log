import logging

from database import session
from model import *

import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


logger.info({
	'action': 'controller.py',
	'status': 'readed'
	})


def insert_user(datas):
	"""ユーザー新規登録の処理
	ユーザー情報を受け取りDBに登録する。
	Args:
		datas (ImmutableMultiDict): formから送られてきたデータ
	Returns:
		is_success: bool
	"""
	users = Users()
	users.user_name = datas.get('user_name')
	users.email_address = datas.get('email_address')
	# passwordはhash化してDBに格納する
	password = datas.get('user_password')
	hashed_password = utils.hash_password(password=password)
	users.user_password = hashed_password

	logger.info({
		'action': 'controller.py insert_user',
		'users.user_name': users.user_name,
		'users.user_password': users.user_password,
		'users.email_address': users.email_address,
		})

	is_success = True
	try:
		session.add(users)
		session.commit()
		is_success = True
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py insert_user',
			'Exception': e
			})
		is_success = False
	finally:
		session.close()

	return is_success


def get_user(login_datas):
	"""ログイン時ユーザー情報を取得する処理
	emailアドレスとパスワードを受け取りDB検索する。
	対象ユーザーのidとnameをリスト形式で返す
	Args:
		datas (ImmutableMultiDict): formから送られてきたデータ
	Returns:
		user_datas: List
	"""
	email_address = login_datas.get('email_address')
	# passwordはhash化してDB検索する
	password = login_datas.get('user_password')
	hashed_password = utils.hash_password(password=password)
	logger.info({
		'action': 'controller.py get_user',
		'email_address': email_address,
		'hashed_password': hashed_password
		})

	datas = []
	try:
		users = session.query(Users).filter(Users.email_address==email_address, Users.user_password==hashed_password).all()
		for user in users:
			data = {}
			data['user_id'] = user.user_id
			data['user_name'] = user.user_name
			datas.append(data)
		logger.info({
			'action': 'controller.py get_user',
			'datas': datas,
			'datas type': type(datas)
			})
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py get_user',
			'Exception': e
			})
	finally:
		session.close()

	return datas


def insert_item(datas):
	if datas['table_name'] == 'section':
		budget_section = Budget_section()
		budget_section.name = datas['data']
		pass


def select_item():
	master_tables = [Budget_category, Budget_classification, Budget_section, Budget_kind, Budget_group]
	master_tables_str = ['Budget_category', 'Budget_classification', 'Budget_section', 'Budget_kind', 'Budget_group']

	master_datas = {}
	master_datas[master_tables_str[0]] = select_category(database_name=master_tables[0])
	master_datas[master_tables_str[1]] = select_classification(database_name=master_tables[1])
	# master_datas[master_tables_str[2]] = select_section(database_name=master_tables[2])
	# master_datas[master_tables_str[3]] = select_kind(database_name=master_tables[3])
	# master_datas[master_tables_str[4]] = select_group(database_name=master_tables[4])

	return master_datas


def select_category(database_name):
	try:
		categories = session.query(database_name).all()
		datas = []
		for category in categories:
			data = {}
			data['category_id'] = category.category_id
			data['category_name'] = category.category_name
			datas.append(data)
		logger.info({
			'action': 'controller.py select_category',
			'datas': datas
			})
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py select_category',
			'Exception': e
			})
	finally:
		session.close()
	return datas


def select_classification(database_name):
	try:
		classifications = session.query(database_name).all()
		datas = []
		for classification in classifications:
			data = {}
			data['class_id'] = classification.class_id
			data['class_name'] = classification.class_name
			data['category_id'] = classification.category_id
			datas.append(data)
		logger.info({
			'action': 'controller.py select_classification',
			'datas': datas
			})
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py select_classification',
			'Exception': e
			})
	finally:
		session.close()
	return datas


def select_section(database_name):
	try:
		sections = session.query(database_name).all()
		datas = []
		for section in sections:
			data = {}
			data['section_id'] = section.section_id
			data['section_name'] = section.section_name
			data['class_id'] = section.class_id
			datas.append(data)
		logger.info({
			'action': 'controller.py select_section',
			'datas': datas
			})
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py select_section',
			'Exception': e
			})
	finally:
		session.close()
	return datas


def select_kind(database_name):
	try:
		kinds = session.query(database_name).all()
		datas = []
		for kind in kinds:
			data = {}
			data['kind_id'] = kind.kind_id
			data['kind_name'] = kind.kind_name
			datas.append(data)
		logger.info({
			'action': 'controller.py select_kind',
			'datas': datas
			})
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py select_kind',
			'Exception': e
			})
	finally:
		session.close()
	return datas


def select_group(database_name):
	try:
		groups = session.query(database_name).all()
		datas = []
		for group in groups:
			data = {}
			data['group_id'] = group.group_id
			data['group_name'] = group.group_name
			data['kind_id'] = group.kind_id
			datas.append(data)
		logger.info({
			'action': 'controller.py select_group',
			'datas': datas
			})
	except Exception as e:
		session.rollback()
		logger.info({
			'action': 'controller.py select_group',
			'Exception': e
			})
	finally:
		session.close()
	return datas


# def get_category():
# 	"""
# 	Args:
# 		None
# 	Return:
# 		List
# 	"""
# 	try:
# 		categories = session.query(Category).all()
# 		datas = []
# 		for category in categories:
# 			data = {}
# 			data['category_id'] = category.category_id
# 			data['category'] = category.category
# 			datas.append(data)
# 		logger.info({
# 				'action': 'controller.py',
# 				'datas': datas,
# 				'datas type': type(datas),
# 				'datas[0]': datas[0],
# 				'datas[0] type': type(datas[0])
# 			})
# 	finally:
# 		session.close()
# 	return datas


# def get_products(category_id):
# 	"""
# 	Args:
# 		category_id (int): カテゴリid
# 	Return:
# 		List
# 	"""
# 	try:
# 		products = session.query(Products.products_id, Products.title).filter(Products.category_id == category_id).all()
# 		datas = []
# 		for product in products:
# 			datas.append(product)
# 			logger.info({
# 				'action': 'controller.py',
# 				'datas': datas,
# 				'datas type': type(datas),
# 				'datas[0]': datas[0][0],
# 				'datas[0] type': type(datas[0][0])
# 			})
# 	finally:
# 		session.close()
# 	return datas


# def get_all_data(products_id):
# 	"""
# 	Args:
# 		products_id (int): 作品id
# 	Return:
# 		dict
# 	"""
# 	try:
# 		products_datas = session.query(Products).filter(Products.products_id==products_id).all()
# 		main_data = {}
# 		for products_data in products_datas:
# 			main_data['p_id'] = products_data.products_id
# 			main_data['p_title'] = products_data.title
# 			main_data['p_director'] = products_data.director
# 			main_data['p_overview'] = products_data.overview
# 			main_data['p_image_path'] = products_data.image_path
# 		# logger.info({
# 		# 		'action': 'controller.py',
# 		# 		'main_data': main_data
# 		# 	})
# 		rrl_datas = session.query(Real_life_location).filter(Real_life_location.products_id==products_id).all()
# 		real_life_location_datas = []
# 		for rrl_data in rrl_datas:
# 			data = {}
# 			data['r_name'] = rrl_data.name
# 			data['r_scene'] = rrl_data.scene
# 			data['r_overview'] = rrl_data.overview
# 			data['r_image_path'] = rrl_data.image_path
# 			data['r_latitude'] = rrl_data.latitude
# 			data['r_longitude'] = rrl_data.longitude
# 			data['r_id'] = rrl_data.real_life_location_id
# 			real_life_location_datas.append(data)
# 		# logger.info({
# 		# 		'action': 'controller.py',
# 		# 		'real_life_location_datas': real_life_location_datas
# 		# 	})
# 		main_data['real_life_location_data'] = real_life_location_datas
# 	finally:
# 		session.close()

# 	return main_data


# def get_latlng_data(real_life_location_id):
# 	"""
# 	Args:
# 		real_life_location_id (int): 聖地id
# 	Return:
# 		List
# 	"""
# 	try:
# 		datas = session.query(Real_life_location).\
# 		filter(Real_life_location.real_life_location_id==real_life_location_id).all()
# 		real_life_location_data = {}
# 		real_life_location_data['name'] = datas[0].name
# 		real_life_location_data['scene'] = datas[0].scene
# 		real_life_location_data['overview'] = datas[0].overview
# 		real_life_location_data['image_path'] = datas[0].image_path
# 		real_life_location_data['latitude'] = float(datas[0].latitude)
# 		real_life_location_data['longitude'] = float(datas[0].longitude)
# 		logger.info({
# 				'action': 'controller.py',
# 				'real_life_location_data': real_life_location_data,
# 				'real_life_location_data type': type(real_life_location_data)
# 			})
# 		real_life_location_datas = []
# 		real_life_location_datas.append(real_life_location_data)
# 	finally:
# 		session.close()
# 	return real_life_location_datas


# def get_all_latlng_datas(products_id):
# 	"""
# 	Args:
# 		products_id (int): 作品id
# 	Return:
# 		List
# 	"""
# 	try:
# 		rrl_datas = session.query(Real_life_location).filter(products_id==products_id).all()
# 		real_life_location_datas = []
# 		for rrl_data in rrl_datas:
# 			data = {}
# 			data['name'] = rrl_data.name
# 			data['scene'] = rrl_data.scene
# 			data['overview'] = rrl_data.overview
# 			data['image_path'] = rrl_data.image_path
# 			data['latitude'] = float(rrl_data.latitude)
# 			data['longitude'] = float(rrl_data.longitude)
# 			real_life_location_datas.append(data)
# 		logger.info({
# 				'action': 'controller.py',
# 				'real_life_location_datas': real_life_location_datas,
# 				'real_life_location_datas type': type(real_life_location_datas)
# 			})
# 	finally:
# 		session.close()
# 	return real_life_location_datas



# # 動作テスト用
# def get_user():
# 	datas = []
# 	try:
# 		users = session.query(Users).all()
# 		for user in users:
# 			data = {}
# 			data['user_id'] = user.user_id
# 			data['user_name'] = user.user_name
# 			data['email_address'] = user.email_address
# 			data['user_password'] = user.user_password
# 			datas.append(data)
# 		logger.info({
# 			'action': 'controller.py get_user',
# 			'datas': datas,
# 			'datas type': type(datas)
# 			})
# 	except Exception as e:
# 		session.rollback()
# 		logger.info({
# 			'action': 'controller.py get_user',
# 			'Exception': e
# 			})
# 	finally:
# 		session.close()

# 	return datas

if __name__ == '__main__':
	pass
	# datas = {
	# 	'user_name': 'yasuhiro M',
	# 	'email_address': 'taijyu@gmail.com',
	# 	'user_password': '0123456789'
	# }

	# insert_user(datas)

	# users = get_user()
	# user = users[0]
	# logger.info({
	# 	'action': 'controller.py main',
	# 	'users': users,
	# 	'user': user,
	# 	'user_name': user['user_name']
	# 	})

	# insert_real_life_location(datas)

	# r = get_all_latlng_datas(1)
	# get_latlng_data(1)



