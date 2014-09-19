import unittest
import urllib.request
import bs4

class TestRunRiseInfo(unittest.TestCase):
	def test_sample(self):
		self.assertEqual(1, 1)

	def test_get_html(self):
		url = 'http://astro.kasi.re.kr/Life/Knowledge/sunmoon_map/sunmoon_popup.php?year=2014&month=9&location=%C3%B5%BE%C8'
		req = urllib.request.Request(url)

		f = urllib.request.urlopen(req)
		html = f.read().decode('euc-kr')
		f.close()

		self.assertTrue('일출몰' in html)	

	def test_get_local_html(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		self.assertTrue('일출몰' in html)

	def test_get_read_soup(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		soup = bs4.BeautifulSoup(html)
		self.assertEqual(soup.title.text, '월별 해/달 출몰시각')	

	def test_get_sunrise_time(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		soup = bs4.BeautifulSoup(html)

		# 일짜별 데이터는 tbody에서 순서대로 가는 것이 아니라, tbody안에서 필요한 테그만 붙이면 된다.
		# tr은 날짜별 데이터
		day_info = soup.tbody.find_all('tr')

		# find_all의 결과는 ResultSet이다. 
		# ResultSet은 list의 subclass이고, 각 원소가 Tag 객체이다.
		# find_all 결과에 다시 find_all을 하고 싶다면, 
		# 각 원소에 다시 find_all을 적용하면 된다.

		# for info in day_info:
		# 	sunrise_info = info.find_all('td')
		#	print(sunrise_info[2].text)
		sunrise_info = day_info[0].find_all('td')

		self.assertEqual(sunrise_info[2].text, '06:02')	

			
if __name__== '__main__':
	unittest.main()
