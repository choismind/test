import unittest
import site
site.addsitedir("..")
from tests.root_path import LibmeTestCase


def suite():
	suit_set = unittest.TestSuite()
	suit_set.addTests([LibmeTestCase("testRootpath"),
						LibmeTestCase("testUpper")])
	return suit_set

if __name__ == "__main__":
	tests = suite()
	runner = unittest.TextTestRunner()
	runner.run(tests)
