import logging

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info({
	'action': 'bokeh_chart.py',
	'status': 'readed'
	})


class My_bokeh_chart(object):
	"""docstring for My_bokeh_chart"""
	def __init__(self, df):
		self.df = df


	def create_chart(self):
		pass

