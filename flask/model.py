import logging
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base
from database import ENGINE


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info({
	'action': 'model.py',
	'status': 'readed'
	})


class Users(Base):
	"""
	user master table for budget.
	To register user information.
	"""
	__tablename__ = 'users'
	user_id = Column('user_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	user_name = Column('user_name', String(20), nullable=False,)
	email_address = Column('email_address', String(64), nullable=False,)
	user_password = Column('user_password', String(128), nullable=False,)


class Budget_category(Base):
	"""
	category master table for budget.
	To categorise income or outcome.
	"""
	__tablename__ = 'budget_category'
	category_id = Column('category_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	category_name = Column('category_name', String(30), nullable=False, unique=True)
	classifications = relationship('Budget_classification', back_populates='category')


class Budget_classification(Base):
	"""
	classification master table for budget.
	To categorise fixed cost or variable cost.
	"""
	__tablename__ = 'budget_classification'
	class_id = Column('class_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	class_name = Column('class_name', String(30), nullable=False, unique=True)
	category_id = Column('category_id', Integer, ForeignKey(Budget_category.category_id))
	category = relationship('Budget_category', back_populates='classifications')
	sections = relationship('Budget_section', back_populates='classification')


class Budget_section(Base):
	"""
	section master table for budget.
	To categorise bills. for example food, grocery, medical, leisure...
	"""
	__tablename__ = 'budget_section'
	section_id = Column('section_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	section_name = Column('section_name', String(30), nullable=False, unique=True)
	class_id = Column('class_id', Integer, ForeignKey(Budget_classification.class_id))
	classification = relationship('Budget_classification', back_populates='sections')


class Budget_kind(Base):
	"""
	kind master table for budget.
	To categorise kind of the item.
	"""
	__tablename__ = 'budget_kind'
	kind_id = Column('kind_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	kind_name = Column('kind_name', String(30), nullable=False, unique=True)
	groups = relationship('Budget_group', back_populates='kind')


class Budget_group(Base):
	"""
	Group master table for budget.
	To categorise the group of the item.
	"""
	__tablename__ = 'budget_group'
	group_id = Column('group_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	group_name = Column('group_name', String(30), nullable=False, unique=True)
	kind_id = Column('kind_id', ForeignKey(Budget_kind.kind_id))
	kind = relationship('Budget_kind', back_populates='groups')


class Budget_currency(Base):
	"""
	Currency master table for budget.
	To categorise the using currency.
	"""
	__tablename__ = 'budget_currency'
	currency_id = Column('currency_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	currency_code = Column('currency_code', String(10), nullable=False, unique=True)


class Budget_essential(Base):
	"""
	Currency master table for budget.
	To categorise the using currency.
	"""
	__tablename__ = 'budget_essential'
	essential_id = Column('essential_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	essential_value = Column('essential_value', String(30), nullable=False, unique=True)
 

class Budget_monthly_result(Base):
	"""
	Monthly budget result transaction table for budget.
	To register the logs of total results.
	"""
	__tablename__ = 'budget_monthly_result'
	result_id = Column('result_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	amount = Column('amount', Integer, nullable=False)
	date = Column('date', String(10), nullable=False)
	category_id = Column('category_id', Integer, nullable=False)
	class_id = Column('class_id', Integer, nullable=False)
	section_id = Column('section_id', Integer, nullable=False)
	essential_id = Column('essential_id', Integer, nullable=False)


class Budget_monthly_plan(Base):
	"""
	Monthly budget plan transaction table for budget.
	To register the logs of total results.
	"""
	__tablename__ = 'budget_monthly_plan'
	plan_id = Column('plan_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	amount = Column('amount', Integer, nullable=False)
	date = Column('date', String(10), nullable=False)
	category_id = Column('category_id', Integer, nullable=False)
	class_id = Column('class_id', Integer, nullable=False)
	section_id = Column('section_id', Integer, nullable=False)
	essential_id = Column('essential_id', Integer, nullable=False)


class Budget_payment(Base):
	"""
	Monthly budget plan transaction table for budget.
	To register the logs of total results.
	"""
	__tablename__ = 'budget_payment'
	payment_id = Column('payment_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	item_name = Column('item_name', String(30), nullable=True)
	amount = Column('amount', Integer, nullable=False)
	date = Column('date', String(10), nullable=False)
	category_id = Column('category_id', Integer, nullable=False)
	class_id = Column('class_id', Integer, nullable=False)
	section_id = Column('section_id', Integer, nullable=False)
	kind_id = Column('kind_id', Integer, nullable=False)
	group_id = Column('group_id', Integer, nullable=False)
	currency_id = Column('currency_id', Integer, nullable=False)
	essential_id = Column('essential_id', Integer, nullable=False)



# class Real_life_location(Base):
# 	"""docstring for Real_life_location"""
# 	__tablename__ = 'real_life_location'
# 	real_life_location_id = Column('real_life_location_id', Integer, nullable=False, primary_key=True)
# 	name = Column('name', String(20), nullable=False,)
# 	scene = Column('scene', String(50), nullable=False,)
# 	overview = Column('overview', String(200), nullable=False,)
# 	image_path = Column('image_path', String(50))
# 	latitude = Column('latitude', String(15), nullable=False)
# 	longitude = Column('longitude', String(15), nullable=False)
# 	products_id = Column('products_id', Integer, nullable=False,)
		

def main():
	Base.metadata.create_all(bind=ENGINE)



if __name__ == '__main__':
	logger.info({
		'action': 'model.py main',
		'status': 'model.py main is called' 
		})
	main()
	
	# # Usersテーブルを削除する
	# Users.__table__.drop(ENGINE)