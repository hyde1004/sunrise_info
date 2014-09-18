import unittest

class TestRunRiseInfo(unittest.TestCase):
	def test_sample(self):
		self.assertEqual(1, 1)

	def test_get_html(self):
		self.assertTrue('일출몰' == '일출몰')	
		
if __name__== '__main__':
	unittest.main()
