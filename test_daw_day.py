import unittest
import draw_day
import datetime

class TestDrawDay(unittest.TestCase):
	def test_init(self):
		a = draw_day.DrawDay()

	def test_get_data(self):
		day_info = draw_day.DrawDay()
		data = [datetime.datetime(2014,9,25, 6, 2), datetime.datetime(2014,9,26, 6,4), datetime.datetime(2014, 9, 27, 6, 7)]

		out = day_info.get_data(data)
		self.assertEqual(out, ([735501, 735502, 735503], [0.2513888889, 0.2527777777, 0.254861111])) 

if __name__ == '__main__':
	unittest.main()