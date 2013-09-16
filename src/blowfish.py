class Blowfish():

    def __init__(self,key):
        self.key = key

    def blockSize(self):
        """
        Returns the cipher's block size in bytes
        """
        return 8
        
    def keySize(self):
        """
        Returns the cipher's key size in bytes
        """
        #32 bits up to 448 bits
        return 56 #448 bits!
        
    def setKey(self, key):
        """
        Sets the cipher's key
        """
        self.key = key
        
    def encrypt(self, plain):
        """
        Given a plaintext block, produces a ciphertext
        """
        pass 
        
    def decrypt(self, cipher):
        """
        Given a ciphertext block, produces a plaintext
        """
        pass 