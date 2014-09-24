import urllib.request
import urllib.parse
import bs4

class DayInfo:
	url = 'http://astro.kasi.re.kr/Life/Knowledge/sunmoon_map/sunmoon_popup.php'
	query = None
	data = None

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
		self.data = f.read()
		f.close()
