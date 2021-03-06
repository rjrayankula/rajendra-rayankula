import pandas as pands
import matplotlib.pyplot as grph_plot

data_frame = pands.read_csv('term_wise_visitors.csv')
data_frame.head(12)
data_frame = data_frame.set_index('2019 Year')


fig, axes_obj = grph_plot.subplots()
data_frame.plot(kind='bar', ax=axes_obj)
grph_plot.ylabel('visitors')
axes_obj.grid(color='gray', linestyle='-', alpha=0.3)