# 단위 테스트 시 아래 comment 기호 삭제
#import site
#site.addsitedir("../..")
import libme
import unittest


class LibmeTestCase(unittest.TestCase):

	def setUp(self):
		self.app = libme.app.test_client()

	def testRootpath(self):
		read_page = self.app.get("/")
		self.assertIn(b"Hello World!", read_page.get_data(), "예상한 응답이 아닙니다.")

	@unittest.skip("demo")
	def testUpper(self):
		self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
	unittest.main()
