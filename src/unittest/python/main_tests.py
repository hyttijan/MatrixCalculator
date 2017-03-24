
import unittest
from main import main, parseMatrix
class MainTest(unittest.TestCase):
    def setUp(self):
        main()
    def testParseMatrix(self):
        parseMatrix()

if __name__ == '__main__':
    unittest.main()
