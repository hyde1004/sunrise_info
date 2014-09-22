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
		f = open('./sunrise.html', 'rb')
		html = f.read().decode('utf-8')
		f.close()

		soup = bs4.BeautifulSoup(html)

		# 일짜별 데이터는 tbody에서 순서대로 가는 것이 아니라, tbody안에서 필요한 테그만 붙이면 된다.
		# tr은 날짜별 데이터
		day_info = soup.tbody.find_all('tr')

		# 일출시간은 세번째 td만을 뽑아낸다.
		sunrise_info = day_info.find_all('td')

		for info in day_info:
			sunrise_info = info.find_all('td')
#			print(sunrise_info[2].text)

		self.assertEqual(sunrise_info[2].text, '06:02')	

			
if __name__== '__main__':
	unittest.main()
