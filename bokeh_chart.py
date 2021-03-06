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
	def __init__(self, df=None, width=None, height=None):
		self.df = df
		self.width = width
		self.height = height


	def create_chart(self):
		# DataFrameの値を Bokeh用セット
		source = ColumnDataSource(self.df)
		source.add(self.df.index, 'index')
		
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
					'@index': 'datetime',
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
				plot_width=300,
				plot_height=300,
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
				plot_width=300,
				plot_height=300,
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


		logger.info({
			'action': 'bokeh_chart.py',
			'p: ': p
			})

		return p


	def create_milage_chart(self):
		# DataFrameの値を Bokeh用セット
		source = ColumnDataSource(self.df)
		source.add(self.df.index, 'index')
		
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
					'@index': 'datetime',
					},
				mode='mouse')

		# figureオブジェクトを生成
		# figureオブジェクトのlineプロパティに値を追加する
		milage_plot = figure(
				plot_width=self.width,
				plot_height=self.height,
				x_axis_type="datetime",
				x_axis_label = "date",
				y_axis_label = "distance(km)",
				title='Milage Line_Chart',
				tools=[milage_hover_tool, tools]
			)
		milage_plot.line(
				x = "index",
				y = "Sum_milage",
				source = source,
				legend = "走行距離",
				color = "blue",
				line_width = 2
			)
		milage_plot.line(
				x = "index",
				y = "Sum_target",
				source = source,
				legend = "目標値",
				color = "red",
				line_width = 2
			)
		milage_plot.add_layout(milage_plot.legend[0], 'below')

		return milage_plot


	def create_elevation_chart(self):
		# DataFrameの値を Bokeh用セット
		source = ColumnDataSource(self.df)
		source.add(self.df.index, 'index')
		
		# チャートのツールを設定
		tools = "pan,box_zoom,reset,save"

		# チャート内のツールチップのツールチップを設定
		elevation_hover_tool = HoverTool(
				tooltips=[
					('日付', "@index{%F}"),
					('当日獲得標高', "@Elevation"+' (m)'),
					('合計獲得標高', '@Sum_elevation'+' (m)')],
				formatters={
					'@index': 'datetime',
					},
				mode='mouse')

		# figureオブジェクトを生成
		# figureオブジェクトのlineプロパティに値を追加する
		elevation_plot = figure(
				plot_width=300,
				plot_height=300,
				x_axis_type="datetime",
				x_axis_label = "date",
				y_axis_label = "height(m)",
				title='Elevation Line_Chart',
				tools=[elevation_hover_tool, tools]
			)
		elevation_plot.line(
				x = "index",
				y = "Sum_elevation",
				source = source,
					legend = "獲得標高",
				color = "blue",
				line_width = 2
			)
		elevation_plot.add_layout(elevation_plot.legend[0], 'below')

		return elevation_plot
