import urllib.request
import bs4

class DayInfo:
	location = None
	year = None
	month = None
	def __init__(self, location=None, year=None, month=None):
		self.location = location
		self.year = year
		self.month = month

	def set_year_month(self):
		pass

	def get_sunrise_time(self):
		pass