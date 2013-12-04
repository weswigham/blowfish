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
        t = datetime.now()
        #print("Starting trial at " +str(t))
        zero_key = bytearray(b'\x00' * Blowfish.keySize())
        self.cipher = Blowfish(zero_key)
        for i in range(self.n):
            self.test_once()
        y = datetime.now()
        t = y - t
        #print("Ending timetrial at " + str(y))
        #print("Total time taken: "+str(t))

    def test_once(self):
        

        zero_block = bytearray(b'\x00' * Blowfish.blockSize())
        self.cipher.encrypt(zero_block)
        #print(zero_block)



x = TestRunningTime()
x.setUp()
x.n = 2500000
cProfile.run('x.test_ntimes()')
