import logging

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import gridplot
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
	    milage_hover_tool = HoverTool(
	    	tooltips=[
	    		('日付', "@index{%F}"),
	    		('当日走行距離', '@Milage'+' (km)'),
	    		('合計走行距離', '@Sum_milage'+'( km)'),
	    		('目標距離', '@Sum_target'+' (km)')],
	    	formatters={
	    		'index': 'datetime',
	    		},
	    	mode='mouse')

		elevation_hover_tool = HoverTool(
			tooltips=[
				('日付', "@index{%F}"),
				('当日獲得標高', "@Elevation"+' (m)'),
				('合計獲得標高', '@Sum_elevation'+' (m)')],
			formatters={
				'index': 'datetime',
				},
			mode='mouse')

		left_plot = figure(
		    x_axis_type="datetime",
		    x_axis_label = "date",
		    y_axis_label = "distance(km)",
		    title='Milage Line_Chart',
		    tools=[milage_hover_tool, tools]
		)
		left_plot.line(
		    x = "index",
		    y = "Sum_milage",
		    source = source,
		    legend = "走行距離",
		    color = "blue",
		    line_width = 2
		)
		left_plot.line(
		    x = "index",
		    y = "Sum_target",
		    source = source,
		    legend = "目標値",
		    color = "red",
		    line_width = 2
		)

		right_plot = figure(
		    x_axis_type="datetime",
		    x_axis_label = "date",
		    y_axis_label = "height(m)",
		    title='Elevation Line_Chart',
		    tools=[elevation_hover_tool, tools]
		)
		right_plot.line(
		    x = "index",
		    y = "Sum_elevation",
		    source = source,
		    legend = "獲得標高",
		    color = "blue",
		    line_width = 2
		)

		p = gridplot([[left_plot, right_plot]])













	    # hover_tool = HoverTool(
	    #     tooltips=[
	    #         ('index', "@index{%F %T}"),
	    #         ('Milage', "@Milage"),
	    #     ],
	    #     formatters={
	    #         'index': 'datetime',
	    #     },
	    #     mode='vline')

	    # # figureオブジェクトを生成
	    # p = figure(x_axis_type="datetime",
	    #            plot_width=1000,
	    #            plot_height=400,
	    #            title='Milage Line_Chart',
	    #            tools=[hover_tool, tools])

	    # p.vbar(
	    # 	x='index',
	    # 	top='Milage',
	    # 	source=source,
	    # 	width=0.3,
	    # 	bottom=0,
	    # 	color='firebrick')

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

