import sys
from blowfish import Blowfish

MODE_ENCRYPT = '-e'
MODE_DECRYPT = '-d'

def main(mode, key, infile, outfile):
    cipher = Blowfish(bytearray.fromhex(key))
    text = infile.read()
    
    for i in range(0,len(text),cipher.blockSize()):
        block = bytearray()
        if i+cipher.blockSize() <= len(text):
            block.extend(text[i:i+cipher.blockSize()])
        else:
            block.extend(text[i:])
            remainder = cipher.blockSize()-len(block) #Not sure if necessary
            for j in range(remainder):
                block.append(0)
        
        out = ()
        
        if mode==MODE_ENCRYPT:
            out = cipher.encrypt(block)
        elif mode==MODE_DECRYPT:
            out = cipher.decrypt(block)
            
        outfile.write(out or b'')
 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fishc.py {-e/-d} key [inputfile] [outputfile]")
        sys.exit(1)
    else:
        try:
            infile,outfile = open(sys.argv[3], 'rb'),open(sys.argv[4], 'wb')
            main(sys.argv[1], sys.argv[2], infile, outfile)
        except:
            infile = sys.stdin.buffer
            outfile = sys.stdout.buffer
            main(sys.argv[1], sys.argv[2], infile, outfile)