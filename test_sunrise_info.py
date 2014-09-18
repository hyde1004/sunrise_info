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
		td = soup.html.body.div.tbody.tr.td #의문 : TABLE tag가 parsing되지 않는다!
		# print(td)
		self.assertEqual(td.text, '06:02')	

			
if __name__== '__main__':
	unittest.main()
