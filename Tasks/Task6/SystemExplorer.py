import os
import AES_realisation

def main():
    password = raw_input("Enter an encryption password: ")
    password = AES_realisation.getKey(password)
    print("SHA 256 genereated password: " + password)

    with open("shaKeys", "w") as passwordFile:
        passwordFile.write(password)

    for root, dirs, files in os.walk("C:\\TestFolder", topdown=True):
        if (str(root).__contains__("System32")):
            continue
        else:
            for fileName in files:
                filePath = root + "\\" + fileName
                AES_realisation.encrypt(password, filePath)


    for root, dirs, files in os.walk("C:\\TestFolder", topdown=True):
        if (str(root).__contains__("System32")):
            continue
        else:
            for fileName in files:
                filePath = root + "\\" + fileName
                AES_realisation.decrypt(password, filePath)

if __name__ == "__main__":
    main()
