import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256

partSize = 64 * 1024

def encrypt(key, fileName):
    outputFileName = fileName + "_e"
    fileSize = str(os.path.getsize(fileName)).zfill(16)
    iv = Random.new().read(16)
    print ("Encryption iv: " + iv)

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(fileName, 'rb') as inputFile:
        with open(outputFileName, 'wb') as outputFile:
            outputFile.write(fileSize.encode('utf-8'))
            outputFile.write(iv)

            while(True):
                chunk = inputFile.read(partSize)
                if len(chunk) == 0:
                    break
                elif len(chunk)%16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16 ))
                outputFile.write(encryptor.encrypt(chunk))

def decrypt(key, inputFileName):
    outputFileName = inputFileName[:len(inputFileName)-2] + "_d"

    with open(inputFileName, 'rb') as inputFile:
        originalFileSize = int(inputFile.read(16))
        iv = inputFile.read(16)
        print ("Decryption iv: " + iv)
        decryptor = AES.new(key,AES.MODE_CBC, iv)
        with open(outputFileName, 'wb') as outputFile:
            while True:
                chunk = inputFile.read(partSize)
                if len(chunk) == 0:
                    break

                outputFile.write(decryptor.decrypt(chunk))

def getKey(inputKey):
    hasher = SHA256.new(inputKey.encode("utf-8"))
    return hasher.digest()


if __name__ == "__main__":
    encrypt('Some random key.', '1.pdf')
    decrypt('Some random key.','1.pdf_e')