
import unittest
from ut_googl import TestGoogl
from ut_bitly import TestBitly
from ut_tinyurlcom import TestTinyUrlcom
from ut_vgd import TestVgd
from ut_isgd import TestIsgd

def run_test(class_to_test):
    suite = unittest.TestLoader().loadTestsFromTestCase(class_to_test)
    unittest.TextTestRunner(verbosity=2).run(suite)

if '__main__' == __name__:
    print '%70s' %'Testing Goo.gl API'
    print '='*70
    run_test(TestGoogl)

    print '%70s' %'Testing Bit.ly API'
    print '='*70
    run_test(TestBitly)

    print '%70s' %'Testing TinyUrl.com API'
    print '='*70
    run_test(TestTinyUrlcom)

    print '%70s' %'Testing v.gd API'
    print '='*70
    run_test(TestVgd)

    print '%70s' %'Testing is.gd API'
    print '='*70
    run_test(TestIsgd)
