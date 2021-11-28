import logging
import sys

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info({
	'action': 'database.py',
	'status': 'readed'
	})

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
	'admin', 'password', 'database', 'test_training_log'
	)

ENGINE = create_engine(DATABASE, encoding='utf-8', echo=False)

session = scoped_session(
	sessionmaker(
		autocommit = False,
		autoflush = True,
		bind = ENGINE
	)
)

Base = declarative_base()
Base.query = session.query_property()
