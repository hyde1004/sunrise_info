import urllib.request
import urllib.parse
import bs4
import datetime

class DayInfo:
	address = 'http://astro.kasi.re.kr/Life/Knowledge/sunmoon_map/sunmoon_popup.php'
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
		# urlencode는 default encoding으로 'utf-8'을 사용하므로,
		# euc-kr encoding을 명시적으로 넘겨주어야 한다.
		# 그렇지않으면, utf-8로 이미 변경된채로 다시 euc-kr로 재변환하게 된다.
		self.query = urllib.parse.urlencode({'year':self.year, 'month':self.month, 'location':self.location}, encoding='euc-kr')
		url = "%s?%s" % (self.address, self.query)

		f = urllib.request.urlopen(url)
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


