import sys
from blowfish import Blowfish

MODE_ENCRYPT = '-e'
MODE_DECRYPT = '-d'

def main(mode, key, infile, outfile):

    cipher = Blowfish(bytearray.fromhex(key))
    text = infile.read()
    
    size = Blowfish.blockSize()
    
    for i in range(0,len(text),size):
        block = bytearray(text[i:(i+size)])
        
        if len(block)<size:
            for _ in range(size-len(block)):
                block.append(0)
        
        if mode==MODE_ENCRYPT:
            cipher.encrypt(block)
                    
        elif mode==MODE_DECRYPT:
            cipher.decrypt(block)
    
        outfile.write(block)
        outfile.flush()
 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fishc.py {-e/-d} key [inputfile] [outputfile]")
        sys.exit(1)
    else:
        infile,outfile = None, None
        try:
            infile = open(sys.argv[3], 'rb')
            outfile = open(sys.argv[4], 'wb')
        except:
            print("Couldn't open a file for reading and/or writing, using stdin and stdout instead", file=sys.stderr)
            infile = sys.stdin.buffer
            outfile = sys.stdout.buffer
        main(sys.argv[1], sys.argv[2], infile, outfile)
