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
		# self.assertAlmostEqual(out, ([735501, 735502, 735503], [0.2513888889, 0.2527777777, 0.254861111])) 
		self.assertAlmostEqual(out[0][0], 735501)
		self.assertAlmostEqual(out[1][0], 0.2513888889)

		self.assertAlmostEqual(out[0][1], 735502)
		self.assertAlmostEqual(out[1][1], 0.2527777777)

		self.assertAlmostEqual(out[0][2], 735503)
		self.assertAlmostEqual(out[1][2], 0.254861111)


if __name__ == '__main__':
	unittest.main()