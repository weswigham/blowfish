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
x.n = 1000000 #int(input("How many times should we encrypt the all 0 bitstring?\n"))

if False: # Using cProfile
    cProfile.run('x.test_ntimes()')

if True: # Plain ol' time trial
    start_t = datetime.now()
    print("Starting trial at " + str(start_t))

    x.test_ntimes()
    print()

    end_t = datetime.now()
    total_t = end_t - start_t
    print("Ending timetrial at " + str(end_t))
    print("Total time taken: "+str(total_t))

print('Done.')
