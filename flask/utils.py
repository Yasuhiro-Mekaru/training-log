import base64
import hashlib
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


logger.info({
	'action': 'utils.py',
	'status': 'readed'
	})

# salt = base64.b64encode(os.urandom(32))
# logger.info({
# 	'action': 'utils.py',
# 	'salt': salt
# 	})


def hash_password(password):
	password = bytes(password, 'utf-8')
	digest = hashlib.sha256(password).hexdigest()
	logger.info({
		'action': 'utils.py hash_password',
		'digest': digest,
		'digest type': type(digest)
		})
	return digest

