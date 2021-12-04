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
	"""docstring for Users"""
	__tablename__ = 'users'
	user_id = Column('user_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	user_name = Column('user_name', String(20), nullable=False,)
	email_address = Column('email_address', String(64), nullable=False,)
	user_password = Column('user_password', String(128), nullable=False,)


class Categories(Base):
	__tablename__ = 'categories'
	category_id = Column('category_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	category_name = Column('category_name', String(30), nullable=False, unique=True)
	classes = relationship('Classes', back_populates='categories')


class Classes(Base):
	__tablename__ = 'classes'
	class_id = Column('class_id', Integer, nullable=False, primary_key=True, autoincrement=True)
	class_name = Column('class_name', String(30), nullable=False, unique=True)
	category_id = Column('category_id', Integer, ForeignKey(Categories.category_id))
	categories = relationship('Categories', back_populates='classes')


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
		'sys.argv': sys.argv
		})
	main()
	
	# # Usersテーブルを削除する
	# Users.__table__.drop(ENGINE)