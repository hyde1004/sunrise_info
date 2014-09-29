import datetime
import matplotlib.dates
import matplotlib.pyplot as plt
import math
import day_info

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


day = day_info.DayInfo('천안')
day.set_year(2014)
day.set_month(9)
day.read_data()
b = []
for a in day.data:
	b.append(int(a.split(':')[0])*60+int(a.split(':')[1]))

#print(b)
plt.plot(b)
plt.show()
