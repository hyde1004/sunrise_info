import matplotlib.pyplot as plt
import day_info


day = day_info.DayInfo('천안')
day.set_year(2014)

b = []

for month in range(12):
		day.set_month(month+1)
		day.read_data()
		# print(len(day.data))
		for a in day.data:
			time = a.split(':')
			b.append(int(time[0])*60 + int(time[1]))   # convert to minutes

plt.plot(b)
plt.show()
