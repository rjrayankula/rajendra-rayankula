import pandas as pands
import matplotlib.pyplot as grph_plot

data_frame = pands.read_csv('visitors_room_reservation.csv')
data_frame.head(12)
data_frame = data_frame.set_index('2019 Year')


fig, axes_obj = grph_plot.subplots()
data_frame.plot(kind='line', ax=axes_obj)
grph_plot.ylabel('visitors')
axes_obj.grid(color='gray', linestyle='-', alpha=0.3)