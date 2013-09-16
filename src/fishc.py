import sys
from blowfish import Blowfish

MODE_ENCRYPT = '-e'
MODE_DECRYPT = '-d'

def main(mode, key, infile, outfile):
    cipher = Blowfish(key)
    text = infile.read()
    
    for i=0,len(text),cipher.blockSize():
        block = ()
        if i+cipher.blockSize() <= len(text):
            block = text[i:i+cipher.blockSize()-1]
        else:
            block = text[i:]
            remainder = cipher.blockSize()-len(block) #Not sure if necessary
            for j=0,remainder:
                block.append(b'0')
        
        out = ()
        
        if mode==MODE_ENCRYPT:
            out = cipher.encrypt(block)
        elif mode==MODE_DECRYPT:
            out = cipher.decrypt(block)
            
        outfile.write(out)
 

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python fishc.py {-e/-d} key [inputfile] [outputfile]")
        return 
    else:
        infile,outfile = ()
        try:
            infile = open(sys.argv[3], 'rb')
        except:
            infile = sys.stdin.buffer
        try:
            outfile = open(sys.argv[4], 'wb')
        except:
            outfile = sys.stdout.buffer
        main(sys.argv[1], sys.argv[2], infile, outfile)