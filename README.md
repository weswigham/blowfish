[blowfish](http://weswigham.github.io/blowfish)
========

Block cipher implementation in Python 3

Tests
-----

Two tests are included; standard test vectors of the blowfish function itself in `battery.py` and a profiler/time trial in `timetrial.py`.
These tests may be run by `cd`'ing into the `src` directory and running them with `python3 ../tests/battery.py` or `python3 ../tests/timetrial.py 2500000` (Where 2500000 is the number of times you want to run the encryption function in the trial.)

Encrypting/Decrypting Files
---------------------------

Included is `fishc.py`, which encrypts and decrypts whole files (in Electronic Codebook mode). To use it, `cd` into the `src` dir and run `python3 fishc.py {-e/-d} [key (hex)] [input file] [output file]`. Use `-e` for encryption and `-d` for decryption. 
