import unittest
import sys

sys.path.append("../src/")
from blowfish import Blowfish

class TestRunningTime(unittest.TestCase):
    def setUp(self):
        self.n = 1

    def test_ntimes(self):
        for i in range(self.n):
            self.test_once()

    def test_once(self):
        zero_key = bytearray(b'\x00' * Blowfish.keySize(None))
        self.cipher = Blowfish(zero_key)

        zero_block = bytearray(b'\x00' * Blowfish.blockSize(None))
        self.cipher.encrypt(zero_block)
        print(zero_block)



x = TestRunningTime()
x.setUp()
x.test_ntimes()
