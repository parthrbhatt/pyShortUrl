
import unittest
from ut_googl import TestGoogl

if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogl)
    unittest.TextTestRunner(verbosity=2).run(suite)
