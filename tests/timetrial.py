import unittest
import sys
from datetime import datetime
import cProfile

sys.path.append("../src/")
from blowfish import Blowfish

class TestRunningTime(unittest.TestCase):
    def setUp(self):
        self.n = 1

    def test_ntimes(self):
        zero_key = bytes(b'\x00' * Blowfish.keySize())
        self.cipher = Blowfish(zero_key)
        for i in range(self.n):
            self.test_once()
            if i % 1000 == 0:
                if i % 100000 == 0:
                    print()
                print('.', end='')
                sys.stdout.flush()

    def test_once(self):
        zero_block = bytes(b'\x00' * Blowfish.blockSize())
        self.cipher.encrypt(zero_block)
        #print(zero_block)

x = TestRunningTime()
x.setUp()
x.n = 2500000
cProfile.run('x.test_ntimes()')
print('Done.')
