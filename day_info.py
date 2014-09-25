import urllib.request
import urllib.parse
import bs4
import datetime

class DayInfo:
	url = 'http://astro.kasi.re.kr/Life/Knowledge/sunmoon_map/sunmoon_popup.php'
	query = None
	data = []

	location = None
	year = None
	month = None

	def __init__(self, location=None, year=None, month=None):
		self.location = location
		self.year = year
		self.month = month

	def set_month(self, month):
		self.month = month

	def set_year(self, year):
		self.year = year

	def read_data(self):
		self.query = urllib.parse.urlencode({'year':self.year, 'month':self.month, 'location':self.location.encode('euc-kr')})
		self.query = self.query.encode('euc-kr')

		req = urllib.request.Request(self.url, self.query)
		f = urllib.request.urlopen(req)
		data = f.read().decode('euc-kr')
		f.close()

		soup = bs4.BeautifulSoup(data)
		day_info = soup.tbody.find_all('tr')
		
		for info in day_info:
			sunrise_info = info.find_all('td')
			# print(sunrise_info[2].text)
			self.data.append(sunrise_info[2].text)


	def get_day_info(self, month, day):
		if self.data == None:
			read_data()

		sunrise = self.data[day-1]

		return datetime.time(int(sunrise.split(':')[0]), int(sunrise.split(':')[1]))


