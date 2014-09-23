import unittest
import urllib.request
import bs4
import matplotlib.pyplot as plt
import day_info

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

	@unittest.skip("local html skipping")
	def test_get_local_html(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		self.assertTrue('일출몰' in html)

	@unittest.skip("local html skipping")
	def test_get_read_soup(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		soup = bs4.BeautifulSoup(html)
		self.assertEqual(soup.title.text, '월별 해/달 출몰시각')	

	@unittest.skip("local html skipping")
	def test_get_sunrise_time(self):
		f = open('./sunrise.html', 'rb')
		html = f.read().decode('utf-8')
		f.close()

		# html tag structure
		#
		# <html>
		# 	<head>
		# 	</head>

		# 	<body>
		# 		<div class="graybox" style="width:650px;">
		# 			<div>
		# 				<table>
		# 				</table>
		# 			</div>

		# 			<TABLE>
		# 				<thead>
		# 				</tead>

		# 				<tbody>
		# 					<tr>
		# 						<td>1</td>
		# 						<td>06:02</td>  <- to be parsed
		# 					</tr>
		#
		#					<tr>
		#						<td>2</td>
		#						<td>06:03</td>	<- to be parsed		
		#					</tr>
		# 				</tbody>
		# 			</table>
		# 		</div>
		# 	</body>
		# </html>

		soup = bs4.BeautifulSoup(html)

		# 처음에는 계층적인 구조로 tag를 내려가면서 parsing하려고 하였다. (soup.html.body...)
		# 그러나 soup는 동일한 tag 중 첫번째 tag를 찾기도 했고,
		# tag를 이용한 방법으로 잘 되지 않았다.

		# 특이 사항은 tag를 사용할때 상위부모-부모-자식을 다 명시할 필요없이,
		# 필요한 부모만 넣어주고 중간은 skip해도 되었다.

		# 일짜별 데이터는 tbody에서 순서대로 가는 것이 아니라, tbody안에서 필요한 테그만 붙이면 된다.
		# tr은 날짜별 데이터를 담고 있다.
		day_info = soup.tbody.find_all('tr')

		# find_all의 결과는 parsing된 Tag를 원소로 가지는 ResultSet이다. 
		# ResultSet은 list의 subclass인데, 각 원소가 Tag 객체이다.
		# 따라서, find_all 결과에 다시 find_all을 하고 싶다면, 
		# 각 원소에 다시 find_all을 적용하면 된다.

		# for info in day_info:
		# 	sunrise_info = info.find_all('td')
		#	print(sunrise_info[2].text)
		sunrise_info = day_info[0].find_all('td')

		self.assertEqual(sunrise_info[2].text, '06:02')	

	@unittest.skip("local html skipping")
	def test_sunset_time(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		soup = bs4.BeautifulSoup(html)
		day_info = soup.tbody.find_all('tr')
		sunset_info = day_info[0].find_all('td')


		self.assertEqual(sunset_info[4].text, '19:01')

	@unittest.skip("local html skipping")
	def test_draw_day(self):
		f = open('./sunrise.html', 'rt')
		html = f.read()
		f.close()

		sunrise_times = []
		sunset_times = []
		soup = bs4.BeautifulSoup(html)
		day_info = soup.tbody.find_all('tr')
		for info in day_info:
			sunrise_info = info.find_all('td')
			# print(sunrise_info[2].text)
			time1 = (sunrise_info[2].text).split(':')
			time2 = (sunrise_info[4].text).split(':')
			sunrise_times.append(int(time1[0])*60 + int(time1[1]))
			sunset_times.append(int(time2[0])*60 + int(time2[1]))

		# print(sunrise_time)
		day = list(range(1, len(sunrise_times)+1))
		# print(day)
		plt.plot(day, sunrise_times)
		plt.plot(day, sunset_times)
		plt.show()

		self.assertEqual(0, 0)

	def test_initialize(self):
		day = day_info.DayInfo()
		self.assertTrue(day != None)

		day = day_info.DayInfo('천안')
		self.assertEqual(day.location, '천안')

		day = day_info.DayInfo('천안', 2014, 9)
		self.assertEqual(day.year, 2014)
		self.assertEqual(day.month, 9)


if __name__== '__main__':
	unittest.main()
