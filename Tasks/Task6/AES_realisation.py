import os
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256

partSize = 64 * 1024


def encrypt(key, fileName):
    outputFilePath = fileName + "_e"

    fileSize = str(os.path.getsize(fileName)).zfill(16)
    initVector = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, initVector)

    with open(fileName, 'rb') as inputFile:
        with open(outputFilePath, 'wb') as outputFile:
            outputFile.write(fileSize.encode('utf-8'))
            outputFile.write(initVector)

            while (True):
                chunk = inputFile.read(partSize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                outputFile.write(encryptor.encrypt(chunk))
    os.remove(fileName)


def decrypt(key, inputFileName):
    if (not inputFileName[-2:] == "e_"):
        print("File: {} wasn't encrypted".format(inputFileName))
        return
    outputFileName = inputFileName[:len(inputFileName) - 2]

    with open(inputFileName, 'rb') as inputFile:
        originalFileSize = int(inputFile.read(16))
        iv = inputFile.read(16)
        print ("Decryption iv: " + iv)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(outputFileName, 'wb') as outputFile:
            while True:
                chunk = inputFile.read(partSize)
                if len(chunk) == 0:
                    break

                outputFile.write(decryptor.decrypt(chunk))
    os.remove(inputFileName)


def getHashKey(inputKey):
    hasher = SHA256.new(inputKey.encode("utf-8"))
    return hasher.digest()
