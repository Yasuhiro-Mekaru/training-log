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
		# DataFrameの値を Bokeh用セット
	    source = ColumnDataSource(self.df)
	    source.add(self.df.index, 'index')

	    # output_file("milage_log.html")
	    
	    # チャートのツールを設定
	    tools = "pan,box_zoom,reset,save"

	    # チャート内のツールチップのツールチップを設定
	    hover_tool = HoverTool(
	        tooltips=[
	            ('index', "@index{%F %T}"),
	            ('Milage', "@Milage"),
	        ],
	        formatters={
	            'index': 'datetime',
	        },
	        mode='vline')

	    # figureオブジェクトを生成
	    p = figure(x_axis_type="datetime",
	               plot_width=1000,
	               plot_height=400,
	               title='Milage Line_Chart',
	               tools=[hover_tool, tools])

	    p.vbar(
	    	x='index',
	    	top='Milage',
	    	source=source,
	    	width=10.0,
	    	bottom=0,
	    	color='firebrick')

	    # # 終値の描画設定
	    # p.circle(x='index',
	    #          y='Milage',
	    #          source=source,
	    #          size=1,
	    #          line_color='red',
	    #          fill_color='red',
	    #          fill_alpha=0.3)

	    # # 終値のラインを設定
	    # p.line(x='index',
	    #        y='Milage',
	    #        source=source,
	    #        line_color='blue',
	    #        line_alpha=0.5,
	    #        legend='Milage',
	    #       )

	    # # SMA28のラインを設定
	    # p.line(x='index',
	    #       y='Elevation',
	    #       source=source,
	    #       line_color='orange',
	    #       line_alpha=1.0,
	    #       legend='Elevation')

	    logger.info({
	    	'action': 'bokeh_chart.py',
	    	'p: ': p
	    	})

	    # figureインスタンスを描画
	    # show(p)
	    return p

