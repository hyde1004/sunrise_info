import urllib.request
import bs4

class DayInfo:
	host = 'http://astro.kasi.re.kr/Life/Knowledge/sunmoon_map/sunmoon_popup.php?'

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

	def request_url(self):
		# data = urllib.parse.urlencode({'location':self.location, 'year':self.year, 'month':self.month})
		# data = data.encode('euc-kr')

		data = 'location' + str(self.location.encode('cp949'))
		return data