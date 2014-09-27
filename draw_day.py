import datetime
import matplotlib.dates
import math

class DrawDay():
	days = []
	times = []

	def __init__(self):
		pass

	def get_data(self, day_info):
		for day in day_info:
			info = math.modf(matplotlib.dates.date2num(day))

			self.times.append(info[0])
			self.days.append(info[1])
		# self.days = [math.trunc(matplotlib.dates.date2num(day)) for day in day_info]
		# #self.days = [datetime.date(day.year, day.month, day.day) for day in day_info]
		# self.times = [matplotlib.dates.date2num(day) - math.trunc(matplotlib.dates.date2num(day))  for day in day_info]
		# #return 0
		# #return ([735501, 735502, 735503], [0.2513888889, 0.2527777777, 0.254861111])
		return (self.days, self.times)