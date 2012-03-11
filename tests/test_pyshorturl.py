
import unittest
from ut_googl import TestGoogl
from ut_bitly import TestBitly

def run_test(class_to_test):
    suite = unittest.TestLoader().loadTestsFromTestCase(class_to_test)
    unittest.TextTestRunner(verbosity=2).run(suite)

if '__main__' == __name__:
    print '%70s' %'Testing Googl API'
    print '-'*70
    run_test(TestGoogl)

    print '%70s' %'Testing Bitly API'
    print '-'*70
    run_test(TestBitly)
