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
        zero_key = bytearray(b'\x00' * Blowfish.keySize())
        self.cipher = Blowfish(zero_key)
        for i in range(self.n):
            self.test_once()

    def test_once(self):
        zero_block = bytearray(b'\x00' * Blowfish.blockSize())
        self.cipher.encrypt(zero_block)
        #print(zero_block)
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python timetrial.py [number of trials]")
        sys.exit(1)
    else:
        x = TestRunningTime()
        x.setUp()
        x.n = int(sys.argv[1])
        cProfile.run('x.test_ntimes()')
        print('Done.')
