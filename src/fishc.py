import sys
from blowfish import Blowfish

MODE_ENCRYPT = '-e'
MODE_DECRYPT = '-d'
MODE_READHEX = '-h'

def main(mode, key, infile, outfile, ashex):

    cipher = Blowfish(bytearray.fromhex(key))
    text = infile.read()
    
    if ashex:
        text = bytearray.fromhex(text.strip())
        print(text)
    
    for i in range(0,len(text),cipher.blockSize()):
        block = bytearray()
        if i+cipher.blockSize() <= len(text):
            block.extend(text[i:i+cipher.blockSize()])
        else:
            block.extend(text[i:])
            remainder = cipher.blockSize()-len(block) #Not sure if necessary
            for j in range(remainder):
                block.append(0)
        
        out = b''
        
        if mode==MODE_ENCRYPT:
            out = cipher.encrypt(block)
        elif mode==MODE_DECRYPT:
            out = cipher.decrypt(block)
            
        if ashex:
            processed = ""
            for num in out:
                processed += hex(num)[2:]
            out = processed
            print(out)
            
        outfile.write(out or b'')
 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fishc.py {-e/-d} ["+MODE_READHEX+"] key [inputfile] [outputfile]")
        sys.exit(1)
    else:
        if sys.argv[2]==MODE_READHEX:
            infile,outfile = None, None
            try:
                infile = open(sys.argv[4], 'r')
                outfile = open(sys.argv[5], 'w')
            except:
                print("Couldn't open a file for reading and/or writing, using stdin and stdout instead", file=sys.stderr)
                infile = sys.stdin
                outfile = sys.stdout
            main(sys.argv[1], sys.argv[3], infile, outfile, True)
        else:
            infile,outfile = None, None
            try:
                infile,outfile = open(sys.argv[3], 'rb'),open(sys.argv[4], 'wb')
            except:
                print("Couldn't open a file for reading and/or writing, using stdin and stdout instead", file=sys.stderr)
                infile = sys.stdin.buffer
                outfile = sys.stdout.buffer
            main(sys.argv[1], sys.argv[2], infile, outfile, False)